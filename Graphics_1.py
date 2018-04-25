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
        self.detect = 0
        self.velx = 0
        self.vely = 0
        self.r = 10

        self.color = 'blue'
        self.ball = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.gravitation = 0.9805




    def set_coords(self):
        canv.coords(self.ball, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):

        self.x += self.velx
        self.y += self.vely
        self.set_coords()

        if self.x >= 1280:
            self.velx = -self.velx
        if self.y >= 700:
            self.vely = -self.vely
        if self.x <= 0:
            self.velx = -self.velx
        if self.y <= 0:
            self.vely = -self.vely

class centre_mass():
    def __init__(self,velx, vely):

        self.velx = velx
        self.vely = vely



class vector():
    def __init__(self, x, y):
        self.velx = x
        self.vely = y




def distance(ball_1, ball_2):
    return math.sqrt((ball_1.x-ball_2.x)**2+(ball_1.y-ball_2.y)**2)

def centre_vect(ball_1, ball_2):
    return vector(ball_1.x-ball_2.x, ball_1.y-ball_2.y)

def cos_angle(vect_1, vect_2):
    return (vect_1.velx*vect_2.velx + vect_2.vely*vect_1.vely)/((math.sqrt((vect_1.velx)**2 + (vect_1.vely)**2))*(math.sqrt((vect_2.velx)**2 + (vect_2.vely)**2)))

def norm_vect(vectorl):

    return vector(-vectorl.vely, vectorl.velx)

def len_norm_v(vector1, norm_vectorn):
    n = abs(cos_angle(vector1, norm_vectorn))*(math.sqrt(vector1.velx**2 + vector1.vely**2)/(math.sqrt(norm_vectorn.velx**2 + norm_vectorn.vely**2)))


    return vector(norm_vectorn.velx * n, norm_vectorn.vely * n)

def energy(d):
    t = 0
    for i in range(len(d)):
        t+= (d[i].velx**2 + d[i].vely**2)
    return t


def collision(ball_1 , ball_2):



    CM = centre_mass((ball_1.velx+ball_2.velx)/2, (ball_1.vely+ball_2.vely)/2)

    ball_1.velx -= CM.velx

    ball_2.velx -= CM.velx

    ball_1.vely -= CM.vely

    ball_2.vely -= CM.vely

    centre_vector = centre_vect(ball_1, ball_2)

    cent_vector1 = len_norm_v(ball_1, centre_vector)

    cent_vector2 = len_norm_v(ball_2, centre_vector)

    cos_a1 = cos_angle(ball_1, centre_vector)

    cos_a2 = cos_angle(ball_2, centre_vector)

    if abs(cos_a1) == 1:
        ball_1.velx, ball_2.velx = ball_2.velx, ball_1.velx
        ball_1.vely, ball_2.vely = ball_2.vely, ball_1.vely
        return
    else:

        if cos_a1>0:



            t1x = -cent_vector1.velx
            t1y = -cent_vector1.vely


            ball_1.velx += 2*t1x

            ball_1.vely += 2*t1y
        elif cos_a1<0:

            t1x = cent_vector1.velx
            t1y = cent_vector1.vely


            ball_1.velx += 2*t1x

            ball_1.vely += 2*t1y

        if cos_a2>0:



            t2x = -cent_vector2.velx
            t2y = -cent_vector2.vely


            ball_2.velx += 2*t2x

            ball_2.vely += 2*t2y
        elif cos_a2<0:

            t2x = cent_vector2.velx
            t2y = cent_vector2.vely


            ball_2.velx +=2*t2x

            ball_2.vely += 2*t2y



    ball_1.velx += CM.velx

    ball_2.velx += CM.velx

    ball_1.vely += CM.vely

    ball_2.vely += CM.vely

    return
























particle1 = liquid_particle(1000, 195)
particle2 = liquid_particle(200, 200)


particle2.velx = 20
particle2.vely = 0

particle1.velx = -15
particle1.vely = 0
particles = [particle1, particle2]
for i in range(35):
    particles.append(liquid_particle(100+i*25, 300))
for i in range(35):
    particles.append(liquid_particle(100+i*25, 350))
for i in range(35):
    particles.append(liquid_particle(100+i*25, 400))

while True:

    for x in particles:
        x.move()
    for i in range(len(particles)):
        for j in range(len(particles)):
            if j>i:
                m = particles[i]
                n = particles[j]


                if distance(m , n) > 20:
                    m.detect = 0
                    n.detect = 0
                if distance(m , n) < 20:
                    if m.detect ==0 and n.detect == 0:

                        collision(m, n)

                        m.detect = 1
                        n.detect = 1

    canv.update()
    time.sleep(0.0000001)

