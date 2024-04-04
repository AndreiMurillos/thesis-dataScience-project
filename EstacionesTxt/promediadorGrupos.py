import pandas as pd
import numpy as np
from pathlib import Path

def leer_y_preparar_excel(archivo_excel):
    """
    Lee un archivo Excel y prepara sus datos, reemplazando "-" por NaN.
    """
    excel = pd.ExcelFile(archivo_excel)
    datos_preparados = {}
    
    for nombre_hoja in excel.sheet_names:
        df = excel.parse(sheet_name=nombre_hoja)
        df.replace({"-": np.nan}, inplace=True)
        df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
        datos_preparados[nombre_hoja] = df
    
    return datos_preparados

def combinar_y_promediar(datos):
    """
    Combina los DataFrames de múltiples archivos y calcula el promedio.
    """
    promedios = {}
    for hoja in datos[0]:
        frames = [d[hoja] for d in datos]
        df_concat = pd.concat(frames)
        df_promedio = df_concat.groupby('Año', as_index=False).mean()
        promedios[hoja] = df_promedio
    return promedios

def generar_archivo_promedio(lista_archivos, archivo_salida):
    """
    Genera un archivo Excel con el promedio de los valores de múltiples archivos Excel.
    """
    datos_excel = [leer_y_preparar_excel(archivo) for archivo in lista_archivos]
    promedios_globales = combinar_y_promediar(datos_excel)
    
    with pd.ExcelWriter(archivo_salida) as writer:
        for hoja, df in promedios_globales.items():
            df.to_excel(writer, sheet_name=hoja, index=False)

def encontrar_archivos_excel(directorio, extension=".xlsx"):
    """
    Encuentra todos los archivos en el directorio dado con la extensión especificada.
    """
    return [str(archivo) for archivo in Path(directorio).glob(f'*{extension}')]

def generar_archivo_promedio_desde_carpeta(directorio, archivo_salida="/mnt/data/Promedio_Estaciones_Carpeta.xlsx"):
    """
    Genera un archivo Excel con el promedio de los valores de todos los archivos Excel en un directorio.
    """
    lista_archivos = encontrar_archivos_excel(directorio)
    if not lista_archivos:
        print("No se encontraron archivos Excel en el directorio especificado.")
        return
    
    generar_archivo_promedio(lista_archivos, archivo_salida)

# Ejemplo de uso
directorio = 'C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/ExcelGrupo3'  # Ajusta esta ruta al directorio que contiene tus archivos Excel
archivo_salida = 'C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/ExcelGrupo3/PROMEDIO_GRUPO_3.xlsx'
generar_archivo_promedio_desde_carpeta(directorio, archivo_salida)
