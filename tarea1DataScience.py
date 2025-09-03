import pandas as pd

# Crea un DataFrame desde un diccionario
estudiantes = [
    {"nombre": "Juan", "nota": [5.7, 6.0, 7.0]},
    {"nombre": "Ana", "nota": [4.0, 5.0, 6.0]},
    {"nombre": "Pedro", "nota": [3.0, 5.0, 4.5]},
    {"nombre": "Lucía", "nota": [6.3, 6.8, 7.0]},
    {"nombre": "Carlos", "nota": [4.5, 4.8, 5.2]},
    {"nombre": "María", "nota": [5.9, 6.1, 6.7]},
    {"nombre": "Andrés", "nota": [3.5, 4.0, 4.2]},
    {"nombre": "Sofía", "nota": [6.9, 6.5, 6.8]},
    {"nombre": "Daniel", "nota": [5.0, 5.5, 6.0]},
    {"nombre": "Valentina", "nota": [6.0, 6.3, 6.5]},
    {"nombre": "Luis", "nota": [2.5, 3.0, 4.0]},
    {"nombre": "Camila", "nota": [6.2, 6.5, 7.0]},
    {"nombre": "Javier", "nota": [4.0, 4.5, 4.8]},
    {"nombre": "Martina", "nota": [5.5, 5.8, 6.0]},
    {"nombre": "Felipe", "nota": [3.8, 4.1, 4.5]},
    {"nombre": "Antonia", "nota": [6.6, 6.7, 6.9]},
    {"nombre": "Tomás", "nota": [5.1, 5.4, 5.6]},
    {"nombre": "Isidora", "nota": [6.0, 6.2, 6.4]},
    {"nombre": "Mateo", "nota": [4.2, 4.5, 5.0]},
    {"nombre": "Emilia", "nota": [6.7, 6.9, 7.0]},
    {"nombre": "Diego", "nota": [3.7, 4.0, 4.3]},
    {"nombre": "Josefa", "nota": [5.8, 6.0, 6.2]},
    {"nombre": "Benjamín", "nota": [2.8, 3.2, 3.6]},
    {"nombre": "Florencia", "nota": [6.5, 6.7, 6.8]},
    {"nombre": "Agustín", "nota": [4.9, 5.1, 5.4]},
    {"nombre": "Renata", "nota": [5.6, 5.9, 6.0]},
    {"nombre": "Sebastián", "nota": [3.5, 3.9, 4.2]},
    {"nombre": "Trinidad", "nota": [6.3, 6.6, 6.9]},
    {"nombre": "Maximiliano", "nota": [4.0, 4.2, 4.5]},
    {"nombre": "Amanda", "nota": [6.1, 2.0, 6.6]},
]

df_alumnos = pd.DataFrame(estudiantes)