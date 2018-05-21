#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing
import timeit


from tkinter import *
import math

# print (dir(math))

import time

root = Tk()

fr = Frame(root)

root.geometry('1280x728')

canv = Canvas(root, bg='white')

canv.pack(fill=BOTH, expand=1)

def cooling_chamber():

    canv.create_rectangle(650, 450, 800, 600, width = 7)

def compressor():

    canv.create_rectangle(650, 400, 800, 450, width = 7, fill = "#05f")

def pipeline():

    canv.create_line(800, 400, 800, 300, width = 7)

    canv.create_line(800, 300, 650, 200, width = 7)

    canv.create_line(650, 400, 650, 300, width = 7)

    canv.create_line(550, 300, 650, 300, width = 7)

    canv.create_line(550, 200, 650, 200, width = 7)

    canv.create_line(550, 200, 400, 300, width = 7)

def heat_exchanger():

    canv.create_line(550, 300, 450, 320, width = 7) #heat_exchnger_1#

    canv.create_line(450, 320, 550, 340, width = 7) #heat_exchnger_2#

    canv.create_line(400, 340, 500, 360, width = 7) #heat_exchnger_3#

    canv.create_line(500, 360, 400, 380, width = 7) #heat_exchnger_4#

    canv.create_line(550, 380, 450, 400, width = 7) #heat_exchnger_5#

    canv.create_line(450, 400, 650, 450, width= 7)  #heat_exchnger_6#

    canv.create_line(400, 425, 650, 485, width= 7)  #out_pipeline_exchnger_1#

    canv.create_line(550, 300, 550, 425, width= 7)

    canv.create_line(400, 300, 400, 425, width= 7)

    canv.create_polygon(550 , 300 , 450 , 320 , 550 , 340, fill = "#f50")

    canv.create_polygon(400, 340, 500, 360, 400, 380, fill="#f50")

    canv.create_polygon(550, 380, 450, 400, 550, 425, fill="#f50")

canv.create_rectangle(400, 425, 650, 485, width = 1)

Thermal_system_window = (400, 200, 800, 600)


