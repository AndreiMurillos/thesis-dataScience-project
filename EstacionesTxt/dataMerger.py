import pandas as pd

# Cargar el archivo "PROMEDIO_GRUPO1.xlsx" para revisar su estructura
promedio_grupo1_df = pd.read_excel('C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/ExcelGrupo3/PROMEDIO_GRUPO_3.xlsx')

sheet_names = pd.ExcelFile('C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/ExcelGrupo3/PROMEDIO_GRUPO_3.xlsx').sheet_names

# Cargar las hojas para evaporación, temperatura máxima y temperatura mínima
precipitacion_df = pd.read_excel('C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/ExcelGrupo3/PROMEDIO_GRUPO_3.xlsx', sheet_name='LLUVIA TOTAL MEN')
evaporacion_df = pd.read_excel('C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/ExcelGrupo3/PROMEDIO_GRUPO_3.xlsx', sheet_name='EVAPORACION MEN')
temp_maxima_df = pd.read_excel('C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/ExcelGrupo3/PROMEDIO_GRUPO_3.xlsx', sheet_name='TEMP MAXIMA PROM')
temp_minima_df = pd.read_excel('C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/ExcelGrupo3/PROMEDIO_GRUPO_3.xlsx', sheet_name='TEMP MINIMA PROM')


# Definir una función para transformar los datos al formato deseado
def transformar_datos(año, precipitacion, evaporacion, temp_max, temp_min):
    """Transforma los datos de las hojas de cálculo en el formato deseado."""
    # Crear una lista para almacenar los datos transformados
    datos_transformados = []
    
    # Iterar sobre cada mes
    meses = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']
    for i, mes in enumerate(meses, start=1):
        for año_index in range(len(año)):
            datos_transformados.append([
                "Region 3", # Region
                año[año_index], # Año
                i, # Mes (formato numérico)
                precipitacion[mes][año_index], # Precipitación
                evaporacion[mes][año_index], # Evaporación
                temp_max[mes][año_index], # Temperatura Máxima
                temp_min[mes][año_index], # Temperatura Mínima
            ])
    
    # Convertir la lista a DataFrame
    columnas = ['Region', 'Año', 'Mes', 'precipitacion', 'evaporacion', 'temperaturaMax', 'temperaturaMin']
    datos_transformados_df = pd.DataFrame(datos_transformados, columns=columnas)
    
    return datos_transformados_df

# Llamar a la función para transformar los datos
datos_transformados_df = transformar_datos(
    promedio_grupo1_df['Año'],
    precipitacion_df,
    evaporacion_df,
    temp_maxima_df,
    temp_minima_df
)

archivo_destino = 'C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/datosLimpiosGrupo3.xlsx'
datos_transformados_df.to_excel(archivo_destino, index=False)

archivo_destino

