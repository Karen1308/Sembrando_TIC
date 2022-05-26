from datos.modelos import servicio as modelo_servicio

key_list = ['id_servicio', 'tipo', 'nom_servicio', 'lat_long', 'descripcion', 'direccion', 'tel_contacto', 'nom_contacto']

def crear_servicio(tipo, nom_servicio, lat_long, descripcion, direccion, tel_contacto, nom_contacto):
    resultado = modelo_servicio.crear_servicio(tipo, nom_servicio, lat_long, descripcion, direccion, tel_contacto, nom_contacto)
    return resultado

def buscar_servicio(id_servicio):
    resultado = modelo_servicio.buscar_servicio(id_servicio)
    valores_lista = resultado
    diccionario = {}
    contador = 0
    for keys in key_list:
        for values in valores_lista:
            diccionario[keys] = values[contador]
            contador = contador+1
    return diccionario

def all_servicios_usuario(correo):
    resultado = modelo_servicio.all_servicios_usuario(correo)
    return resultado

def buscar_x_nom_servicio(nom_servicio):
    resultado = modelo_servicio.buscar_x_nom_servicio(nom_servicio)
    return resultado

def buscar_x_direccion(direccion):
    resultado = modelo_servicio.buscar_x_direccion(direccion)
    return resultado

def buscar_servicios_x_lugar(id_servicio, id_lugar):
    resultado = modelo_servicio.buscar_servicios_x_lugar(id_servicio, id_lugar)
    return resultado

def modificar_servicio(id_servicio, tipo, nom_servicio, lat_long, descripcion, direccion, tel_contacto, nom_contacto):
    modelo_servicio.modificar_servicio(id_servicio, tipo, nom_servicio, lat_long, descripcion, direccion, tel_contacto, nom_contacto)

def eliminar_servicio(id_servicio):
    modelo_servicio.eliminar_servicio(id_servicio)

def asociar_servicio_usuario(id_servicio, correo):
    modelo_servicio.asociar_servicio_usuario(id_servicio, correo)

def eliminar_servicio_usuario(id_servicio):
    modelo_servicio.eliminar_servicio_usuario(id_servicio)

def asociar_servicio_lugar(id_servicio, id_lugar):
    modelo_servicio.asociar_servicio_lugar(id_servicio, id_lugar)

def eliminar_servicio_lugar(id_servicio, id_lugar):
    modelo_servicio.eliminar_servicio_lugar(id_servicio, id_lugar)