class freon_particle():

    def __init__(self, x, y):

        self.x = x

        self.y = y

        self.detect = 0

        self.velx = 0

        self.vely = 0

        self.r = 3

        self.position_x = set()

        self.position_y = set()

        self.main_position = 'cooling_chamber'

        self.color = 'blue'

        self.ball = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)

        self.gravitation = 0.02

        self.f = 0

        self.accel = 0

        self.type = 'liquid'

    def set_coords(self):

        canv.coords(self.ball, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):

        if self.x < 800 and self.x>650 and self.y > 450 and self.y <600:

            self.main_position = 'cooling_chamber'

        elif self.x<800 and self.x>650 and self.y<450 and self.y>400:

            self.main_position = 'compressor'

        elif self.x<800 and self.x>650 and self.y <499 and self.y >300:

            self.main_position = 'pipeline_1'

        elif self.x<800 and self.x>650 and self.y <300 and self.y >200:

            self.main_position = 'pipeline_2'

        elif self.x < 650 and self.x > 550 and self.y < 300 and self.y >200:

            self.main_position = 'pipeline_3'

        elif self.x > 400 and self.x < 550 and self.y > 200 and self.y <300:

            self.main_position = 'pipeline_4'

        elif self.x > 400 and self.x < 550 and self.y > 300 and self.y < 320:

            self.main_position = 'heat_exchanger_1'

        elif self.x > 400 and self.x < 550 and self.y > 320 and self.y < 340:

            self.main_position = 'heat_exchanger_2'

        elif self.x > 400 and self.x < 550 and self.y > 340 and self.y < 360:

            self.main_position = 'heat_exchanger_3'

        elif self.x > 400 and self.x < 550 and self.y > 360 and self.y < 380:

            self.main_position = 'heat_exchanger_4'

        elif self.x > 400 and self.x < 550 and self.y > 380 and self.y < 400:

            self.main_position = 'heat_exchanger_5'

        elif self.x > 400 and self.x < 550 and self.y > 400 and self.y < 420:

            self.main_position = 'heat_exchanger_6'

        elif self.x > 400 and self.x < 650 and self.y > 425 and self.y < 485:

            self.main_position = 'pipeline_5'


        self.vely  += self.gravitation

        self.y += self.vely

        self.x += self.velx

        self.set_coords()

        if self.main_position == 'cooling_chamber':

            if self.y > 550:

                self.gravitation = 0
            else:
                self.gravitation = 0.02

            if self.x >= 800:

                self.velx = -abs(self.velx)

            if self.y >= 600:

                self.vely = -abs(self.vely)

            if self.x <= 650:

                self.velx = abs(self.velx)

        if self.main_position == 'compressor':

            self.vely = -3

            if self.x <= 650:

                self.velx = abs(self.velx)

            if self.x >= 800:

                self.velx = -abs(self.velx)

        if self.main_position == 'pipeline_1':

            if self.x <= 650:

                self.velx = abs(self.velx)

            if self.x >= 800:

                self.velx = -abs(self.velx)

        if self.main_position == 'pipeline_2':

            self.velx -= self.accel

            cos_alpha = cos_angle(vector(150, 100), vector(self.velx, self.vely))

            sin_alpha = math.sqrt(1-cos_alpha**2)

            el_vector = len_norm_v(vector(self.velx, self.vely), vector(150, 100))

            dist = (self.x*(2/3) - self.y -233)/(math.sqrt((2/3)**2 + 1))

            if dist<0:

                self.f = 0

            if dist>0 and self.f == 0:

                self.f = 1

                if cos_alpha >0:

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                else:

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

        if self.main_position == 'pipeline_3':

            self.velx -= self.accel

            if self.y <= 200:

                self.vely = abs(self.vely)

            if self.y >= 300:

                self.vely = -abs(self.vely)

        if self.main_position == 'pipeline_4':

            self.velx -= self.accel

            cos_alpha = cos_angle(vector(150, -100), vector(self.velx, self.vely))

            sin_alpha = math.sqrt(1-cos_alpha**2)

            el_vector = len_norm_v(vector(self.velx, self.vely), vector(150, -100))

            dist = (self.x*(-2/3) - self.y +566.6666)/(math.sqrt((2/3)**2 + 1))

            if dist<0:

                self.f = 0

            if dist>0 and self.f == 0:

                self.f = 1

                if cos_alpha >0:

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                else:

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

        if self.main_position == 'heat_exchanger_1':

            self.velx -= self.accel

            if self.x < 400:

                self.velx = abs(self.velx)

            cos_alpha = cos_angle(vector(100, -20), vector(self.velx, self.vely))

            sin_alpha = math.sqrt(1 - cos_alpha ** 2)

            el_vector = len_norm_v(vector(self.velx, self.vely), vector(100, -20))

            dist = (self.x * (-1/ 5) - self.y + 410) / (math.sqrt((-1 / 5) ** 2 + 1))

            if dist > 0:
                self.f = 0

            if dist < 0 and self.f == 0:

                self.f = 1

                if cos_alpha > 0:

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                else:

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

        if self.main_position == 'heat_exchanger_2':

            self.velx += self.accel

            if self.x < 400:

                self.velx = abs(self.velx)

            cos_alpha = cos_angle(vector(100, 20), vector(self.velx, self.vely))

            sin_alpha = math.sqrt(1 - cos_alpha ** 2)

            el_vector = len_norm_v(vector(self.velx, self.vely), vector(100, 20))



            dist = (self.x * (1 / 5) - self.y + 230) / (math.sqrt((1 / 5) ** 2 + 1))

            if dist < 0:
                self.f = 0

            if dist > 0 and self.f == 0:

                self.f = 1

                if cos_alpha > 0:

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                else:

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely



        if self.main_position == 'heat_exchanger_3':

            self.velx += self.accel

            if self.x < 400:

                self.velx = abs(self.velx)

            cos_alpha = cos_angle(vector(100, 20), vector(self.velx, self.vely))

            sin_alpha = math.sqrt(1 - cos_alpha ** 2)

            el_vector = len_norm_v(vector(self.velx, self.vely), vector(100, 20))



            dist = (self.x * (1 / 5) - self.y + 260) / (math.sqrt((1 / 5) ** 2 + 1))

            if dist > 0:
                self.f = 0

            if dist < 0 and self.f == 0:

                self.f = 1

                if cos_alpha > 0:

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                else:

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

        if self.main_position == 'heat_exchanger_4':

            self.velx -= self.accel

            if self.x > 550:

                self.velx = -abs(self.velx)

            cos_alpha = cos_angle(vector(100, -20), vector(self.velx, self.vely))

            sin_alpha = math.sqrt(1 - cos_alpha ** 2)

            el_vector = len_norm_v(vector(self.velx, self.vely), vector(100, -20))



            dist = (self.x * (-1 / 5) - self.y + 460) / (math.sqrt((1 / 5) ** 2 + 1))

            if dist < 0:
                self.f = 0

            if dist > 0 and self.f == 0:

                self.f = 1

                if cos_alpha > 0:

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                else:

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

        if self.main_position == 'heat_exchanger_5':

            self.velx -= self.accel

            if self.x < 400:

                self.velx = abs(self.velx)

            cos_alpha = cos_angle(vector(100, -20), vector(self.velx, self.vely))

            sin_alpha = math.sqrt(1 - cos_alpha ** 2)

            el_vector = len_norm_v(vector(self.velx, self.vely), vector(100, -20))



            dist = (self.x * (-1 / 5) - self.y + 490) / (math.sqrt((1 / 5) ** 2 + 1))

            if dist > 0:
                self.f = 0

            if dist < 0 and self.f == 0:

                self.f = 1

                if cos_alpha > 0:

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                else:

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

        if self.main_position == 'heat_exchanger_6':

            self.velx += self.accel

            if self.x < 400:

                self.velx = abs(self.velx)

            cos_alpha = cos_angle(vector(100, 20), vector(self.velx, self.vely))

            sin_alpha = math.sqrt(1 - cos_alpha ** 2)

            el_vector = len_norm_v(vector(self.velx, self.vely), vector(100, 20))



            dist = (self.x * (1 / 4) - self.y + 287.5) / (math.sqrt((1 / 4) ** 2 + 1))

            if dist < 0:
                self.f = 0

            if dist > 0 and self.f == 0:

                self.f = 1

                if cos_alpha > 0:

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                else:

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

        if self.main_position == 'pipeline_5':

            self.velx += self.accel

            cos_alpha = cos_angle(vector(100, 20), vector(self.velx, self.vely))

            sin_alpha = math.sqrt(1 - cos_alpha ** 2)

            el_vector = len_norm_v(vector(self.velx, self.vely), vector(100, 20))

            dist_1 = (self.x * 0.24 - self.y + 329) / (math.sqrt(0.24 ** 2 + 1))

            dist_2 = (self.x * (1 / 4) - self.y + 287.5) / (math.sqrt((1 / 4) ** 2 + 1))

            if dist_1 and -dist_2 > 0:

                self.f = 0

            if (dist_1 < 0 and self.f == 0) or (dist_2 > 0 and self.f == 0):

                self.f = 1

                if cos_alpha > 0:

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                else:

                    self.velx += sin_alpha * el_vector.velx

                    self.vely += sin_alpha * el_vector.vely

                    self.velx, self.vely = -self.velx, -self.vely

                    self.velx -= sin_alpha * el_vector.velx

                    self.vely -= sin_alpha * el_vector.vely

        if self.type == 'gas':

            self.gravitation = -0.03


