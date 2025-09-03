from tarea1DataScience import df_alumnos
import numpy as np

# Porcentaje de estudiantes tiene al menos una nota bajo 4.0
estudiantes_nota_baja = df_alumnos['nota'].apply(lambda notas: np.any(np.array(notas) < 4.0)).sum()

porcentaje_nota_baja = (estudiantes_nota_baja / len(df_alumnos)) * 100

print(f"Porcentaje de estudiantes con al menos una nota bajo 4.0: {porcentaje_nota_baja:.2f}%")