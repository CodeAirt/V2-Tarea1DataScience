from tarea1DataScience import df_alumnos
import numpy as np

# Cuantos estudiantes aprobaron todas sus notas
cantidad_aprobados = df_alumnos['nota'].apply(lambda notas: np.all(np.array(notas) >= 4.0)).sum()

print(f"Cantidad de estudiantes que aprobaron todas sus notas: {cantidad_aprobados}")