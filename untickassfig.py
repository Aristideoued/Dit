#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:22:31 2021

@author: 226sauvage
"""
from math import pi
import turtle


class Figure:
    def __init__(self,nom,longueur):
        self.nom=nom
        self.longueur=longueur
        
        
    def perimetre(self):
         if self.nom=="carré":
            return self.longueur*4
         elif self.nom=="rectangle":
            print( (self.longueur+self.longueur*0.5)*2)
         elif self.nom=="cercle":
            return 2*self.longueur*pi
         else:
            return "nom non pris en charge" 
        
        
    def tracer(self):
          t=turtle.Turtle()
          if self.nom=="carré":
                for i in range(4):
                    t.forward(self.longueur)
                    t.right(90)         
          elif self.nom=="rectangle":
                    t.forward(self.longueur)
                    t.right(90)  
                    t.forward(self.longueur*0.5)
                    t.right(90)  
                    t.forward(self.longueur)
                    t.right(90)  
                    t.forward(self.longueur*0.5)
                    t.right(90)  
          elif self.nom=="cercle":
             t.circle(self.longueur) 
             
             
          else:
              return "nom non pris en charge"
          
fig1=Figure("rectangle",50) 
perm=fig1.perimetre() 
print(perm) 


fig1.tracer() 
#fig=Figure("cercle",50)  
#print(fig.perimetre()) 
#fig.tracer()  
#fig2=Figure("carré",50)  
#print(fig2.perimetre()) 
#fig2.tracer()       