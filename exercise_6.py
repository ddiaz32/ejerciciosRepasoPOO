#Crear un programa que calcule la suma de los números en una lista dada.

def sumaLista(list):
    suma = 0 
    for number in list:
        suma += number 
    return suma 


list=[5,10,15,20,25]

sumaT=sumaLista(list)

print("\33[1m"+"La suma total es:"+ "\033[0m",sumaT)
    