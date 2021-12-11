# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:18:37 2021

@author: Administrador
"""

    
        
    
#1.- Realiza un programa que lea 2 números por teclado 

def numeroteclado1(numero1,numero2):
    if numero1==numero2:
        return "los dos números son iguales"
    else:
        return "los dos números son diferentes"

def numeroteclado2 (number1,number2):
    if number1>number2:
        return " y el primero es mayor que el segundo"
    else:
        return " y el segundo es mayor o igual que el primero"

num1=float(input("1.- Escriba un numero:"))
num2=float(input("Escriba otro número:"))
print("\nSe concluye lo siguiente: \n",numeroteclado1(num1,num2))
print(numeroteclado2(num1,num2))

#2.- Cadena de texto introducida por el usuario

def LongitudFrase (frase):
    cont=0
    for i in frase:
        cont=cont+1
    if cont<5:
        return "La cadena de texto tiene una longitud < a 5"
    elif cont <10:
        return "La cadena de texto tiene una longitud >=5 y <10"
    else:
        return "La cadena de texto tiene una longitud >=10"
    
texto=input("2.- Escriba una frase:")
print(LongitudFrase(texto))

#3.- Multiplicación de número introducido

numero=float(input("3.- Escriba un numero entre 0 y 99:"))

while numero<=0 or numero>=99:
    numero=float(input("Vuelva a escribir un número. Debe ser entre 0 y 99:"))
print ("A continuación se presenta la tabla multiplicando el valor")
print("introducido por valores entre 1 y 10:")    

i=1
mult=1
while (i<=10):
    mult=numero*i
    print(numero,"multiplicado por",i,"es",mult)
    i=i+1

#4.- Media entre tres numeros 

numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3)/ 3
print("\n4.-La nota media es", media)    

#5.- Lectura de número impar

impar=int(input("5.-Escriba un número impar:"))
n=0
while (n==0):
    if impar % 2 == 0:
        impar=int(input("Error. Vuelve a escribir un número impar:"))
    
    else:
        print("Correcto, número impar introducido.")
        n=1

#6.- Suma de todos números enteros impares desde el 0 hasta el 115  
   
j=1
sumaimpar=0
while j<=115:
    sumaimpar=sumaimpar+j
    j=j+2
print("\n6.- La suma de todos los numeros enteros impares desde 0 hasta 115")
print ("es:",sumaimpar)