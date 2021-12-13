# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 13:18:15 2021

@author: Administrador
"""

def suma(n1,n2):
    if(type(n1)==int or type(n1)==float)and(type(n2)==int or type(n2)==float):
        n3=n1+n2
        return n3
    else:
        return "Error. No se han introducido dos números."

def resta(n3,n4):
    if(type(n3)==int or type(n3)==float)and(type(n4)==int or type(n4)==float):
        return n3-n4
    else:
        return "Error. No se han introducido dos números."

def producto(n5,n6):
    if(type(n5)==int or type(n5)==float)and(type(n6)==int or type(n6)==float):
        return n5*n6
    else:
        return "Error. No se han introducido dos números."

def division(n7,n8):
    if n8==0:
        return "Error. Número no divisible."
    elif((type(n7)==int or type(n7)==float) 
         and (type(n8)==int or type(n8)==float)):
        return n7/n8
    else:
        return "Error. No se han introducido dos números."


