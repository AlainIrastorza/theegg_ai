# Tarea 89

## Enunciado
Se deben codigicar cinco funciones:
- Función que calcule el máximo de 2 números
- Función que calcule el máximo de 3 números
- Función que calcule la longitud de una frase
- Función que determine si el carácter introducido es vocal o no
- Función que sume y multiplique los valores de una lista
___

## Solución planteada
El lenguaje escogido para realizar esta tarea ha sido PYTHON.
En las cinco funciones se ha utilizado una estructura muy parecida.

- Función que calcule el máximo de 2 números
  Se introducen los dos números en la función y se utilizan tres condiciones con if.
  En la primera condición si el segundo número es mayor que el primer número la función devuelve el número 2.
  En la segunda condición si el primer número es mayor que el segundo número la función devuelve el número 1.
  En la tercera condición si el primer y el segundo número son iguales la función devuelve la frase "son iguales".

- Función que calcule el máximo de 3 números
  El funcionamiento de esta función es muy similar a la función que calcula el máximo de 2 números.
  La diferencia es que se deben introducir más condiciones al tratarse de más números.

- Función que calcule la longitud de una frase
  Se utiliza una función "for" y un contador de caracteres que parte de 0.
  Mediante la función "for" se le suma el número uno al contador cada vez que se cuenta un carácter de la frase analizada.

- Función que determine si el carácter introducido es vocal o no
  Se utiliza una condición con if: si la letra introducida es uno de los vocales (mediante OR) se indica que es vocal.

- Función que sume y multiplique los valores de una lista
  Se vuelve a utilizar la función for.
  En el caso de la suma se utiliza la variable sumatot que parte del valor cero y se le suma el valor de cada numéro de la lista de numeros de la variable numerossuma.
  En el caso de la multiplicación el funcionamiento es similar pero se utiliza la variable mult que parte de 1 (si partiese de cero el resultado sería siempre cero).

A continuación se presenta un ejemplo del programa:

```
El mayor número entre 12 y 12 es son iguales
El mayor número entre 13 , 12 y 11 es 13
La longitud de la frase Buenos dias es de 11 caracteres.
La letra b no es vocal
La suma de los numeros [5, 6, 7] es 18
La multiplicacion de los numeros [5, 6, 7] es 210
```