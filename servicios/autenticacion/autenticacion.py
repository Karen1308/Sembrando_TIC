from datetime import datetime

from datos.modelos import usuario as modelo_usuario

#Comprobando existencia #
def existe_usuario(correo):
    usuarios = modelo_usuario.buscar_usuario(correo)
    return not len(usuarios) == 0

# Crear el usuario #
def crear_usuario(correo, password, nombre, apellido, tipo):
    if not existe_usuario(correo):
        modelo_usuario.crear_usuario(correo, password, nombre, apellido, tipo)
    else:
        raise Exception("El usuario ya existe")

# Login del usuario #
def login(correo):
    if existe_usuario(correo):
        usuario = modelo_usuario.login(correo)[0]
        return usuario
    else:
        raise Exception("El usuario no existe")

# Sesion de usuario #
def crear_sesion(correo):
    hora_actual = datetime.now()
    datetime_ingreso = hora_actual.strftime("%d/%m/%Y %H:%M:%S")

    # Valido que no exista una vigente aun #
    try:
        sesion = modelo_usuario.obtener_ultima_sesion(correo)[0]
        id_sesion = sesion['id_sesion']
        fecha_hora = sesion['fecha_hora']

        if not validar_sesion(id_sesion, fecha_hora):
            modelo_usuario.crear_sesion(correo, datetime_ingreso)
            sesion = modelo_usuario.obtener_ultima_sesion(correo)[0]
            return sesion
        else:
            return sesion
    except Exception:
        modelo_usuario.crear_sesion(correo, datetime_ingreso)
        sesion = modelo_usuario.obtener_ultima_sesion(correo)[0]
        return sesion

# Validando sesion #
def validar_sesion(id_sesion, fecha_hora):
    if str(id_sesion) == "None":
        return False
    elif (datetime.now() - datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M:%S")).total_seconds() > 3600:
        # Sesion expirada
        return False
    else:
        return True

# Activando cuenta #
def activar_cuenta(correo):
    usuario = modelo_usuario.activar_cuenta(correo)
    return usuario

def buscar_usuario(correo):
    usuario = modelo_usuario.buscar_usuario(correo)[0]
    return usuario

def modificar_usuario(correo, password, nombre, apellido, tipo):
    modelo_usuario.modificar_usuario(correo, password, nombre, apellido, tipo)

def desactivar_cuenta(correo):
    hora_actual = datetime.now()
    datetime_ingreso = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    usuario = modelo_usuario.desactivar_cuenta(correo, datetime_ingreso)
    return usuario