from datetime import datetime

from datos.modelos import cambios as modelo_cambio

def agregar_cambio(tipo, cambio, lugar):
    hora_actual = datetime.now()
    fecha = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    resultado = modelo_cambio.agregar_cambio(tipo, cambio, fecha, lugar)
    return resultado

def listar_cambios():
    resultado = modelo_cambio.listar_cambios()
    return resultado