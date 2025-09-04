from ejercicio_1 import df_alumnos
import pandas as pd

# Listado ordenado de estudiantes segun su promedio
df_ordenado = df_alumnos.sort_values(by='promedio', ascending=False).reset_index(drop=True) #reset index resetea el indice para que empiece en 0 y no mantenga el indice original

print("\nListado de estudiantes ordenados por su promedio (de mayor a menor):")
print(df_ordenado)