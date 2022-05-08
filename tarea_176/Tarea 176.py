# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:03:26 2021

@author: AlainIrastorza
"""

# PROGRAMA 1
numero1=1
numero2=2
numero3=3

if (numero1>numero2) and (numero1>numero3):
    numero=numero1
elif ((numero2>numero3) and (numero2>numero1)):
    numero=numero2
else:
    numero=numero3
print("PROGRAMA 1:")
print("El máximo de los tres números es",numero)    


# PROGRAMA 2
longitud=0
frase="Hola, que tal?"

# x=len(frase) CALCULAR LA LONGITUD DE UNA FRASE MEDIANTE UNA FUNCIÓN
while True:
    try:
        frase[longitud]
        longitud+=1
    except IndexError:
        break

print ("\nPROGRAMA 2:")
print ("Longitud de una frase:",longitud)


# PROGRAMA 3
letra="a"

if ((letra=="a") or (letra=="e") or (letra=="i") or (letra=="o") or (letra=="u")):
    print ("\nPROGRAMA 3:")
    print ("La letra es una vocal.")
else:
    print ("\nPROGRAMA 3:")
    print("La letra no es una vocal")
    
    
# PROGRAMA 4
suma=0
cont=0
lista=[1,6,4,6]
longitud_lista=len(lista)
while (cont<longitud_lista):
    suma=suma+lista[cont]
    cont=cont+1
print ("\nPROGRAMA 4:")
print("Sumatorio de los valores de la lista: ",suma) 


# PROGRAMA 5
palabra="alaala"
longitud_palabra=len(palabra)
contador=0
igual=1
while((igual==1) and (contador!=longitud_palabra/2)):
    if (palabra[contador]!=palabra[longitud_palabra-1-contador]):
        igual=0
    contador=contador+1
if igual==1:
    print ("\nPROGRAMA 5:")
    print ("La palabra es palíndroma.")
else:
    print ("\nPROGRAMA 5:")
    print ("La palabra no es palíndroma.")
    
    
# PROGRAMA 6
lista1=[1,2,4,8,6]
lista2=[8,9,6,4,1,7,8]
longitud_lista1=len(lista1)
longitud_lista2=len(lista2)
contador_igual=0
contador6_1=0
contador6_2=0
while(contador6_1<longitud_lista1):
    while(contador6_2<longitud_lista2):
        if (lista1[contador6_1]==lista2[contador6_2]):
            contador_igual=contador_igual+1
        contador6_2=contador6_2+1
    contador6_1=contador6_1+1
    contador6_2=0
print ("\nPROGRAMA 6:")
print ("Número de valores coincidentes: ",contador_igual)