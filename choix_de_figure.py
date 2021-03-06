#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:51:53 2021

@author: 226sauvage
"""
import turtle

def cube():   
    t=turtle.Turtle()
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(150)
        t.left(90)
    t.goto(50,50)
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(150)
        t.left(90)
    t.goto(150,50)
    t.goto(100,0)
    t.goto(100,150)
    t.goto(150,200)
    t.goto(50,200)
    t.goto(0,150)

def cylindre():
    t=turtle.Turtle()
    height = 100
    radius = 20
    t.forward(height)
    t.circle(radius)
    t.setheading(90)
    t.penup()
    t.forward(2*radius)
    t.pendown()
    t.setheading(180)
    t.forward(height)
    t.circle(radius, extent=180) 
    t.circle(radius, extent=180)  
    t.done()
    
def pyramide():    
    t=turtle.Turtle()
    t.pendown()
    t.speed(0)
    t.pensize(1)
    t.color('grey')
    for i in range(250):
        t.forward(i)
        t.left(120)
        
def choix_defigure():
    choix=input("Veuillez choisir le nom d'une figure parmi cube ,cylindre et cylindre")
    if choix=="cube":
        cube()
    elif choix=="pyramide":
        pyramide()
    elif choix=="cylindre":
        cylindre()
    else:
        print("Choix incorrect")        
