#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:59:35 2021

@author: 226sauvage
"""
from math import sqrt
class Poly:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def discriminant(self):
        return self.b**2-(4*(self.a*self.c))
    
    def solution(self):
        delta=self.discriminant()
        if delta<0:
            return "pas de solution"
        elif delta==0:
            return -self.b/2*self.a
        else:
            s_1=(-self.b+sqrt(delta))/2*self.a
            s_2=(-self.b-sqrt(delta))/2*self.a
            return f" s_1= {s_1} et s_2= {s_2}"
        
        
        
        
p=Poly(8,50,8)
p.solution()        