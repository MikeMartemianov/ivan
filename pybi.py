import kivy
import pygame
import time
import math
import turtle
import ursina
kivy = kivy
pygame = pygame
time = time
math = math
turtle = turtle
ursina = ursina
def mult(list1, list2):
    l = []
    for n in range(len(list1)):
        l.append(list1[n - 1] * list2[n - 1])
    return l
def sum(list1, list2):
    l = []
    for n in range(len(list1)):
        l.append(list1[n - 1] + list2[n - 1])
    return l
def diff(list1, list2):
    l = []
    for n in range(len(list1)):
        l.append(list1[n - 1] - list2[n - 1])
    return l
def divi(list1, list2):
    l = []
    for n in range(len(list1)):
        l.append(list1[n - 1] / list2[n - 1])
    return l
class pen:
    def __init__(self):
        self.pen = turtle.Pen()
    def forward(self, pic):
        self.pen.forward(pic)
    def run(self):
        while True:
            pass
