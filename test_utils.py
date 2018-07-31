#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def nop():
    pass

def move(x, y, step, angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx, ny
    
def cabs(x):
    if not isinstance(int, float):
        raise TypeError('bad operand type')
    if x>=0:
        return x 
    else:
        return -x
