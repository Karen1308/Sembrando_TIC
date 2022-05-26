from datos.base_de_datos import BaseDeDatos

############################################################
####################### LIKE LUGAR ##########################
############################################################
def nuevo_like_lugar(correo, id_lugar):
    nuevo_like_lugar_sql = f"""
            INSERT INTO LIKES(CORREO, ID_LUGAR, ID_SERVICIO)
            VALUES ('{correo}', '{id_lugar}', NULL)
        """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(nuevo_like_lugar_sql)

def eliminar_like_lugar(correo, id_lugar):
    eliminar_like_lugar_sql = f""" DELETE FROM LIKES WHERE CORREO = '{correo}' AND ID_LUGAR = '{id_lugar}' """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(eliminar_like_lugar_sql)

def existe_mg_lugar_usuario(correo, id_lugar):
    existe_mg_lugar_usuario_sql = f"""
            SELECT * FROM LIKES WHERE CORREO = '{correo}' AND ID_LUGAR = '{id_lugar}'
        """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(existe_mg_lugar_usuario_sql)

############################################################
####################### LIKE SERVICIO #######################
############################################################
def nuevo_like_servicio(correo, id_servicio):
    nuevo_like_servicio_sql = f"""
            INSERT INTO LIKES(CORREO, ID_LUGAR, ID_SERVICIO)
            VALUES ('{correo}',NULL,  '{id_servicio}')
        """
    bd = BaseDeDatos()
    bd.ejecutar_sql(nuevo_like_servicio_sql)

def eliminar_like_servicio(correo, id_servicio):
    eliminar_like_servicio_sql = f""" DELETE FROM LIKES WHERE CORREO = '{correo}' AND ID_SERVICIO = '{id_servicio}' """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_like_servicio_sql)