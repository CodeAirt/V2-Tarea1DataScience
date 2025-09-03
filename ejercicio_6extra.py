from ejercicio_1 import df_alumnos
import pandas as pd

# Promedio total del curso
promedio_curso = df_alumnos['promedio'].mean().round(1)

print(f"El promedio total del curso es: {promedio_curso}")