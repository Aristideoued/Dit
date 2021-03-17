#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:11:16 2021

@author: 226sauvage
"""
from time import sleep
class Chanson:
    def __init__(self,paroles):
        self.paroles=paroles
        
    def chanter(self):
        for i in self.paroles:
            print(i)
            sleep(10)
            
            
ch=Chanson(["ajk","vfj","dfjio"])
ch.chanter()            