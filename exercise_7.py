#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
import random 

def searchMaxNumber(n):
    list=[]
    for i in range(n):
        list.append(random.randint(0,100))
    print(list)
    print(max(list))

n=searchMaxNumber(int(input("Ingrese el numero de elementos que desea en la lista,siguiente se Mostrara el numero mayor de la lista aleatoria generada:")))








