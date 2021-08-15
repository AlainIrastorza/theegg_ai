# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 19:25:22 2021

@author: Administrador
"""
#Condiciones iniciales de las variables.
#P significa Pikachu y J Jigglypuff.
#Si el turno vale 0 en el combate ataca Pikachu y si vale 1 viceversa.
#i significa el número del ataque.
AtaqueP=55
VidaP=100
AtaqueJ=45
VidaJ=100
Turno=1
i=0

print ("SITUACIÓN INICIAL:")
print ("PIKACHU \n  Ataque=",AtaqueP,"\n  Vida=",VidaP)
print ("\nJIGGLYPUFF \n  Ataque=",AtaqueJ, "\n  Vida=",VidaJ)

#Comienza el combate.
#El combate finaliza cuando la vida de uno de los Pokemons es igual 
#o inferior a 0.
while VidaP>0 and VidaJ>0:
    if Turno==1:
        VidaJ=VidaJ-AtaqueP
        Turno=0
        i=i+1
        print ("\n\nTras el ataque número",i)
        print ("\nPIKACHU \n  Ataque=",AtaqueP,"\n  Vida=",VidaP)
        print ("\nJIGGLYPUFF \n  Ataque=",AtaqueJ, "\n  Vida=",VidaJ)
        
    else:
        VidaP=VidaP-AtaqueJ
        Turno=1
        i=i+1
        print ("\n\nTras el ataque número",i)
        print ("\nPIKACHU \n  Ataque=",AtaqueP,"\n  Vida=",VidaP)
        print ("\nJIGGLYPUFF \n  Ataque=",AtaqueJ, "\n  Vida=",VidaJ)

#Finaliza el combate y se presenta el ganador.
if VidaP<=0:
    print ("\nHA GANADO JIGGLYPUFF")
    
else:
    print ("\nHA GANADO PIKACHU")