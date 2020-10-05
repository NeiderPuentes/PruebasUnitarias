# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:16:34 2020
@author: Christian Caro - 20181020027
@author: Neider Puentes - 20172020
@author: Santiago Rios - 2018020027
"""
import math

class calculadora:
    def sumar(self, x, y):
        return x+y
    def restar(self, x, y):
        return x-y
    def multilplicar (self, x, y):
        return x*y
    def dividir(self, x, y):
        return x/y
    def elevar (self, x, y):
        return math.pow(x, y)
    def raizCuadrada (self, x):
        return math.sqrt(x)
