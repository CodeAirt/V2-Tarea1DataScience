import pandas as pd

#Verificacion listado de estudiantes
def verificar_listado_notas(df_alumnos):

    def sanear_notas(notas):
        notas_limpias = []
        for nota in notas:
            try:
                valor = float(nota) #convierte a float
                valor = abs(valor) #convierte a positivo absoluto
                notas_limpias.append(valor) #agrega el valor a la lista

            except (ValueError, TypeError):
                continue #sino descarta el valor
        return notas_limpias
    
    df_alumnos['nota'] = df_alumnos['nota'].apply(sanear_notas) #sanea las notas

    df_filtrado = df_alumnos[df_alumnos['nota'].apply(lambda notas: len(notas) > 0)].copy()
    return df_filtrado