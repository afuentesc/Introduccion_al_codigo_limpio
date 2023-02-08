""" General
Este script contiene las variables que se utilizaran en el resto de los
codigos para facilitar cualquier ajuste al usuario.

Este script asume que se cuenta con los archivos de datos en formato
(.csv) sin procesar en las carpetas de datos **********

El script tambien necesita contar con la libreria de `pandas`, `****`
instaladas en Python.
"""

# Librerias necesarias
from datetime import datetime
import pandas as pd
import logging

# Configuracion de logging
logging.basicConfig(
    filename='./resultados_gral.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

# Variable para tener fecha actual para las versiones
now = datetime.today()
date_str = now.strftime("%d%m_%H%M")

try:
    eda_heatmap = "imgs/heatmap_" + date_str + ".png"
    eda_scatter = "imgs/scatter_" + date_str + ".png"
except:
    TypeError: logging.error("Fallo generar nombres de imagenes.")


# Variables con datos originales
try:
    train_data = pd.read_csv("data/raw_train.csv")
    test_data = pd.read_csv("data/raw_test.csv")
except:
    FileNotFoundError: logging.error("No se encontraron los archivos csv.")


# Variables de las columnas de datos
drop_col = ["Id", "Alley", "PoolQC", "MiscFeature", "Fence",
            "MoSold", "YrSold", "MSSubClass", "GarageType",
            "GarageArea", "GarageYrBlt", "GarageFinish",
            "YearRemodAdd", "LandSlope", "BsmtUnfSF",
            "BsmtExposure", "2ndFlrSF", "LowQualFinSF",
            "Condition1", "Condition2", "Heating", "Exterior1st",
            "Exterior2nd", "HouseStyle", "LotShape",
            "LandContour", "LotConfig", "Functional", "BsmtFinSF1",
            "BsmtFinSF2", "FireplaceQu", "WoodDeckSF", "GarageQual",
            "GarageCond", "OverallCond"
            ]

drop_final = ['OverallQual', 'ExterCond', 'ExterQual', 'BsmtCond',
              'BsmtQual', 'BsmtFinType1', 'BsmtFinType2', 'HeatingQC',
              'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch',
              'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
              ]
