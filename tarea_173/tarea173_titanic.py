# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 22:23:32 2022

@author: Administrador
"""

# Importamos la librería en nuestro programa y le asignamos un alias (pseudónimo)
import pandas as pd

# Leemos un fichero CSV para lo que debemos indicar la ruta.
# Los valores del fichero se le asignan a la variable data 
data = pd.read_csv("pandas\dataset/02_titanic.csv");

print(data);