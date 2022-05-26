from datos.modelos import lugar as modelo_lugar

def crear_lugar(nombre, historia, lat_long, descripcion, actividades, caracteristicas) -> object:
    resultado = modelo_lugar.crear_lugar(nombre, historia, lat_long, descripcion, actividades, caracteristicas)
    return resultado

def asociar_lugar_usuario(id_lugar, correo):
    modelo_lugar.asociar_lugar_usuario(id_lugar, correo)

def modificar_lugar(id_lugar, nombre, historia, lat_long, descripcion, actividades, caracteristicas):
    resultado = modelo_lugar.modificar_lugar(id_lugar, nombre, historia, lat_long, descripcion, actividades, caracteristicas)
    return resultado

def eliminar_lugar(id_lugar):
    modelo_lugar.eliminar_lugar(id_lugar)

def eliminar_lugar_usuario(id_lugar):
    modelo_lugar.eliminar_lugar_usuario(id_lugar)

def eliminar_lugar_cambio(id_lugar):
    modelo_lugar.eliminar_lugar_cambio(id_lugar)

def all_lugares():
    resultado = modelo_lugar.all_lugares()
    return resultado

def buscar_x_id(id_lugar):
    resultado = modelo_lugar.buscar_x_id(id_lugar)
    return resultado

def buscar_x_nom_lugar(nombre):
    resultado = modelo_lugar.buscar_x_nom_lugar(nombre)
    return resultado

def buscar_x_actividad(actividad):
    resultado = modelo_lugar.buscar_x_actividad(actividad)
    return resultado

def buscar_x_caracteristica(caracteristicas):
    resultado = modelo_lugar.buscar_x_caracteristica(caracteristicas)
    return resultado

def lugar_segun_servicio(id_servicio):
    resultado = modelo_lugar.lugar_segun_servicio(id_servicio)
    return resultado