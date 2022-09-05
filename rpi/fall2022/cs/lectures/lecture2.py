#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:03:31 2022

@author: andrewzeng
"""

def squircle(r):
    pi = 3.14159
    area = pi*r**2
    return area

def squylinder(r, h):
    pi = 3.14159
    area = pi*r**2
    volume = area*h
    return volume

def interdasting(origina, rate, term):
    return origina + (origina * rate * term)

print("area is:", squircle(5))
print("volume is:", squylinder(5, 10))
print("interest after 1 year will be:", interdasting(100,0.05,1))
print("interest after 2 years will be:", interdasting(100,0.05,2))
print("interest after 3 years will be:", interdasting(100,0.05,3))