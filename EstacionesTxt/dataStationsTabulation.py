import os
import re
import csv

def encontrar_linea_encabezado(file_path, encabezado):
    """
    Encuentra la línea número en la que aparece el encabezado dado.
    """
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        for i, line in enumerate(file, 1):
            if encabezado in line.upper():
                return i
    return None

def extraer_medias(file_path, start_line):
    """
    Extrae las medias mensuales de una sección dada comenzando en 'start_line'.
    """
    medias = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        for i, line in enumerate(file, 1):
            if i > start_line:
                if "MEDIA" in line.upper():
                    medias = re.findall(r'\d+\.\d+|\d+', line)
                    break
    if len(medias) > 12:
        medias = medias[:12]
    return medias

# Encabezados de secciones para buscar en cada archivo
encabezados = {
    "evaporacion": "EVAPORACION MEN.",
    "lluvia": "LLUVIA TOTAL MEN",
    "temp_max": "TEMP MAXIMA PROM",
    "temp_min": "TEMP MINIMA PROM"
}

# Directorio donde se encuentran los archivos TXT
directory_path = './Estaciones'

# Creando y escribiendo en el archivo CSV
csv_file_path = './datos_climaticos_resumidos.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    encabezados_escritos = False # Para escribir los encabezados solo una vez

    # Iterando sobre cada archivo en el directorio
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".TXT"):
            file_path = os.path.join(directory_path, file_name)
            
            # Encontrando las líneas de encabezado para cada sección
            lineas_encabezado = {seccion: encontrar_linea_encabezado(file_path, encabezado) 
                                 for seccion, encabezado in encabezados.items()}

            # Extrayendo medias mensuales para cada sección
            datos_medias = {seccion: extraer_medias(file_path, linea) 
                            for seccion, linea in lineas_encabezado.items() if linea}

            # Escribiendo los datos al CSV
            if all(datos_medias.values()):  # Verificar que todas las secciones tengan datos
                if not encabezados_escritos:  # Si es la primera línea, escribir encabezados
                    columnas = ['Estación']
                    for param in ['prec', 'eva', 'tempMax', 'tempMin']:
                        for mes in ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']:
                            columnas.append(f'{param}{mes}')
                    writer.writerow(columnas)
                    encabezados_escritos = True

                fila_datos = [file_name.split('.')[0]]  # Nombre del archivo como nombre de la estación
                for seccion in ['lluvia', 'evaporacion', 'temp_max', 'temp_min']:
                    fila_datos.extend(datos_medias[seccion])

                writer.writerow(fila_datos)

csv_file_path
