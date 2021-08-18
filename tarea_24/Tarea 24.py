# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:57:02 2021

@author: AlainIrastorza
"""
def main():
    x=VALORDECIMAL()
    y=NUMERODIGITOS(x)
    NUMEROBINARIO(y,x)
    
def VALORDECIMAL():
    #PEDIR VALOR DECIMAL
    print ("Escriba un valor decimal:")
    numero = float(input())

    while numero<0 or numero!=int(numero):
        print ("ERROR. Escriba un valor decimal:")
        numero = float(input())
    return numero

def NUMERODIGITOS(numero):
    #CÁLCULO NÚMERO DE DIGITOS DEL VALOR EN BINARIO
    exponente=0
    while 2**exponente<numero:
        exponente=exponente+1
    exponent=exponente
    return exponent

def NUMEROBINARIO (exponent, numero):
    #CÁLCULO NÚMERO EN BINARIO Y PRESENTACIÓN DE RESULTADO
    binari=[]

    while (exponent>=0):

        if 2**exponent <= numero:
            numero=numero-2**exponent
            binari.append(1)
            exponent=exponent-1
   
        else:
            binari.append(0)
            exponent=exponent-1
      
    print ("\nSu valor binario es ",binari)
    return binari

main()