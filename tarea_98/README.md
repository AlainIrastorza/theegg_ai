# Tarea 98

## Ejercicio
En esta tarea, se pretende analizar la eficiencia de los algoritmos a medida que aumenta la cantidad de datos a procesar.

En este caso se escriben dos funciones distintas para calcular la suma acumulada de un número.

En el primer caso, la suma se realiza linealmente; es decir, se realiza la suma acumulada de numéro en número.
En el segundo caso, la suma se realiza de manera constante, mediante una formula.

Evidentemente, según la lógica en el primer caso (suma lineal) se debería de tardar más tiempo que en el segundo caso (suma constante). A continuación, en la solución planteada se puede ver que es así.


___

## Solución planteada

A continuación se presenta un ejemplo del programa:

En cada linea aparece primero el valor de la suma y después el tiempo que se ha requerido para realizar la suma.
La primera linea corresponde a la suma lineal y la segunda a la suma constante.
Después, semultiplica por 10 el numero de cuya suma se debe calcular y se repite la operación.
Se han realizado los cálculos para cuatro numeros. 

```
SumaLineal: 500000500000 - 0.2178785800933838
SumaConstante:500000500000.0 - 0.0
SumaLineal: 50000005000000 - 2.0268402099609375
SumaConstante:50000005000000.0 - 0.0
SumaLineal: 5000000050000000 - 16.577600955963135
SumaConstante:5000000050000000.0 - 0.0
SumaLineal: 500000000500000000 - 179.6079864501953
SumaConstante:5.000000005e+17 - 0.0
```