# Tarea 21

## Enunciado
Se debe diseñar un programa que dado un número introducido entre 0,0001 y 0,9999 (no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible.
___

## Solución planteada
El lenguaje escogido para realizar esta tarea ha sido PYTHON.

En primer lugar aparece en pantalla que se escriba un número entre 0.0001 y 0.9999 (condición del enunciado) mediante una función "while". En caso de que se escriba un número que cumple con esa condición se cálcula la fracción irreducible; en caso contrario, se vuelve a pedir otro número.

Para calcular la fracción irreducible, primero se transforma el número introducido en un número entero multiplicándolo por 10.000 (el número más pequeño es 0.0001 y este multiplicado por 10.000 es 1). 

Se utiliza otra función while en el cual se divide el numerador y enumerador por los números que van desde 0 a 9999 (el mínimo y máximo valor logrado tras multiplicar el número introducido por 10.000) siempre que el resultado de ambas divisiones son números enteros. 

A continuación se presenta un ejemplo del programa:

```
Escriba un número entre 0.0001 y 0.9999:

20
Escriba un número entre 0.0001 y 0.9999:

0.001
Su fracción irreducible es:  1.0 / 1000.0
```