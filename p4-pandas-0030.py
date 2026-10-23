import pandas as pd
import numpy as np
# Cepeda Darrell NC = 0030
# Fecha 23/10/2026
n_filas=5
n_columnas=5
tag_columna=tuple("ABCDE") # etiquetas para las columnas
print(tag_columna)
matriz=np.random.randint(1, 6, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("Con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la variable df es DataFrame
df = pd.DataFrame(matriz, columns= tag_columna)
print("--- La tabla o DataFrame ---NC = 0030")
print(df)
print("------- Programa ejecutado por Cepeda Darrell NC = 0030 -------")