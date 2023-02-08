""" Preprocesamiento
Este script  permite realizar un preprocesamiento de los datasets.
Cuenta con funciones para realizar One-Hot-Encoding de variables,
así como también funciones para realizar ingeniería de entradas con interacciones
entre las variables.
El script tambien necesita contar con la libreria de `pandas` y `scikit-learn`.
"""

# Librerias necesarias
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder


def encode_ordinal(train_data,test_data):
    """
    Realiza One-Hot-Encoding sobre las variables ordinales que lo requieran de set entrenamiento y test.
    :param train_data: dataframe con el set de datos de entrenamiento.
    :param test_data: dataframe con el set de datos de test.   
    :return: agrega la transformacion de las variables en los datasets.
    """
    OE1 = OrdinalEncoder(categories=[['No', 'Po', 'Fa', 'TA', 'Gd', 'Ex']])
    train_data['BsmtQual'] = OE1.fit_transform(train_data[['BsmtQual']])
    test_data['BsmtQual'] = OE1.transform(test_data[['BsmtQual']])
    train_data['BsmtCond'] = OE1.fit_transform(train_data[['BsmtCond']])
    test_data['BsmtCond'] = OE1.transform(test_data[['BsmtCond']])
    
    OE2 = OrdinalEncoder(categories=[['Po', 'Fa', 'TA', 'Gd', 'Ex']])
    train_data['ExterQual'] = OE2.fit_transform(train_data[['ExterQual']])
    test_data['ExterQual'] = OE2.transform(test_data[['ExterQual']])
    train_data['ExterCond'] = OE2.fit_transform(train_data[['ExterCond']])
    test_data['ExterCond'] = OE2.transform(test_data[['ExterCond']])
    train_data['KitchenQual'] = OE2.fit_transform(train_data[['KitchenQual']])
    test_data['KitchenQual'] = OE2.transform(test_data[['KitchenQual']])
    
    OE3 = OrdinalEncoder(categories=[['N', 'P', 'Y']])
    train_data['PavedDrive'] = OE3.fit_transform(train_data[['PavedDrive']])
    test_data['PavedDrive'] = OE3.transform(test_data[['PavedDrive']])
    
    OE4 = OrdinalEncoder(categories=[['Mix', 'FuseP', 'FuseF', 'FuseA', 'SBrkr']])
    train_data['Electrical'] = OE4.fit_transform(train_data[['Electrical']])
    test_data['Electrical'] = OE4.transform(test_data[['Electrical']])
    
    OE5 = OrdinalEncoder(categories=[['No', 'Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ']])
    train_data['BsmtFinType1'] = OE5.fit_transform(train_data[['BsmtFinType1']])
    test_data['BsmtFinType1'] = OE5.transform(test_data[['BsmtFinType1']])
    train_data['BsmtFinType2'] = OE5.fit_transform(train_data[['BsmtFinType2']])
    test_data['BsmtFinType2'] = OE5.transform(test_data[['BsmtFinType2']])
    
    OE6 = OrdinalEncoder(categories=[['ELO', 'NoSeWa', 'NoSewr', 'AllPub']])
    train_data['Utilities'] = OE6.fit_transform(train_data[['Utilities']])
    test_data['Utilities'] = OE6.transform(test_data[['Utilities']])
    
    OE7 = OrdinalEncoder(categories=[['C (all)', 'RH', 'RM', 'RL', 'FV']])
    train_data['MSZoning'] = OE7.fit_transform(train_data[['MSZoning']])
    test_data['MSZoning'] = OE7.transform(test_data[['MSZoning']])
    
    OE8 = OrdinalEncoder(categories=[['Slab', 'BrkTil', 'Stone', 'CBlock', 'Wood', 'PConc']])
    train_data['Foundation'] = OE8.fit_transform(train_data[['Foundation']])
    test_data['Foundation'] = OE8.transform(test_data[['Foundation']])
    
    OE9 = OrdinalEncoder(categories=[['MeadowV', 'IDOTRR', 'BrDale', 'Edwards', 'BrkSide', 'OldTown', 'NAmes', 'Sawyer', 'Mitchel', 'NPkVill', 'SWISU', 'Blueste', 'SawyerW', 'NWAmes', 'Gilbert', 'Blmngtn', 'ClearCr', 'Crawfor', 'CollgCr', 'Veenker', 'Timber', 'Somerst', 'NoRidge', 'StoneBr', 'NridgHt']])
    train_data['Neighborhood'] = OE9.fit_transform(train_data[['Neighborhood']])
    test_data['Neighborhood'] = OE9.transform(test_data[['Neighborhood']])
    
    OE10 = OrdinalEncoder(categories=[['None', 'BrkCmn', 'BrkFace', 'Stone']])
    train_data['MasVnrType'] = OE10.fit_transform(train_data[['MasVnrType']])
    test_data['MasVnrType'] = OE10.transform(test_data[['MasVnrType']])
    
    OE11 = OrdinalEncoder(categories=[['AdjLand', 'Abnorml','Alloca', 'Family', 'Normal', 'Partial']])
    train_data['SaleCondition'] = OE11.fit_transform(train_data[['SaleCondition']])
    test_data['SaleCondition'] = OE11.transform(test_data[['SaleCondition']])
    
    OE12 = OrdinalEncoder(categories=[['Gambrel', 'Gable','Hip', 'Mansard', 'Flat', 'Shed']])
    train_data['RoofStyle'] = OE12.fit_transform(train_data[['RoofStyle']])
    test_data['RoofStyle'] = OE12.transform(test_data[['RoofStyle']])
    
    OE13 = OrdinalEncoder(categories=[['ClyTile', 'CompShg', 'Roll','Metal', 'Tar&Grv','Membran', 'WdShake', 'WdShngl']])
    train_data['RoofMatl'] = OE13.fit_transform(train_data[['RoofMatl']])
    test_data['RoofMatl'] = OE13.transform(test_data[['RoofMatl']])


    
