# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:03:26 2021

@author: AlainIrastorza
"""

# ENTRADA DE DATOS: NºVACAS Y PESO PERMITIDO DE CAMIÓN
numvacas=int(input("Escribe el número total de vacas:"))
pesototal=int(input("Escribe el peso total permitido del camión:"))

# INICIALIZACIÓN DE VARIABLES DE PESO Y PRODUCCIÓN DE LECHE DE CADA VACA
pesovaca=[]
pesovaca.append(0)
lechevaca=[]
lechevaca.append(0)

# ENTRADA DE DATOS: PESO Y PRODUCCIÓN POR VACA
print ("Ingrese el peso de cada vaca:", end = "")
pesovaca_all = input().split(" ")
for pesovaca_one in pesovaca_all:
        pesovaca.append(int(pesovaca_one))
print ("Ingrese la producción en litros diaria de cada vaca:", end = "")
lechevaca_all = input().split(" ")
for lechevaca_one in lechevaca_all:
        lechevaca.append(int(lechevaca_one))


# CÁLCULOS DEL VALOR MÁXIMO DE PRODUCCIÓN UTILIZANDO PROGRAMACIÓN DINÁMICA
# Y PRESENTACIÓN DEL RESULTADO
max_lechevaca = [([0]*(pesototal+1)) for i in range(0,numvacas+1)]
for i in range(1,numvacas+1):
        for j in range(1,pesototal+1):
            if(j>=pesovaca[i]):
                max_lechevaca[i][j] = max(max_lechevaca[i-1][j],max_lechevaca[i-1][j-pesovaca[i]]+lechevaca[i])
            else:
                max_lechevaca[i][j] = max_lechevaca[i-1][j]
print ("Cuando el peso permitido en el camión es % d, el valor máximo de producción de leche en litros es:% d"% (pesototal, max_lechevaca [numvacas] [pesototal]))

# CÁLCULO DE LAS VACAS SELECCIONADAS Y PRESENTACIÓN DEL RESULTADO 
item = [0 for i in range(numvacas+2)]
m = numvacas
while m>=1:
        i = m
        if(max_lechevaca[i][pesototal] == max_lechevaca[i-1][pesototal]):
            item[i] = 0
        else:
            item[i] = 1
            pesototal-=pesovaca[i]
        m-=1
print ("Las vacas que se escogen son (1 se coge, 0 no se coge):", end = "")
for i in range(1,numvacas+1):
        print(item[i],end = " ")
