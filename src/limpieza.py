""" Limpieza
Este script permite complementar los datos faltantes con diferentes valores
de acuerdo al tipo de variable.
Cuenta con dos funciones, una permite llenar los datos faltantes con el texto No,
la segunda funcion permite imputar la media a los datos faltantes de variables numericas,
y la moda a variables categoricas.
El script tambien necesita contar con la libreria de `pandas`.
"""

# Librerias necesarias
import pandas as pd
#from general import fill_no

# funcion para completar valores
def fill_no(data):
    """
    Complementa la informacion faltante con el texto No.
    :param data: dataframe con el set de datos a complementar.
    :return: regresa el dataset con los datos imputados.
    """
    for col in fill_col_no:
        data[col].fillna("No", inplace=True)
    return data

# funcion para completar valores
def fill_missing_values(data):
    """
    LLena la informacion faltante con la media en variables numericas y moda en variables categoricas.
    :param data: dataframe con el set de datos a complementar.
    :return: regresa el dataset con los datos imputados.
    """
    for col in data.columns:
        if ((data[col].dtype == 'float64') or (data[col].dtype == 'int64')):
            data[col].fillna(data[col].mean(), inplace=True)
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)
    return data
