"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    ruta_archivo = "./files/input/tbl0.tsv" 
    tbl0 = pd.read_csv(ruta_archivo, sep="\t")
    cantidad_columnas = tbl0.shape[1]  

    return cantidad_columnas


if __name__ == "__main__":
    print(pregunta_02())
