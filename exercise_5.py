#Crear una función que convierta grados Fahrenheit a grados Celsius. 

def fahrenheit_a_celsius(grados_f):
    grados_c = (grados_f - 32) * 5/9
    return grados_c

grados_c = fahrenheit_a_celsius(32)
print("32 grados Fahrenheit son ", grados_c, " grados Celsius.")

