from generators.GeneradorTaller1 import GeneradorTaller1
import pandas as pd

def analizarDatos():
    datos=GeneradorTaller1()
    tabla=pd.DataFrame(datos,columns=["Producto","categoria"])
    tabla.to_csv("./data/AnalisisTaller.csv",index=False)
analizarDatos()