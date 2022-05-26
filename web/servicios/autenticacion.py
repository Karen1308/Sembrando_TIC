import requests
from flask import jsonify

from web.servicios import rest_api

# Validar datos del ingreso de usuario #
def validar_usuario(correo, password):
    body = {"correo": correo,
                "password": password}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta

# Validar datos del registro de usuario #
def registro(correo, password, nombre, apellido, tipo):
    body = {"correo": correo,
                "password": password,
                "nombre": nombre,
                "apellido": apellido,
                "tipo": tipo}
    respuesta = requests.post(f'{rest_api.API_URL}/registro', json=body)
    return respuesta

# Activar usuario inactivo #
def activar_usuario(correo):
    body = {"correo": correo}
    respuesta = requests.post(f'{rest_api.API_URL}/activar', json=body)
    return respuesta

# Desactivar cuenta de usuario #
def desactivar_cuenta(correo):
    respuesta = requests.put(f'{rest_api.API_URL}/desactivar/{correo}')
    return respuesta

###################################################
################# POR HACER ######################
# Validar datos de la modificación de datos del usuario #
def modificar_usuario(correo, password, nombre, apellido, tipo):
    body = {"correo": correo,
                "password": password,
                "nombre": nombre,
                "apellido": apellido,
                "tipo": tipo}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios/<correo>', json=body)
    return respuesta.status_code == 200

