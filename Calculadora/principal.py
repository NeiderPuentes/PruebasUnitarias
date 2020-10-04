# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:22:34 2020

@author: Neider Puentes
"""

from calculadora import calculadora

c = calculadora()

def menu():
    print(" ")
    print ("** Calculadora ** \n")
    print ("Seleccione una opción :") 
    print("1 Sumar")
    print("2 Restar ")
    print("3 multiplicar ")
    print("4 Dividir ")
    print("5 Potencia ")
    print("6 Raiz Cuadrada ")
    print("0 Salir ")
    return int(input("Digita tu opcion "))

while(True):
    opcion = menu()
    if (opcion==0):
        break
    else:
        num1= float(input("Ingresa numero base: "))
        if(opcion!=6):
             num2 = float(input("Ingresa numero Complemento: \n"))
        if(opcion==1):
            print("El resultado de la suma es :")
            print (c.sumar(num1,num2))
        elif(opcion == 2):
            print("El resultado de la resta es :")
            print (c.restar(num1,num2))
        elif(opcion == 3):
            print("El resultado de la multiplicación es :")
            print (c.multilplicar(num1,num2))               
        elif(opcion == 4):
            print("El resultado de la divicion es :")
            print (c.dividir(num1,num2))
        elif(opcion == 5):
            print("El resultado de la potencia es :")
            print (c.elevar(num1,num2))
        elif(opcion == 6):
            print("El resultado de la raiz es :")
            print (c.raizCuadrada(num1))
            