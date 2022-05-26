import requests

from web.servicios import rest_api

# Validar datos al crear lugar #
def crear_lugar(correo, nombre, historia, lat_long, descripcion, actividades, caracteristicas):
    body = {"correo": correo,
                    "nombre": nombre,
                    "historia": historia,
                    "lat_long": lat_long,
                    "descripcion": descripcion,
                    "actividades": actividades,
                    "caracteristicas": caracteristicas}
    respuesta = requests.post(f'{rest_api.API_URL}/crear_lugar', json=body)
    return respuesta

# Validar datos al modificar lugar #
def modificar_lugar(id_lugar, nombre, historia, lat_long, descripcion, actividades, caracteristicas):
    body = {"id_lugar": id_lugar,
                    "nombre": nombre,
                    "historia": historia,
                    "lat_long": lat_long,
                    "descripcion": descripcion,
                    "actividades": actividades,
                    "caracteristicas": caracteristicas}
    respuesta = requests.put(f'{rest_api.API_URL}/lugar/{id_lugar}', json=body)
    return respuesta

#Eliminar lugar #
def eliminar_lugar(id_lugar):
    body = {"id_lugar": id_lugar}
    respuesta = requests.delete(f'{rest_api.API_URL}/lugares/{id_lugar}', json=body)
    return respuesta

# Obtener lugares # Con mas me gustas por hacer #
def obtener_lugares():
    respuesta = requests.get(f'{rest_api.API_URL}/lugares')
    return respuesta.json()

# Obtener lugar por id #
def lugar_por_id(id_lugar):
    respuesta = requests.get(f'{rest_api.API_URL}/lugar/{id_lugar}')
    return respuesta.json()

# Obtener lugar/es segun filtro #
def lugares_segun_filtro(filtro, valor):
    body = {"filtro": filtro,
                    "valor": valor}
    respuesta = requests.get(f'{rest_api.API_URL}/lugares/', json=body)
    return respuesta