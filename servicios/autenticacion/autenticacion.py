from datos.modelos import usuario as modelo_usuario

def crear_usuario(correo, password, nombre, apellido, tipo):
    modelo_usuario.crear_usuario(correo, password, nombre, apellido, tipo)