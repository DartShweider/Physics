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
r = 5

class liquid_particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.r = 5
        self.color = 'blue'
        self.ball = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.gravitation = 0.9805
        self.dir = (self.vel_x, self.vel_y)
    def set_coords(self):
        canv.coords(self.ball, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        self.x += +self.vel_x
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

particle1 = liquid_particle(800, 200)
particle2 = liquid_particle(600, 200)
particle2.vel_x = 1
screen1 = canv.create_text(400, 300, text='', font='28')
particles = [particle1, particle2]



while True:
    for x in particles:
        x.move()
    if particle1.x == particle2.x+2*r:
        particle2.vel_x = -particle2.vel_x
    canv.update()
    time.sleep(0.001)

