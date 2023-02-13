""" Test Limpieza
Este script contiene las funciones para hacer el test a las funciones fill_no,
del modulo Eda.

El script tambien necesita contar con la libreria de `pytest`.

"""
import logging
import pandas as pd
from src.limpieza import fill_no


try:
    data = pd.read_csv("data/raw_train.csv")
except AssertionError:
    logging.error("No se encontraron los archivos csv.")


def test_fill_no(data):
    """
    Hace un test para revisar la funcionalidad de fill_no
    :param data: dataframe con el set de datos a complementar.
    """
    try:
        data_clean = fill_no(data)

    except AssertionError as err:
        logging.error("Error en la limpieza del archivo")
        raise err
    return data_clean
