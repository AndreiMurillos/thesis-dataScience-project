import pandas as pd
import os

def find_start_lines(file_path, keywords):
    start_lines = {}
    with open(file_path, 'r', encoding='latin-1') as file:
        for i, line in enumerate(file, start=1):
            for keyword in keywords:
                if keyword.upper() in line.upper():  # Hacer la comparación insensible a mayúsculas
                    start_lines[keyword] = i + 1
                    break
    return start_lines

def process_section(file_path, start_line, end_year=2021, start_year=2000):
    data = []
    with open(file_path, 'r', encoding='latin-1') as file:
        for i, line in enumerate(file, start=1):
            if i >= start_line:
                parts = line.split()
                if len(parts) >= 13:
                    try:
                        year = int(parts[0])
                        if start_year <= year <= end_year:
                            monthly_values = parts[1:13]
                            data.append([year] + monthly_values)
                    except ValueError:
                        break
    columns = ['Año', 'ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']
    df = pd.DataFrame(data, columns=columns)
    return df

def process_files(input_folder, output_folder):
    keywords = ['EVAPORACION MEN', 'LLUVIA TOTAL MEN', 'TEMP MAXIMA PROM', 'TEMP MINIMA PROM']
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.TXT') or file_name.endswith('.txt'):  # Asegurar que es un archivo .txt
            file_path = os.path.join(input_folder, file_name)
            start_lines = find_start_lines(file_path, keywords)
            dataframes = []
            sheet_names = []
            for keyword, start_line in start_lines.items():
                df = process_section(file_path, start_line)
                dataframes.append(df)
                sheet_names.append(keyword)
            
            # Crear un archivo Excel para cada archivo de texto
            excel_file_name = os.path.splitext(file_name)[0] + '.xlsx'
            excel_path = os.path.join(output_folder, excel_file_name)
            with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
                for df, sheet_name in zip(dataframes, sheet_names):
                    df.to_excel(writer, sheet_name=sheet_name, index=False)

# Especifica la carpeta de entrada y salida
input_folder = 'C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/Estaciones/Grupo3'
output_folder = 'C:/Users/carli/Desktop/proyectoTesina/EstacionesTxt/ExcelGrupo3'

# Procesar todos los archivos
process_files(input_folder, output_folder)



### PARA GUARDARLO EN CSV

# import pandas as pd
# import os

# def find_section_start_line(file_path, section_name):
#     """
#     Encuentra la línea de inicio de una sección basada en una palabra clave.

#     :param file_path: Ruta al archivo de texto.
#     :param section_name: Nombre de la sección para buscar.
#     :return: Número de línea donde comienza la sección o None si no se encuentra.
#     """
#     with open(file_path, 'r', encoding='latin-1') as file:
#         for i, line in enumerate(file, start=1):
#             if section_name in line:
#                 return i
#     return None

# def process_section(file_path, section_name, end_year=2021, start_year=2000):
#     # Encuentra el inicio de la sección
#     start_line = find_section_start_line(file_path, section_name)
#     if start_line is None:
#         return None
#     """
#     Procesa una sección del archivo de texto y extrae los datos de los años especificados.

#     :param file_path: Ruta al archivo de texto.
#     :param start_line: Número de línea donde comienza la sección.
#     :param end_year: Año final a incluir en los datos.
#     :param start_year: Año inicial a incluir en los datos.
#     :return: DataFrame con los datos de la sección.
#     """
#     data = []
#     with open(file_path, 'r', encoding='latin-1') as file:
#         for i, line in enumerate(file, start=1):
#             if i >= start_line:
#                 parts = line.split()
#                 if len(parts) >= 13:  # Asegurarse de que hay suficientes partes para un año completo
#                     try:
#                         year = int(parts[0])
#                         if start_year <= year <= end_year:
#                             monthly_values = parts[1:13]  # Enero a Diciembre
#                             data.append([year] + monthly_values)
#                     except ValueError:
#                         break

#     columns = ['Año', 'ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']
#     df = pd.DataFrame(data, columns=columns)
#     return df

# # Ruta al archivo de texto
# folder_path = './Estaciones_Grupo_1'  # Reemplaza con la ruta de tu carpeta  # Reemplaza con la ruta de tu archivo

# sections = ["EVAPORACION MEN", "LLUVIA TOTAL MEN", "TEMP MAXIMA PROM", "TEMP MINIMA PROM"]

# # Iterar sobre cada archivo en la carpeta
# for filename in os.listdir(folder_path):
#     if filename.endswith('.txt'):
#         file_path = os.path.join(folder_path, filename)
        
#         # Procesar cada sección en el archivo
#         for section in sections:
#             df = process_section(file_path, section)
#             if df is not None:
#                 # Base del nombre para los archivos CSV
#                 base_name = os.path.splitext(filename)[0]
#                 csv_filename = f'{base_name}_{section}.csv'.replace(" ", "_")
#                 df.to_csv(csv_filename, index=False)
