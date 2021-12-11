# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:28:48 2021

@author: Administrador
"""

#Funcion que calcule el máximo de 2 numeros

def NumeroMaximo (numero1, numero2):
    if numero1<numero2:
        return numero2
    if numero2<numero1:
        return numero1
    if numero1==numero2:
        return "son iguales"

num1=12
num2=12
print("El mayor número entre",num1,"y",num2, "es",NumeroMaximo(num1,num2))
    
#Función que calcule el máximo de 3 numeros

def NumeroMaximo2 (nume1, nume2, nume3):
    if (nume1<nume2 and nume3<nume2):
        return nume2
    if (nume2<nume1 and nume3<nume1):
        return nume1
    if (nume1<nume3 and nume2<nume3):
        return nume3
    if (nume1==nume2 and nume2==nume3):
        return "todos son iguales"
    if (nume1==nume2 and nume3<nume2):
        return nume1, "y", nume2
    if (nume3==nume2 and nume1<nume3):
        return nume3, "y", nume2
numer1=13
numer2=12
numer3=11
print("El mayor número entre",numer1,",",numer2,"y",numer3, "es",NumeroMaximo2(numer1,numer2,numer3))

#Función que calcule la longitud de una frase

def LongitudFrase (frase):
    cont=0
    for i in frase:
        cont=cont+1
    return cont

fraseanalizada='Buenos dias'
print("La longitud de la frase",fraseanalizada,"es de",LongitudFrase(fraseanalizada),"caracteres.")

#Función que determine si el caracter introducido es vocal o no
def vocal (letra):
    if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
        return "es vocal"
    else: 
        return "no es vocal"

let='b'
print("La letra",let,vocal(let))

#Función que sume y multiplique los valores de una lista

def suma(numbers):
    sumatot=0
    for z in numbers:
        sumatot=sumatot+z
    return sumatot

numerossuma=[5,6,7]
print("La suma de los numeros",numerossuma,"es",suma(numerossuma))

def multi(numbers2):
    mult=1
    for j in numbers2:
        mult=mult*j
    return mult

print ("La multiplicacion de los numeros",numerossuma,"es",multi(numerossuma))