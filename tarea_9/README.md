# Tarea 9

## Enunciado
Se pide que de manera conceptual se explique qué pasos habría que seguir para hacerlos posible. La respuesta es creativa, no hay una solución única.
___

## Solución planteada: Adelantarse a nuestros gustos. Como lo hacen Amazon, Microsoft, Google (General)

Para poder adelantarse a nuestros gustos, como lo hacen distintas compañias, se podrían utilizar las cookies.

Entre las funciones de las cookies destacan la posibilidad de recordar las configuraciones y estados en las páginas webs visitadas en una sesión de navegación, y también, conocer la información sobre los hábitos de navegación.

En el segundo caso, se permite identificar que búsquedas realiza el usuario. 

El tipo de configuración necesario de las cookies para este fin es el de "socios comerciales". Es posible que incluso se tuviese que comprar esta información a navegadores como Google por ejemplo.

De esta manera, se recibiría desde internet un conjunto de bits en un vector, los cuales después se deberían de segmentar para extraer la información. Un ejemplo de como segmentar la información podría ser el siguiente:
    - Fecha - Hora - IP remitente - IP destino - Contenido de la búsqueda

A partir del registro estructurado de las búsquedas habría que crear una base de datos de cada usuario (con su IP correspondiente) y almacenar en ella todas las búsquedas realizadas. También es interesante almacenar la fecha y la hora de la búsqueda debido a que existe mayor posibilidad de que las búsquedas más recientes se conviertan en compras por ejemplo, en comparación a búsquedas mas antiguas. 

A partir de la información estructurada, se debería de utilizar un modelo de Machine Learning o Deep Learning.

La mejor manera de comprobar la efectividad del modelo sería analizar si las búsquedas que realiza el cliente son acordes al resultado del modelo.