import pandas as pd
import matplotlib.pyplot as plt
import io

# Datos proporcionados
data = """ANIO ENE FEB MAR ABR MAY JUN JUL AGO SEP OCT NOV DIC ACUMULADO MEDIA MESES
                         1998 -      -      -      -      -      101    88.7   281.5  85.8   73.9   -      -        630.9     126.2  5
                         1999 0      0      0      0      0      41.1   215.1  66.5   -      -      0      -        322.7      35.9  9
                         2000 0      -      -      -      -      -      93.5   147    55     47     3.5    40       386.0      55.1  7
                         2001 0      0      3      31     43     133.5  86.2   110.9  182.8  12.3   8.5    3.2      614.4      51.2 12
                         2002 18     30.3   -      26.9   53     60.5   285.5  158.6  112.2  92.5   42     -        879.5      73.3 12
                         2003 10     2      -      0.2    21.2   150.2  221.4  114.3  124.9  43.4   3.5    -        691.1      57.6 12
                         2004 68.6   7.5    43.9   1      64.2   285.8  105.8  142.8  176.2  27.1   11     -        933.9      77.8 12
                         2005 0      70.5   30.5   -      16     0.8    197.7  166.7  105.5  17.3   12     6        623.0      51.9 12
                         2006 3      -      -      -      86.6   71.9   121    129.7  161.5  120.9  23.2   27       744.8      62.1 12
                         2007 41.6   17.2   -      8.5    14.5   281.2  180.5  102.4  40.2   5.4    14.5   3        709.0      59.1 12
                         2008 0      7      1      19.7   12     60.5   339.7  252.7  88.1   6.5    0      -        787.2      65.6 12
                         2009 1      -      1.5    3      39     210.5  52.5   183    179.1  77.7   2      75.2     824.5      68.7 12
                         2010 -      158    -      -      -      65.2   231.6  114    133.2  2      -      -        704.0      64.0 11
                         2011 1      -      2.3    -      17     129.11 45     73.1   113.5  28     5.5    -        414.5      34.5 12
                         2012 17     67.4   1      -      13     56.4   182.7  133.2  59.3   11     1.4    20       562.4      46.9 12
                         2013 62.7   -      -      -      18     80.3   225.5  110.2  197.9  78.9   56.1   124.4    954.0      79.5 12
                         2014 9      -      2      1      81.4   219    186    133.5  150.9  44.2   30.8   30       887.8      74.0 12
                         2015 -      38.3   137.6  5.8    25.8   275.3  121.5  250.8  63.5   202.5  25     55.3    1201.4     109.2 11
                         2016 3.2    9      40     1      14     78     244    176.3  51     14     41.4   4        675.9      56.3 12
                         2017 2      4.5    16     -      5      80.6   159.2  160.3  164.7  31.8   0      55       679.1      56.6 12
                         2018 71.2   35     -      20     50.5   258.8  43     77.5   192    136.3  39.5   18       941.8      78.5 12
                         2019 11.5   -      4      -      4      -      150    171    -      123.7  63.4   18.3     545.9      68.2  8
                         2020 60.5   -      17.5   6.5    18.8   117.8  188.7  82.5   113.9  2      -      30.4     638.6      58.1 11
                         2021 15     0      -      6.5    48     195.1  218.2  143    260.2  28     -      -        914.0     101.6  9"""

# Crear un DataFrame a partir de los datos
df = pd.read_csv(io.StringIO(data), delim_whitespace=True)
df = df.replace("-", float("nan"))  # Reemplaza "-" con NaN

df.to_excel("datos.xlsx", index=False)
df = pd.read_excel("datos.xlsx")

# Transponer el DataFrame para que los meses estén en el índice
df = df.T

# Definir los meses como etiquetas en el eje X
meses = df.index[1:13]

print(len(df.columns))

# Crear una gráfica de líneas con marcadores para cada año
plt.figure(figsize=(12, 8))
for i in range(1, len(df.columns)):
    if df.columns[i] == 18:  # Niña 2015
        plt.plot(
            meses, df.iloc[1:13, i], marker="o", label=str(df.columns[i]), color="red"
        )
    elif df.columns[i] == 13:  # Niño 2010
        plt.plot(
            meses,
            df.iloc[1:13, i],
            marker="o",
            label=str(df.columns[i]),
            color="orange",
        )
    else:
        plt.plot(
            meses, df.iloc[1:13, i], marker="o", label=str(df.columns[i]), color="blue"
        )
        
        ## Verificar cuantos años hay por estacion
        ## Febrero, Junio, Octubre - 4 parametros = precipitacion, tmax, tmin, evaporacion POR CADA ESTACION filas estacionciones col, tmaxM tminM evaM precM por cada mes

plt.title("Precipitación Mensual por Año 1968 - 2021")
plt.xlabel("Meses")
plt.ylabel("Precipitación")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
