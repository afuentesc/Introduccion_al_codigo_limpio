""" EDA
Este script contiene las funciones para realizar las graficas para un EDA,
y posteriormente guardar los outputs como imagenes.

El script tambien necesita contar con la libreria de `pandas`, `seaborn` y
`matplotlib.pyplot` instaladas en Python.

Los outputs generados por las funciones se guardaran en la carpeta imgs del
repositorio.
"""

# Librerias necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#from general import eda_heatmap, eda_scatter

# funciones para gráficar

# funcion para hacer un heatmap
def generate_heatmap(data): 
    """
    Grafica los valores faltantes de las variables para un analisis EDA.
    :param data: dataframe con el set de datos a analizar
    :return: guarda la imagen como eda_heatmap.
    """
    fig, ax = plt.subplots(figsize=(25, 10))
    sns.heatmap(data=data.isnull(), yticklabels=False, ax=ax)
    #fig.savefig(eda_heatmap)
    

# funcion para hacer grafica dispersion 
def generate_violin(data): 
    """
    Grafica una combinacion de scatters, histogramas y diagramas de violin para un analisis EDA.
    :param data: dataframe con el set de datos a analizar
    :return: guarda la imagen como eda_scatter.
    """
    fig, ax = plt.subplots(figsize=(25, 10))
    sns.countplot(x=data['SaleCondition'])
    sns.histplot(x=data['SaleType'], kde=True, ax=ax)
    sns.violinplot(x=data['HouseStyle'], y=data['SalePrice'], ax=ax)
    sns.scatterplot(x=data["Foundation"], y=data["SalePrice"],palette='deep', ax=ax)
    plt.grid()
    #fig.savefig(eda_scatter)    
    
