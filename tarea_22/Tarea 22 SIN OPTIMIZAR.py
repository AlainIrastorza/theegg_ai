# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:03:26 2021

@author: AlainIrastorza
"""

numvacas=int(input("Escribe el número total de vacas:"))
pesototal=int(input("Escribe el peso total permitido del camión:"))

pesovaca=[]
lechevaca=[]
productvaca=[]
pesoselec=0
lechetotal=0

cont=1

while (cont<=numvacas):
    print ("\nVACA NÚMERO",cont)
    pesovaca.append(int(input("Escribe el peso de la vaca:")))
    lechevaca.append(int(input("Escribe la producción de leche en l/día:")))
    productvaca.append(lechevaca[cont-1]/pesovaca[cont-1])
    cont=cont+1
    
fin=0
while fin==0:
    cont=1
    maxproduct=max(productvaca)
    while (productvaca[cont-1]!=maxproduct):
        cont=cont+1
    if ((pesoselec+pesovaca[cont-1])<=pesototal):
        pesoselec=pesoselec+pesovaca[cont-1]
        lechetotal=lechevaca[cont-1]+lechetotal
        print (lechetotal)  #linea a eliminar
    else:
        fin=1
    productvaca[cont-1]=0

print ("\n\nCantidad máxima de producción de leche que se puede obtener:")
print(lechetotal)