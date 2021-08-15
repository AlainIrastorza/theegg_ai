# Tarea 33

## Enunciado
Se debe codificar un programa en base al diagrama de flujo del programa de pikachu tal y como se explica en el vídeo adjuntado en el enunciado de la tarea.
___

## Solución planteada
El lenguaje escogido para realizar esta tarea ha sido PYTHON.

En primer lugar se asignan los valores iniciales a las variables:
- AtaqueP: el valor que le resta Pikachu a la vida de Jigglupuff en un ataque.
- VidaP: la vida de Pikachu cuyos posibles valores son del 0 (sin vida) a 100 (vida máxima, inicial)
- AtaqueJ: el valor que le resta Jigglupuff a la vida de Pikachu en un ataque.
- VidaJ: la vida de Jigglupuff cuyos posibles valores son del 0 (sin vida) a 100 (vida máxima, inicial)
- Turno: si su valor es 0 (valor inicial) es turno de Pikachu en el combate y si su valor es 1 es turno de Jigglypuff.
- i: el número del ataque.

Mediante un while y con la condición de que la vida de ambos Pokemons es superior a 0 se suceden los ataques de ambos (se alternan) considerando las condiciones y variables anteriormente descritas.

Cuando la vida de uno de los Pokemons es inferior o igual a 0 se termina el combate y se informa sobre el ganador del combate.

A continuación se presenta un ejemplo del programa:

```
SITUACIÓN INICIAL:
PIKACHU 
  Ataque= 55 
  Vida= 100

JIGGLYPUFF 
  Ataque= 45 
  Vida= 100


Tras el ataque número 1

PIKACHU 
  Ataque= 55 
  Vida= 100

JIGGLYPUFF 
  Ataque= 45 
  Vida= 45


Tras el ataque número 2

PIKACHU 
  Ataque= 55 
  Vida= 55

JIGGLYPUFF 
  Ataque= 45 
  Vida= 45


Tras el ataque número 3

PIKACHU 
  Ataque= 55 
  Vida= 55

JIGGLYPUFF 
  Ataque= 45 
  Vida= -10

HA GANADO PIKACHU
```