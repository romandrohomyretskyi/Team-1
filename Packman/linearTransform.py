from numpy import array
from math import cos,sin


def rotateXOY(angle):
    return array([[cos(angle),sin(angle),0,0,0],
                  [-sin(angle),cos(angle),0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,0],
                  [0,0,0,0,1]])

def rotateXOZ(angle):
    return array([[cos(angle),0,sin(angle),0,0],
                  [0,1,0,0,0],
                  [-sin(angle),0,cos(angle),0,0],
                  [0,0,0,1,0],
                  [0,0,0,0,1]])

def rotateYOZ(angle):
    return array([[1,0,0,0,0],
                  [0,cos(angle),sin(angle),0,0],
                  [0,-sin(angle),cos(angle),0,0],
                  [0,0,0,1,0],
                  [0,0,0,0,1]])

def rotateXOW(angle):
    return array([[cos(angle),0,0,sin(angle),0],
                  [0,1,0,0,0],
                  [0,0,1,0,0],
                  [-sin(angle),0,0,cos(angle),0],
                  [0,0,0,0,1]])

def rotateYOW(angle):
    return array([[1,0,0,0,0],
                  [0,cos(angle),0,sin(angle),0],
                  [0,0,1,0,0],
                  [0,-sin(angle),0,cos(angle),0],
                  [0,0,0,0,1]])

def rotateZOW(angle):
    return array([[1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,cos(angle),sin(angle),0],
                  [0,0,-sin(angle),cos(angle),0],
                  [0,0,0,0,1]])

def translate(x,y,z,w):
    return array([[1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,0],
                  [x,y,z,w,1]])

