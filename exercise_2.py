#Escribir una función que calcule el área de un círculo dado su radio.
import math


def calculaRadio(radio):
    pi = 3.1416
    area = pi * (radio ** 2)
    return area

radio = calculaRadio(int(input("Ingrese el radio del area a calcular:")))
print(radio)