from tarea1DataScience import df_alumnos
import numpy as np
import pandas as pd

# La nota mas frecuente
nota_frecuente = df_alumnos['nota'].explode().mode()[0] # .explode separa las notas en una sola columna .mode entrega la nota que mas se repite y [0] toma el primer valor en caso de empate

print(f"La nota más frecuente entre todos los estudiantes es: {nota_frecuente}")