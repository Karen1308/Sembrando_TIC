from datos.modelos import like as modelo_likes

def nuevo_like_lugar(correo, id_lugar):
    resultado = modelo_likes.nuevo_like_lugar(correo, id_lugar)
    return resultado

def eliminar_like_lugar(correo, id_lugar):
    resultado = modelo_likes.eliminar_like_lugar(correo, id_lugar)
    return resultado

def existe_mg_lugar_usuario(correo, id_lugar):
    resultado = modelo_likes.existe_mg_lugar_usuario(correo, id_lugar)
    return resultado

#######################################
#######################################
def nuevo_like_servicio(correo, id_servicio):
    resultado = modelo_likes.nuevo_like_servicio(correo, id_servicio)
    return resultado

def eliminar_like_servicio(correo, id_servicio):
    resultado = modelo_likes.eliminar_like_servicio(correo, id_servicio)
    return resultado