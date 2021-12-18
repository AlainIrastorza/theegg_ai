# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:14:57 2021

@author: Administrador
"""

import time
def suma_lineal (n):
    s=1
    sum1=0
    while (s<=n):
        sum1=sum1+s
        s=s+1
    return sum1

def suma_constante (n):
    return (n/2)*(n+1)

cantidad=1000000

for i in range(4):
    t0=time.time()
    suma1=suma_lineal(cantidad)
    t1=time.time()
    suma2=suma_constante(cantidad)
    t2=time.time()
    
    print("SumaLineal: {} - {}".format(suma1,t1-t0))
    print("SumaConstante:{} - {}".format(suma2,t2-t1))
    
    cantidad*=10
    
   