from datos.modelos import foto as modelo_foto

key_list = ['id_foto', 'id_lugar', 'nom_lugar']

def crear_foto(fecha, foto):
    resultado = modelo_foto.crear_foto(fecha, foto)
    return resultado

def buscar_foto(id_foto):
    resultado = modelo_foto.buscar_foto(id_foto)
    return resultado

def buscar_fotos():
    resultado = modelo_foto.buscar_fotos()
    return resultado

def eliminar_foto(id_foto):
    modelo_foto.eliminar_foto(id_foto)

def asociar_foto_lugar(id_foto, id_lugar):
    modelo_foto.asociar_foto_lugar(id_foto, id_lugar)

def eliminar_foto_lugar(id_foto):
    modelo_foto.eliminar_foto_lugar(id_foto)

def lugar_segun_foto(id_foto):
    resultado = modelo_foto.lugar_segun_foto(id_foto)
    valores_lista = resultado
    diccionario = {}
    contador = 0
    for keys in key_list:
        for values in valores_lista:
            diccionario[keys] = values[contador]
            contador = contador+1
    return diccionario