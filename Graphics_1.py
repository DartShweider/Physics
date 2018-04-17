#!/usr/bin/python3
# -*- coding: utf-8 -*-


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
        self.vel = 1
        self.dir = (1, 1)
        self.r = 20
        self.koeff = 1
        self.color = 'blue'
        self.ball = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.gravitation = 0.9805

    def velo(self):
        self.koeff = self.vel / (math.sqrt(self.dir[0] ** 2 + self.dir[1] ** 2))
        self.vel_x = self.koeff * self.dir[0]
        self.vel_y = self.koeff * self.dir[1]

    def set_coords(self):
        canv.coords(self.ball, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        self.velo()
        self.x += self.vel_x
        self.y += self.vel_y
        self.set_coords()

        if self.x >= 1280:
            self.dir = (-self.dir[0], self.dir[1])
        if self.y >= 700:
            self.dir = (self.dir[0], -self.dir[1])
        if self.x <= 0:
            self.dir = (-self.dir[0], self.dir[1])
        if self.y <= 0:
            self.dir = (self.dir[0], -self.dir[1])

class vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = (self.x, self.y)



def distance(ball_1, ball_2):
    return math.sqrt((ball_1.x-ball_2.x)**2+(ball_1.y-ball_2.y)**2)

def centre_vect(ball_1, ball_2):
    return vector(ball_1.x-ball_2.x, ball_1.y-ball_2.y)

def cos_angle(vect_1, vect_2):
    return (vect_1.dir[0]*vect_2.dir[0] + vect_2.dir[1]*vect_1.dir[1])/((math.sqrt((vect_1.dir[0])**2 + (vect_1.dir[1])**2))*(math.sqrt((vect_2.dir[0])**2 + (vect_2.dir[1])**2)))

def norm_vect(vectorl):

    return vector(-vectorl.dir[1], vectorl.dir[0])

def len_norm_v(vector1, norm_vector):
    n = abs(cos_angle(vector1, norm_vector))*(math.sqrt(vector1.dir[0]**2 + vector1.dir[1]**2)/(math.sqrt(norm_vector.dir[0]**2 + norm_vector.dir[1]**2)))


    return vector(norm_vector.dir[0] * n, norm_vector.dir[1] * n)




def collision(ball_1 , ball_2):

    centre_vector = centre_vect(ball_1 , ball_2)

    norm_vector = norm_vect(centre_vector)

    norm_vector1 = len_norm_v(ball_1, norm_vector)

    norm_vector2 = len_norm_v(ball_2, norm_vector)

    cos_a1 = cos_angle(ball_1, norm_vector)

    cos_a2 = cos_angle(ball_2, norm_vector)

    if cos_a1 == 0 and cos_a2 == 0:
        if ball_1.dir[0]*ball_2.dir[0]>=0 and ball_1.dir[1]*ball_2.dir[1]>=0:

            ball_1.vel, ball_2.vel = ball_2.vel, ball_1.vel

            return
        if (ball_1.dir[0]*ball_2.dir[0]>=0 and ball_1.dir[1]*ball_2.dir[1]<=0) or (ball_1.dir[0]*ball_2.dir[0]<=0 and ball_1.dir[1]*ball_2.dir[1]>=0):

            ball_1.dir , ball_2.dir = (ball_2.dir[0], ball_2.dir[1]), (ball_1.dir[0], ball_1.dir[1])

            ball_1.vel, ball_2.vel = ball_2.vel, ball_1.vel

            return


    if cos_a1>0 and cos_a2<0:
        t1x = norm_vector1.dir[0]
        t1y = norm_vector1.dir[1]
        minus_vect1 = vector(-ball_1.dir[0] + t1x, -ball_1.dir[1] + t1y)


        ball_1.dir = (minus_vect1.dir[0] + t1x, minus_vect1.dir[1] + t1y)


        t2x = -norm_vector2.dir[0]
        t2y = -norm_vector2.dir[1]
        minus_vect2 = vector(-ball_2.dir[0] +t2x, -ball_2.dir[1] -t2y)



        ball_2.dir = (minus_vect2.dir[0] + t2x, minus_vect2.dir[1] + t2y )

        ball_1.vel, ball_2.vel = ball_2.vel, ball_1.vel

        return


    elif cos_a2>0 and cos_a1<0:
        t1x = norm_vector1.dir[0]
        t1y = norm_vector1.dir[1]
        minus_vect1 = vector(-ball_1.dir[0] - t1x, -ball_1.dir[1] - t1y)


        ball_1.dir = (minus_vect1.dir[0] - t1x, minus_vect1.dir[1] - t1y)


        t2x = norm_vector2.dir[0]
        t2y = norm_vector2.dir[1]
        minus_vect2 = vector(-ball_2.dir[0] + t2x, -ball_2.dir[1] + t2y)



        ball_2.dir = (minus_vect2.dir[0] + t2x, minus_vect2.dir[1] + t2y)

        ball_1.vel, ball_2.vel = ball_2.vel, ball_1.vel

        return
    elif cos_a1*cos_a2>0:

        t1x = -ball_1.dir[0]
        t1y = -ball_1.dir[1]
        minus_vect1 = vector(t1x + norm_vector1.dir[0], t1y + norm_vector1.dir[1])
        ball_1.dir = ((minus_vect1.dir[0] + norm_vector1.dir[0]), -(minus_vect1.dir[1] + norm_vector1.dir[1]))

        t2x = -ball_2.dir[0]
        t2y = -ball_2.dir[1]
        minus_vect2 = vector(t2x + norm_vector2.dir[0], t2y + norm_vector2.dir[1])
        ball_2.dir = ((minus_vect2.dir[0] + norm_vector2.dir[0]), -(minus_vect2.dir[1] + norm_vector2.dir[1]))

        ball_1.vel, ball_2.vel = ball_2.vel, ball_1.vel

        return

    elif cos_a1 * cos_a2 < 0:

        t1x = ball_1.dir[0]
        t1y = ball_1.dir[1]
        minus_vect1 = vector(t1x - norm_vector1.dir[0], t1y - norm_vector1.dir[1])
        ball_1.dir = ((minus_vect1.dir[0] + norm_vector1.dir[0]), (minus_vect1.dir[1] + norm_vector1.dir[1]))

        t2x = ball_2.dir[0]
        t2y = ball_2.dir[1]
        minus_vect2 = vector(t2x - norm_vector2.dir[0], t2y - norm_vector2.dir[1])
        ball_2.dir = ((minus_vect2.dir[0] + norm_vector2.dir[0]), (minus_vect2.dir[1] + norm_vector2.dir[1]))

        ball_1.vel, ball_2.vel = ball_2.vel, ball_1.vel

        return
    return

particle1 = liquid_particle(200, 100)
particle2 = liquid_particle(1000, 100)

particle2.vel = 1
particle2.dir = (-4,0)
particle1.vel = 1
particle1.dir = (4,0)
particles = [particle1, particle2]
print( particle2.koeff)
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
            print(particle1.dir)
    canv.update()
    time.sleep(0.001)