def encode_catagorical_columns(train, test):
    """
    Realiza One-Hot-Encoding sobre las variables categoricas que lo requieran de set entrenamiento y test.
    :param train_data: dataframe con el set de datos de entrenamiento.
    :param test_data: dataframe con el set de datos de test.   
    :return: agrega la transformacion de las variables en los datasets.
    """
    level_col = ['Street' ,'BldgType', 'SaleType', 'CentralAir']
    encoder = LabelEncoder()
    for col in level_col:
        train[col] = encoder.fit_transform(train[col])
        test[col]  = encoder.transform(test[col])

        
def generate_interactions(train_data, test_data):
    """
    Genera nuevas variables con ingenieria de variables mediante interacciones de las mismas.
    :param train_data: dataframe con el set de datos de entrenamiento.
    :param test_data: dataframe con el set de datos de test.   
    :return: agrega las interacciones de las variables en los datasets.
    """
    train_data['BsmtRating'] = train_data['BsmtCond'] * train_data['BsmtQual']
    train_data['ExterRating'] = train_data['ExterCond'] * train_data['ExterQual']
    train_data['BsmtFinTypeRating'] = train_data['BsmtFinType1'] * train_data['BsmtFinType2']

    train_data['BsmtBath'] = train_data['BsmtFullBath'] + train_data['BsmtHalfBath']
    train_data['Bath'] = train_data['FullBath'] + train_data['HalfBath']
    train_data['PorchArea'] = train_data['OpenPorchSF'] + train_data['EnclosedPorch'] + train_data['3SsnPorch'] + train_data['ScreenPorch']

    test_data['BsmtRating'] = test_data['BsmtCond'] * test_data['BsmtQual']
    test_data['ExterRating'] = test_data['ExterCond'] * test_data['ExterQual']
    test_data['BsmtFinTypeRating'] = test_data['BsmtFinType1'] * test_data['BsmtFinType2']

    test_data['BsmtBath'] = test_data['BsmtFullBath'] + test_data['BsmtHalfBath']
    test_data['Bath'] = test_data['FullBath'] + test_data['HalfBath']
    test_data['PorchArea'] = test_data['OpenPorchSF'] + test_data['EnclosedPorch'] + test_data['3SsnPorch'] + test_data['ScreenPorch']
