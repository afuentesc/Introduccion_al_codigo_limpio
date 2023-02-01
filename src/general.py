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

# Variable para tener fecha actual para las versiones
now = datetime.today()
date_str = now.strftime("%d%m_%H%M")
eda_heatmap = "heatmap_" + date_str 
eda_scatter = "scatter_" + date_str 

# Variables con datos originales
train_data = pd.read_csv("house-prices-data/raw_train.csv") #Cambiar path
test_data = pd.read_csv("house-prices-data/raw_test.csv") #Cambiar path

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

ordinal_col = ['GarageQual', 'GarageCond', 'BsmtQual', 'BsmtCond', 
               'ExterQual', 'ExterCond', 'KitchenQual', 'FireplaceQu',
               'PavedDrive', 'Functional', 'Electrical', 'Heating', 
               'BsmtFinType1', 'BsmtFinType2', 'Utilities'
              ]

level_col = ['Street' ,'BldgType', 'SaleType', 'CentralAir']

drop_final = ['OverallQual', 'ExterCond', 'ExterQual','BsmtCond',
            'BsmtQual','BsmtFinType1', 'BsmtFinType2','HeatingQC',
            'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch',
            'BsmtFullBath', 'BsmtHalfBath','FullBath', 'HalfBath',
             ]
fill_col_no = ['FireplaceQu',"BsmtQual", "BsmtCond", "BsmtFinType1", "BsmtFinType2"]

target = "SalePrice"


# Variables hiperparametros del modelo ml
max_leaf = 250