class centre_mass():

    def __init__(self,velx, vely):

        self.velx = velx

        self.vely = vely



class vector():

    def __init__(self, x, y):

        self.velx = x

        self.vely = y

        self.x = 1

        self.y = -1

def posx(part):

    return part.x

def posy(part):

    return part.y

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



def particles_sort(parts):

    parts.sort(key = posx)

    for k in range(1, 420//(2*particle1.r)):

        for i in range(len(parts)):

            if abs(parts[i].x - 2*particle1.r * k - 400) < 2*particle1.r:

                parts[i].position_x.add(k)

    for k in range(1, 420//(2*particle1.r)):

        for i in range(len(parts)):

            if abs(parts[i].y - 2*particle1.r * k - 200) < 2*particle1.r:

                parts[i].position_y.add(k)

particle1 = freon_particle(690, 580)

particle2 = freon_particle(670, 580)

particle2.velx = 1

particle2.vely = 3

particle1.velx = 7

particle1.vely = 2

particles = [particle1, particle2]

for j in range(14):

    for i in range(10):

        particles.append(freon_particle(665+i*10, 8*j+465))


particles[11].velx  = particles[11].vely = -2

particles[15].velx  = particles[15].vely = 1

particles[18].velx  = particles[18].vely = 3

opportunity = [[0]*len(particles)]*len(particles)

for i in range(len(particles)):

    for j in range(i+1,len(particles)):

        if distance(particles[i], particles[j])<2*particle1.r:

            opportunity[i][j] = 0

        if distance(particles[i], particles[j])>=2*particle1.r:

            opportunity[i][j] = 1



def moving(freon):

    for a in range(len(freon)):

        freon[a].move()

    for i in range(len(freon)):

        for j in range(i+1, len(freon)):

                        m = freon[i]

                        n = freon[j]

                        if len(m.position_x.intersection(n.position_x))>0 :

                            if distance(m , n) >= 2*particle1.r:

                                opportunity[i][j] = 1

                            if distance(m , n) < 2*particle1.r and distance(m , n)>0:

                                if opportunity[i][j] == 1:

                                    collision(m, n)

                                    opportunity[i][j] = 0
                        
    freon.sort(key = posy)

    k = 0

    i = 0

    while k<2 and i < len(freon) - 1:

        if freon[i].main_position == 'cooling chamber':

            if freon[i].type == 'liquid':

                freon[i].type = 'gas'

                k += 1

            else:

                k+=1

        i += 1



cooling_chamber()

compressor()

pipeline()

heat_exchanger()

while True:

    particles_sort(particles)

    divided_parts = [particles[:len(particles)//7], particles[len(particles)//7:2*len(particles)//7], particles[2*len(particles)//7:3*len(particles)//7], particles[3*len(particles)//7:4*len(particles)//7], particles[4*len(particles)//7:5*len(particles)//7], particles[5*len(particles)//7:6*len(particles)//7], particles[6*len(particles)//7:len(particles)]]

    for i in range(len(divided_parts)):

        moving(divided_parts[i])

    canv.update()

    time.sleep(0.00000000001)

