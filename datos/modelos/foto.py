from datos.base_de_datos import BaseDeDatos
bd = BaseDeDatos()

def crear_foto(fecha, foto):
    crear_foto_sql = f""" INSERT INTO FOTOS(FECHA, FOTO) 
        VALUES ('{fecha}','{foto}')
        """
    bd.ejecutar_sql(crear_foto_sql)

    obtener_id_foto_sql = f""" SELECT MAX(ID_FOTO) FROM FOTOS"""
    resultado = bd.ejecutar_sql(obtener_id_foto_sql)
    return resultado

def buscar_foto(id_foto):
    buscar_foto_sql = f""" SELECT * FROM FOTOS WHERE ID_FOTO = '{id_foto}' """
    resultado = bd.ejecutar_sql(buscar_foto_sql)
    return resultado

def buscar_fotos():
    buscar_foto_sql = f""" SELECT * FROM FOTOS"""
    resultado = bd.ejecutar_sql(buscar_foto_sql)
    return resultado

def eliminar_foto(id_foto):
    eliminar_foto_sql = f""" DELETE FROM FOTOS WHERE ID_FOTO = '{id_foto}' """
    bd.ejecutar_sql(eliminar_foto_sql)

def asociar_foto_lugar(id_foto, id_lugar):
    asociar_foto_lugar_sql = f""" INSERT INTO FOTOS_LUGARES (ID_LUGAR, ID_FOTO) VALUES ('{id_lugar}', '{id_foto}') """
    bd.ejecutar_sql(asociar_foto_lugar_sql)

def eliminar_foto_lugar(id_foto):
    eliminar_foto_lugar_sql = f""" DELETE FROM  FOTOS_LUGARES WHERE ID_FOTO = '{id_foto}' """
    bd.ejecutar_sql(eliminar_foto_lugar_sql)

def lugar_segun_foto(id_foto):
    foto_segun_lugar_sql = f""" 
    SELECT F.ID_FOTO, L.ID_LUGAR, L.NOMBRE
    FROM FOTOS AS F, FOTOS_LUGARES  AS FL, LUGARES AS L
    WHERE FL.ID_FOTO = F.ID_FOTO
    AND FL.ID_LUGAR = L.ID_LUGAR
    AND F.ID_FOTO = '{id_foto}' """
    resultado = bd.ejecutar_sql(foto_segun_lugar_sql)
    return resultado