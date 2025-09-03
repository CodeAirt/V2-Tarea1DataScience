from tarea1DataScience import df_alumnos
import numpy as np

# 1.-Calculo de promedios de notas de cada estudiante
df_alumnos['promedio'] = df_alumnos['nota'].apply(np.mean).round(1)

# Encontrar el promedio más alto y más bajo
promedio_max = df_alumnos['promedio'].max()
promedio_min = df_alumnos['promedio'].min()

#Print de resultados
print("\nListado de estudiantes con sus promedios:")
print(df_alumnos)
print(f"El promedio más alto es: {promedio_max}")
print(f"El promedio más bajo es: {promedio_min}")
