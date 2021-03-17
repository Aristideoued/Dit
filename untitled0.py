#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:51:37 2021

@author: 226sauvage
"""
import turtle
t=turtle.Turtle()

nb_carre=5
i=0
cote=10
while i< nb_carre-1:
    for i in range(4):
        t.forward(cote)
        t.left(90)
    cote+=cote
    t.goto(cote,0)
    i+=1