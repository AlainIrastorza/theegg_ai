# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:03:26 2021

@author: AlainIrastorza
"""

# FUNCIÓN 1: función que calcule el máximo de dos números
def maximo (n1,n2):
    if (n1>=n2):
        return n1
    else:
        return n2
n_max=maximo(5,27)
print ("Función 1:")
print ("  Número máximo: ",n_max)

# FUNCIÓN 2: función que calcule el máximo de tres números
def maximo3 (num1,num2,num3):
    if (num1>=num2) and (num1>=num3):
        return num1
    elif (num2>num1) and (num2>num3):
        return num2
    else:
        return num3
num_max=maximo3(25,187,20)
print ("\nFunción 2:")
print ("  Número máximo: ",num_max)

# FUNCIÓN 3: función que calcule la longitud de una frase
def longfrase(frase):
    return len (frase)
longitud_frase=longfrase("Hola, buenos dias")
print ("\nFunción 3:")
print("  Longitud de la frase: ", longitud_frase)

# FUNCIÓN 4: función que determine si el carácter introducido es vocal o no
def vocal (let):
    if (let=="a") or (let=="e")or (let=="i")or (let=="o")or (let=="u"):
        return "vocal"
    else:
        return "consonante"
letra=vocal("b")
print ("\nFunción 4:")
print("  La letra es: ",letra)
    
# FUNCIÓN 5: función que sume y multiplique los valores de una lista
def oper(lista):
    tam=len(lista)
    cont=0
    suma=0
    multi=1
    while(cont<tam):
        suma+=lista[cont]
        multi*=lista[cont]
        cont+=1
    print("\nFunción 5:")
    print("  Valor de la suma: ",suma)
    print("  Valor de la multiplicación: ",multi)
listado=[1,5,9,7,4]
oper(listado)

# FUNCIÓN 6: función que invierta el orden de una frase
def invertir(phrase):
    return phrase[::-1]
frase="Hola, estamos aqui"
invertida=invertir(frase)
print("\nFunción 6:")
print("  Frase invertida: ", invertida)

# FUNCIÓN 7: función que encuentre palindromos
def palindromo(phrase2):
    if phrase2==phrase2[::-1]:
        return "palindromo"
    else:
        return "no palindromo"
frase2=palindromo("aiaaia")
print("\nFunción 7:")
print("  La frase es: ",frase2)

# FUNCIÓN 8: comparar 2 listas y ver si se repite algún valor
def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return "Si"
    return "No"

repet=superposicion([1,2,3,4],[4,6,7])
print("\nFunción 8:")
print("  ¿Se repite algún valor? ",repet)

# FUNCIÓN 9: función que escriba una letra n veces
def escribir (letra9,num):
    print("\nFunción 9:")
    print(num*letra9)
escribir("a",8)

# FUNCIÓN 10: función que dibuje el histograma de los números que se envian
def histograma (lista):
    print("\nFunción 10:")
    for i in lista:
        print (i * "0")

histograma([4, 9, 7,40,2]) 