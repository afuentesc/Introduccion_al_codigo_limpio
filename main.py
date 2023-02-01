"""Principal
Este script sirve para ejecutar el modelo de predicción de precios de casas.
El script usa librerias 
It uses pandas and scikit-learn libraries for data manipulation
and creation of machine learning models.

"""

# librerias necesarias
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

# modulos necesarios
from src import general as gral
from src import limpieza as limp
from src import eda
from src import preprocesamiento as prep

# Carga base de datos
train_data = gral.train_data
test_data = gral.test_data
test_ids = test_data['Id']

#EDA: Generamos gráficos con las funciones necsarias
eda.generate_heatmap(train_data)
eda.generate_scatter(train_data)

# Limpieza de datos
# Limpieza:Imputar valores faltantes
limp.fill_no(train_data)
limp.fill_missing_values(train_data)
limp.fill_missing_values(test_data)

# Limpieza:Elimina variables
train_data.drop(gral.drop_col, axis=1, inplace=True)
test_data.drop(gral.drop_col, axis=1, inplace=True)

#Preprocesamiento de datos
#Preprocesamiento: Encoding
prep.encode_ordinal(train_data, test_data)
prep.encode_catagorical_columns(train_data, test_data)

#Preprocesamiento: Ingeniería de entradas
prep.generate_interactions(train_data, test_data)

#Preprocesamiento: Elimina columnas
train_data.drop(gral.drop_final, axis=1, inplace=True)
test_data.drop(gral.drop_final, axis=1, inplace=True)


#Entrenamos modelo
y = train_data['SalePrice']
X = train_data.drop(['SalePrice'], axis=1)

candidate_max_leaf_nodes= gral.max_leaf
for node in candidate_max_leaf_nodes:
    model = RandomForestRegressor(max_leaf_nodes=node,)
    model.fit(X, y)
    score = cross_val_score(model, X, y, cv=10)

# Generamos pedicciones
price = model.predict(test_data)
submission = pd.DataFrame({
    "Id": test_ids,
    "SalePrice": price
})
# Exportamos predicciones
submission_name= "data/submission_"+ gral.date_str + ".csv"
submission.to_csv(submission_name, index=False)
