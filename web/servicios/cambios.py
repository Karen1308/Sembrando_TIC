import requests

from web.servicios import rest_api

def agregar_cambio(tipo, cambio, lugar):
    body = {"tipo": tipo,
                 "cambio": cambio,
                 "lugar": lugar}
    respuesta = requests.post(f'{rest_api.API_URL}/cambio', json=body)
    return respuesta

def lista_cambios():
    respuesta = requests.get(f'{rest_api.API_URL}/cambio')
    return respuesta.json()