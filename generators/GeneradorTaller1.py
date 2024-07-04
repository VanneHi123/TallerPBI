import random

def GeneradorTaller1():
    Productos=["Música","TV","Aplicaciones","PC","Celulares","Tablets","Accesorios"]
    datos=[]
    for Producto in Productos:
        TipoProducto={}
        categoria=random.choice(["Plus","Mega","Basic"])
        TipoProducto=[Producto,categoria]
        datos.append(TipoProducto)
    return datos 

print(GeneradorTaller1())
