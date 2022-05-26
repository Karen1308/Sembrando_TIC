import requests

from web.servicios import rest_api

# Validar si ya existe el me gusta #
def existe_mg(correo, id_lugar):
    body = {"correo": correo,
                    "id_lugar": id_lugar}
    respuesta = requests.get(f'{rest_api.API_URL}/lugar/mg', json=body)
    return respuesta

# Agregando el me gusta #
def agregar_mg(correo, id_lugar):
    body = {"correo": correo,
                 "id_lugar": id_lugar}
    respuesta = requests.post(f'{rest_api.API_URL}/lugar/mg', json=body)
    return respuesta

# Eliminando el me gusta #
def eliminar_mg(correo, id_lugar):
    body = {"correo": correo,
                 "id_lugar": id_lugar}
    respuesta = requests.delete(f'{rest_api.API_URL}/lugar/mg', json=body)
    return respuesta