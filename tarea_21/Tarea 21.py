# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:12:21 2021

@author: Administrador
"""

#Se pide que se introduzca un número entre 0.0001 y 0.9999 y con no 
#más de 4 cifras decimales. 
#Si no cumple esta condición se vuelve a pedir otro número.
#El valor inicial de 10 de numero es para que se de entrada al while.
numero=10

while numero>=0.9999 or numero<=0.0001 or (numero*10000)!=int(numero*10000):
    print("Escriba un número entre 0.0001 y 0.9999 y no más de 4 decimales:")
    numero = float(input())

#Zenbak es numerador e izend denominador. 
#Son multiplicados por 10.000 para convertirlos en números enteros. 
zenbak=numero*10000
izend=10000

#i es el número divisor utilizado en el cálculo de la fracción irreducible. 
i=2

#Se calcula la fracción irreducible.
while i<=9999:
    while zenbak/i==int(zenbak/i) and izend/i==int(izend/i):
        zenbak=zenbak/i
        izend=izend/i
    i=i+1

#Se presenta el resultado.
print("Su fracción irreducible es: ",zenbak, "/" ,izend)