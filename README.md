# Tarea 03: Introducción al código limpio.

En esta tarea se busca implementar el desarrollo de un modelo de ciencia de datos para el pronostico del precio de casas utilizando como base el código de 
[Kaggle.](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview)


# Dependencias.

El modelo y los scripts se desarrollaron utilizando Python (3.9.13). Las librerias necesarias para la ejecución de los scripts son: `datetime/`, `pandas/`, `matplotlib/`, `seaborn/`, `pytest/` ,  `logging/` y  `scikit-learn/`.

# Inputs / Outputs.

El proyecto considera para los inputs un set de datos de entrenamiento (raw_train.csv) y un set de test (raw_test.csv). Adicionalmente en el script general.py se incluyen variables que sirven de input en el resto de scripts.

El output del modelo se obtiene en imagenes en formato png para un analisis EDA (heatmap_0102_1320.png, scatter_0102_1320), y también se obtiene un csv con las predicciones realizadas por el modelo (submission_0102_1320.csv). El formato de los outputs incluye el nombre del archivo con la fecha en formato dia, mes, hora y minuto de ejecución.

# Estructura del repositorio.
El repositorio cuenta cuenta con dos carpetas.

- En `data/` se almacenan los archivos csv con los datos originales y csv con las predicciones.
- En `imgs/` se almacenan las imágenes generadas para el EDA.
- En `src/` se almacenan los  scripts de python.

```
├── main.py
├── README.md
├── environments.yml
├── test
│   ├── test_limpieza.py
├── data
│   ├── data_description.txt
│   ├── raw_test.csv
│   ├── raw_train.csv
│   ├── submission_0102_1320.csv
├── imgs
│   ├── heatmap_0102_1320.png
│   ├── scatter_0102_1320.png
└── src
    ├── __init__.py
    ├── general.py
    ├── eda.py
    ├── limpieza.py
    └── preprocesamiento.py

```

# Ejecución.

La ejecución del proyecto se realiza desde el script `main.py/`


