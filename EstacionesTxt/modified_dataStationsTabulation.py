
import os
import re
import csv

def encontrar_linea_encabezado(file_path, encabezado):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        for i, line in enumerate(file, 1):
            if encabezado in line.upper():
                return i
    return None

def extraer_datos_anuales(file_path, start_line, year_start=2000, year_end=2021):
    datos_anuales = {}
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        for i, line in enumerate(file, 1):
            if i > start_line:
                year_data = re.findall(r'\d+', line)
                if year_data:
                    year = int(year_data[0])
                    if year_start <= year <= year_end:
                        datos_anuales[year] = year_data[1:]
    return datos_anuales

# Encabezados de secciones para buscar en cada archivo
encabezados = {
    "precipitacion": "LLUVIA TOTAL MEN",
    # Agregar otros encabezados si es necesario
}

# Directorio donde se encuentran los archivos TXT
directory_path = './Estaciones'

# Creando y escribiendo en el archivo CSV
csv_file_path = './datos_climaticos_anuales.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    encabezados_escritos = False

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".TXT"):
            file_path = os.path.join(directory_path, file_name)

            lineas_encabezado = {seccion: encontrar_linea_encabezado(file_path, encabezado) 
                                 for seccion, encabezado in encabezados.items()}

            datos_anuales = {seccion: extraer_datos_anuales(file_path, linea) 
                            for seccion, linea in lineas_encabezado.items() if linea}

            if all(datos_anuales.values()):
                if not encabezados_escritos:
                    columnas = ['Estación', 'Año'] + list(encabezados.keys())
                    writer.writerow(columnas)
                    encabezados_escritos = True

                for year, data in datos_anuales['precipitacion'].items():
                    fila_datos = [file_name.split('.')[0], year] + data
                    writer.writerow(fila_datos)
