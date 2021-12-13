# Tarea 94

## Enunciado
El módulo se denominará calculadora.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una division entres dos números. Todas las funciones devolverán el resultado.

Se deben tratar los siguientes errores:

1.- En caso de que se envíen valores a las funciones que no sean números debe dar un aviso de tipo de error.

2.- En caso de realizar una división por cero debe dar un aviso de tipo de error.

Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo. Llama a todas las funciones del módulo y observa si el comportamiento es el esperado.
___

## Solución planteada
El modulo calculadora.py se ha estructurado de la siguiente forma:
- Se han definido cuatro funciones, uno por cada operación matemática a realizar.
- Se ha introducido cada función con la siguiente estructura: def NOMBRE (variable1,variable2):
- Se ha introducido la condición de que si se no se introduce un número (tipo int-entero o float-con decimales) se debe indicar al usuario del error. Para ello se ha utilizado la función TYPE.
- Se devuelven los valores al fichero principal mediante un RETURN en cada función.
- En el caso de la división se ha introducido la condición de que si la segunda variable es igual a cero se le debe señalar al usuario que no se puede ejecutar la división. 

El fichero calculos.py se ha estructurado de la siguiente forma:
- Primero se llama al otro fichero con "import calculadora".
- Después, para solicitar e imprimir en pantalla el resultado de cada operación matemática se utiliza la función PRINT y se llama a la función mediante calculadora.NOMBREFUNCIÓN(variable1,variable2)


A continuación se presenta un ejemplo del programa. 
Se solicita realizar una suma con la vocal a y el número 11, una resta con 5 y 10, una multiplicación con 5 y 10 y una división con 5 y 0.

```
El resultado de la suma es:  Error. No se han introducido dos números.
El resultado de la resta es:  -5
El resultado de la multiplicación es:  50
El resultado de la división es:  Error. Número no divisible.
```