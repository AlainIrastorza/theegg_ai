# Tarea 22

## Enunciado
Se debe diseñar un programa que dado un número introducido entre 0,0001 y 0,9999 y no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible.
___

## Solución planteada
El lenguaje escogido para realizar esta tarea ha sido PYTHON.
El fichero a corregir es "Tarea 22 OPTIMIZADO.py" el cual se ha diseñadp mediante la programación dinámica. 

En primer lugar, se pide la entrada del número de vacas y del peso permitido de carga en el camión. Ambas variables (numvacas y pesototal) son de tipo int (números enteros).  

Después, se crean e inicializan las variables de peso y producción de leche en litros de cada vaca (de tipo int otra vez). Ambos son de tipo array. A continuación, se pide la entrada de datos de ambos variables. A la hora de escribir los datos se escriben primero los pesos de cada vaca separados por un espaciado y al finalizar se pulsa "enter". La producción de cada vaca se escribe de la misma manera, manteniendo el orden de las vacas.

Para calcular el valor máximo de producción de las vacas que se pueden transportar se ha utilizado programación dinámica. Se ha creado una matriz bidimensional en el cual el peso de las vacas son j. Para ello, se emplea un generador de lista (comienza por "max_lechevaca=...").

Por último se realiza el cálculo y la presentación de la selección de vacas. Las vacas seleccionadas se presentan con un "1", mientras que las vacas no seleccionadas se presentan con un "0". 



A continuación se presenta un ejemplo del programa:

```
Escribe el número total de vacas:4

Escribe el peso total permitido del camión:200
Ingrese el peso de cada vaca:
200 120 340 80
Ingrese la producción en litros diaria de cada vaca:
40 60 50 10
Cuando el peso permitido en el camión es  200, el valor máximo de producción de leche en litros es: 70
Las vacas que se escogen son (1 se coge, 0 no se coge):0 1 0 1
```