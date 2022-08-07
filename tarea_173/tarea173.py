# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 22:23:32 2022

@author: Administrador
"""

# Importamos la librería en nuestro programa y le asignamos un alias (pseudónimo)
import pandas as pd

# Leemos un fichero CSV para lo que debemos indicar la ruta.
# Los valores del fichero se le asignan a la variable data 
data = pd.read_csv("pandas\dataset/00_iris.csv");

#listar primeras 3 filas de la cabecera
h=data.head(3);
print(h);

#listar 3 filas aleatorias de la cabecera
z=data.sample(3);
print(z);

#listar últimas 3 filas de la cabecera
w=data.tail(3);
print(w);

#SERIES CON PANDA: CREACIÓN DE DATAFRAME
asignaturas = pd.Series(["Matemática","estadística","Física","Química","Geografía"])
notas  = pd.Series([7.7,3.4,8.3,6.8,9.0])
b=pd.DataFrame({"Asignaturas": asignaturas, "Notas": notas})
print("\n",b);

# Acceso a la columna Notas
c=b.loc[:,"Notas"];
print("\n",c);

# Acceso a las primeras 3 filas
d=b.loc[0:2];
print("\n",d);


#AGRUPACIÓN
#Fíjate que en este DataFrame hay dos liebres
df=pd.DataFrame({'Animales': ['Perro', 'Gato',
                              'Liebre', 'Liebre'],
                   'Kilómetros/hora': [40, 32, 48, 77]})
# Agrupación por animales y sacar la media
e=df.groupby(['Animales']).mean();
print("\n",e);

#BORRADO DE FILAS-COLUMNAS
#asignaturas = pd.Series(["Matemática","estadística","Física","Química","Geografía"])
#notas  = pd.Series([7.7,3.4,8.3,6.8,9.0])
#b = pd.DataFrame({"Asignaturas": asignaturas, "Notas": notas})
m=b;
# Eliminar la columna Asignaturas
m.drop("Asignaturas",axis=1,inplace=True);
print("\n",m);
# Eliminar la cuarta fila
n=b;
n.drop(3,axis=0,inplace=True);
print("\n",n);