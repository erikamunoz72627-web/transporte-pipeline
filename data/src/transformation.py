# Módulo de transformación y limpieza de datos

import pandas as pd


def transformar_datos(df):
    # Eliminar filas completamente vacías
    df = df.dropna(how="all")

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Limpiar espacios en columnas de texto
    columnas_texto = df.select_dtypes(include="object").columns

    for columna in columnas_texto:
        df[columna] = df[columna].astype(str).str.strip()

    return df
