#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randrange as rnd, choice
from tkinter import *
import math

# print (dir(math))

import time

root = Tk()
fr = Frame(root)
root.geometry('1280x728')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class liquid_particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.r = 20
        self.color = 'blue'
        self.ball = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.gravitation = 0.9805
        self.dir = (self.vel_x, self.vel_y)
    def set_coords(self):
        canv.coords(self.ball, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.set_coords()

        if self.x >= 1280:
            self.vel_x = -self.vel_x
        if self.y >= 700:
            self.vel_y = -self.vel_y
        if self.x <= 0:
            self.vel_x = -self.vel_x
        if self.y <= 0:
            self.vel_y = -self.vel_y

class vector():
    def __init__(self, x, y):
        self.vel_x = x
        self.vel_y = y
        self.dir = (self.vel_x, self.vel_y)

def concat_vect(vect_1, vect_2):
    nand =  vector(vect_1.vel_x + vect_2.vel_x, vect_1.vel_y + vect_2.vel_y)
    return nand
def distance(ball_1, ball_2):
    return math.sqrt((ball_1.x-ball_2.x)**2+(ball_1.y-ball_2.y)**2)

def centre_vect(ball_1, ball_2):
    return vector(ball_1.x-ball_2.x, ball_1.y-ball_2.y)

def cos_angle(vect_1, vect_2):
    return (vect_1.vel_x*vect_2.vel_x + vect_2.vel_y*vect_1.vel_y)/((math.sqrt((vect_1.vel_x)**2 + (vect_1.vel_y)**2))*(math.sqrt((vect_2.vel_x)**2 + (vect_2.vel_y)**2)))

def norm_vect(vector):
    vector.vel_x, vector.vel_y = -vector.vel_y, vector.vel_x
    return vector

def speed(particle):
    return math.sqrt(particle.vel_x**2+particle.vel_y**2)

def len_norm_v(vector1, norm_vector):
    n = abs(cos_angle(vector1, norm_vector))*(math.sqrt(vector1.vel_x**2 + vector1.vel_y**2)/(math.sqrt(norm_vector.vel_x**2 + norm_vector.vel_y**2)))


    return vector(norm_vector.vel_x * n, norm_vector.vel_y * n)




def collision(ball_1 , ball_2):

    centre_vector = centre_vect(ball_1 , ball_2)

    norm_vector = norm_vect(centre_vector)

    norm_vector1 = len_norm_v(ball_1, norm_vector)

    norm_vector2 = len_norm_v(ball_2, norm_vector)

    cos_a1 = cos_angle(ball_1, norm_vector)

    cos_a2 = cos_angle(ball_2, norm_vector)

    if cos_a1>=0 and cos_a2<=0:
        t1x = norm_vector1.vel_x
        t1y = norm_vector1.vel_y
        minus_vect1 = vector(-ball_1.vel_x + t1x, -ball_1.vel_y + t1y)

        ball_1.vel_x = minus_vect1.vel_x + t1x
        ball_1.vel_y = minus_vect1.vel_y + t1y

        t2x = -norm_vector2.vel_x
        t2y = -norm_vector2.vel_y
        minus_vect2 = vector(-ball_2.vel_x +t2x, -ball_2.vel_y -t2y)

        ball_2.vel_x = (minus_vect2.vel_x + t2x)
        ball_2.vel_y = (minus_vect2.vel_y + t2y)

    elif cos_a2>0 and cos_a1<0:
        t1x = norm_vector1.vel_x
        t1y = norm_vector1.vel_y
        minus_vect1 = vector(-ball_1.vel_x - t1x, -ball_1.vel_y - t1y)

        ball_1.vel_x = minus_vect1.vel_x - t1x
        ball_1.vel_y = minus_vect1.vel_y - t1y
        print(t1x, t1y)
        print(minus_vect1.vel_x, minus_vect1.vel_y)
        print(ball_1.vel_x, ball_1.vel_y)
        t2x = norm_vector2.vel_x
        t2y = norm_vector2.vel_y
        minus_vect2 = vector(-ball_2.vel_x + t2x, -ball_2.vel_y + t2y)

        ball_2.vel_x = (minus_vect2.vel_x + t2x)
        ball_2.vel_y = (minus_vect2.vel_y + t2y)




particle1 = liquid_particle(200, 200)
particle2 = liquid_particle(600, 200)

particle2.vel_x = -0.3

particle1.vel_x = 0.2

particles = [particle1, particle2]

t = 0
while True:

    for x in particles:
        x.move()
    if distance(particle1 , particle2) > 40:
        t = 1
    if distance(particle1 , particle2) <= 40:
        if t == 1:

            collision(particle1, particle2)
            t = 0
    canv.update()
    time.sleep(0.001)

