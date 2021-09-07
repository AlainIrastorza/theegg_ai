# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:03:26 2021

@author: AlainIrastorza
"""

# ENTRADA DE DATOS: NºVACAS Y PESO PERMITIDO DE CAMIÓN
pesototal=int(input("Escribe el peso total permitido del camión:"))

# INICIALIZACIÓN DE VARIABLES DE PESO Y PRODUCCIÓN DE LECHE DE CADA VACA
pesovaca=[0]
lechevaca=[0]

# ENTRADA DE DATOS: PESO Y PRODUCCIÓN POR VACA
repeat = True
while repeat:
        print ("Ingrese el peso de cada vaca separado por espacios:", end = "")
        pesovaca_all = input().split(" ")
        print("A continuación se muestran los pesos introducidos. Si son correctos introduzca una 'y' y pulse enter, en caso contrario introduzca cualquier otra cosa.")
        print(pesovaca_all)
        try:
                pesovaca = [int(element) for element in pesovaca_all]
                repeat = input().lowercase() != 'y'
        except:
                print("Los números introducidos no son correctos, repítalos por favor.")
                repeat = True

numvacas=len(pesovaca_all)

repeat = True
while repeat:
        print ("Ingrese la producción en litros diaria de cada vaca:", end = "")
        lechevaca_all = input().split(" ")
        print("A continuación se muestran las producciones introducidas. Si son correctas introduzca una 'y' y pulse enter, en caso contrario introduzca cualquier otra cosa.")
        print(lechevaca_all)
        repeat = input().lowercase() == 'y'
        try:
                lechevaca = [int(element) for element in lechevaca_all]
                repeat = input().lowercase() != 'y'
        except:
                print("Los números introducidos no son correctos, repítalos por favor.")
                repeat = True

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
while numvacas>=1:
        i = numvacas
        if(max_lechevaca[i][pesototal] == max_lechevaca[i-1][pesototal]):
            item[i] = 0
        else:
            item[i] = 1
            pesototal-=pesovaca[i]
        numvacas-=1
print ("Las vacas que se escogen son (1 se coge, 0 no se coge):", end = "")
for i in range(1,numvacas+1):
        print(item[i],end = " ")
