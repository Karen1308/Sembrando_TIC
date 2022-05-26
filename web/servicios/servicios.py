import requests

from web.servicios import rest_api

# Validar datos al crear servicio #
def crear_servicio(correo, tipo, nom_servicio, lat_long, descripcion, direccion, tel_contacto, nom_contacto, recomendado):
    body = {"correo": correo,
            "tipo": tipo,
            "nom_servicio": nom_servicio,
            "lat_long": lat_long,
            "descripcion": descripcion,
            "direccion": direccion,
            "tel_contacto": tel_contacto,
            "nom_contacto": nom_contacto,
            "recomendado": recomendado}
    respuesta = requests.post(f'{rest_api.API_URL}/servicio', json=body)
    return respuesta

# Obtener servicios del usuario ingresado #
def obtener_servicios_usuario(correo):
    respuesta = requests.get(f'{rest_api.API_URL}/servicios/{correo}')
    return respuesta
