# Tarea 95

## Enunciado
Se deben realizar seis ejercicios:
1.- Realiza un programa que lea 2 números por teclado y determine. Si los dos números son iguales, si los dos números son diferentes, si el primero es mayor que el segundo y si el segundo es mayor o igual que el primero.
2.- Determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual a 5 y a su vez es menor que 10.
3.- Realiza un programa que haga la tabla de multiplicación de un número introducido de valor entre 0 y 99: guarda en una variable el número introducido por el usuario, añade un filtro que asegure que el número sea entre 0 y 99 y escribe la tabla multiplicando el valor introducido por valores entre 1 y 10.
4.- El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?
5.- Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar el proceso debe repetirse hasta que lo introduzca correctamente
6.- Realiza un programa que sume todos los números enteros impares desde el 0 hasta el 115.
___

## Solución planteada
El lenguaje escogido para realizar esta tarea ha sido PYTHON.
A continuación, se explican las soluciones planteadas en cada ejercicio.

- EJERCICIO 1
Se han utilizado las funciónes NUMEROTECLADO1 y NUMEROTECLADO2.
Primero se pide que se escriban dos números.
Después, se llama a cada función y se introducen esos dos números en las funciones.
Mediante condiciones matemáticas (utilizando IF y ELSE) muy sencillas (numero igual a y número mayor a) se responde a los requerimientos del enunciado y se devuelve las respuestas mediante RETURN.

- EJERCICIO 2
Primero el usuario escribe una frase.
Después, se llama a la función LONGITUDFRASE.
En esta función se cuentan el número de caracteres de la frase mediante la variable contador CONT y el número de carácter I. Para ello se utiliza la función FOR.
Después, en función del valor final del contador de caracteres CONT se responde a las cuestiones del enunciado utilizando tres condiciones con IF, ELIF y ELSE.

- EJERCICIO 3
Primero, el usuario debe escribir un número entre 0 y 99.
Se comprueba que el número introducido por el usuario cumple con esa condición mediante un WHILE.
Si no es así se cumple con la condición de entrada del WHILE y se le solicita que vuelva a introducir un número que cumpla con las condiciones solicitadas.
Una vez el usuario introduce un número que cumple con las condiciones explicadas se imprime en la pantalla la tabla de multiplicación (multiplicando el número introducido por el usuario por números desde el 1 al 10 mediante otro WHILE y utilizando a la variable I como número multiplicador).

- EJERCICIO 4
El error detectado ha sido que para realizar la operación matemática de la media (la división de la suma de los tres números) era necesario incluir la suma entre dos parentesis.

- EJERCICIO 5
Se solicita al usuario que escriba un número impar.
Se comprueba que el resto de la división del número introducido entre dos sea igual a 0 (para que sea número no impar).
Si es así, se solicita al usuario que vuelva a introducir un número.
Si no es así, se indica al usuario que el número introducido es impar.

- EJERCICIO 6
Utilizando el sumatorio "sumaimpar" iniciado en cero, se realiza la suma mediante una función WHILE sumando el número de la variable "j" (iniciado en cero y cuyo valor se incrementa en 2 en cada suma para que se mantenga la condición de sumar números impares).
Se finaliza la suma cuando el valor de la variable "j" es superior a 115. 


A continuación se presenta un ejemplo del programa:

```
1.- Escriba un numero:1

Escriba otro número:8

Se concluye lo siguiente: 
 los dos números son diferentes
 y el segundo es mayor o igual que el primero

2.- Escriba una frase:Buenos dias
La cadena de texto tiene una longitud >=10

3.- Escriba un numero entre 0 y 99:100

Vuelva a escribir un número. Debe ser entre 0 y 99:12
A continuación se presenta la tabla multiplicando el valor
introducido por valores entre 1 y 10:
12.0 multiplicado por 1 es 12.0
12.0 multiplicado por 2 es 24.0
12.0 multiplicado por 3 es 36.0
12.0 multiplicado por 4 es 48.0
12.0 multiplicado por 5 es 60.0
12.0 multiplicado por 6 es 72.0
12.0 multiplicado por 7 es 84.0
12.0 multiplicado por 8 es 96.0
12.0 multiplicado por 9 es 108.0
12.0 multiplicado por 10 es 120.0

4.-La nota media es 6.0

5.-Escriba un número impar:8

Error. Vuelve a escribir un número impar:7
Correcto, número impar introducido.

6.- La suma de todos los numeros enteros impares desde 0 hasta 115
es: 3364
```