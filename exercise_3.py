#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random

list=[]
n = int(input("Ingrese el numero de numeros aleatorios que desea: "))
for i in range (n):
    list.append(random.randint(0,100))

print(list)