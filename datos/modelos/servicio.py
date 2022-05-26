from datos.base_de_datos import BaseDeDatos

def crear_servicio(tipo, nom_servicio, lat_long, descripcion, direccion, tel_contacto, nom_contacto):
    crear_servicio_sql = f"""
             INSERT INTO SERVICIOS(TIPO, NOM_SERVICIO, LAT_LONG, DESCRIPCION, DIRECCION, TEL_CONTACTO, NOM_CONTACTO)
             VALUES ('{tipo}', UPPER('{nom_servicio}'), '{lat_long}', '{descripcion}', '{direccion}', '{tel_contacto}', '{nom_contacto}')
         """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_servicio_sql)

    obtener_id_servicio_sql = f""" SELECT MAX(ID_SERVICIO) FROM SERVICIOS"""
    resultado = bd.ejecutar_sql(obtener_id_servicio_sql)
    return resultado

def buscar_servicio(id_servicio):
    buscar_servicio_sql = f""" SELECT * FROM SERVICIOS WHERE ID_SERVICIO = '{id_servicio}' """
    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(buscar_servicio_sql)
    return resultado

def all_servicios_usuario(correo):
    buscar_servicio_sql = f""" 
    SELECT *,  (SELECT COUNT (CORREO) AS MG FROM LIKES WHERE ID_SERVICIO = S.ID_SERVICIO) AS MG
    FROM SERVICIOS AS S INNER JOIN SERVICIOS_USUARIOS AS US ON S.ID_SERVICIO = US.ID_SERVICIO 
    WHERE US.CORREO = '{correo}'  """

    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(buscar_servicio_sql)
    return resultado

def buscar_x_nom_servicio(nom_servicio):
    buscar_servicio_sql = f""" SELECT * FROM SERVICIOS WHERE NOM_SERVICIO LIKE UPPER('%{nom_servicio}%')"""
    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(buscar_servicio_sql)
    return resultado

def buscar_x_direccion(direccion):
    buscar_servicio_sql = f""" SELECT * FROM SERVICIOS WHERE DIRECCION LIKE '%{direccion}%' """
    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(buscar_servicio_sql)
    return resultado

def buscar_servicios_x_lugar(id_servicio, id_lugar):
    buscar_servicios_x_lugar_sql = f""" 
    SELECT S.TIPO, S.NOM_SERVICIO, S.LAT_LONG, S.DESCRIPCION, S.DIRECCION, S.TEL_CONTACTO,
    S.NOM_CONTACTO, L.NOMBRE, L.HISTORIA, L.LAT_LONG, L.DESCRIPCION, L.ACTIVIDADES, L.CARACTERISTICAS
    FROM SERVICIOS AS S, SERVICIOS_LUGARES AS SL, LUGARES AS L
    WHERE SL.ID_SERVICIO = S.ID_SERVICIO
    AND SL.ID_LUGAR = L.ID_LUGAR
    AND S.ID_SERVICIO = '{id_servicio}'
    AND L.ID_LUGAR = '{id_lugar}'"""
    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(buscar_servicios_x_lugar_sql)
    return resultado

def modificar_servicio(id_servicio, tipo, nom_servicio, lat_long, descripcion, direccion, tel_contacto, nom_contacto):
    modificar_servicio_sql = f""" 
    UPDATE SERVICIOS SET 
    TIPO = '{tipo}',
    NOM_SERVICIO = UPPER('{nom_servicio}'),
    LAT_LONG = '{lat_long}',
    DESCRIPCION = UPPER('{descripcion}'),
    DIRECCION = UPPER('{direccion}'),
    TEL_CONTACTO = '{tel_contacto}',
    NOM_CONTACTO = UPPER('{nom_contacto}')
    WHERE ID_SERVICIO = '{id_servicio}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_servicio_sql)

def eliminar_servicio(id_servicio):
    eliminar_servicio_sql = f""" DELETE FROM SERVICIOS WHERE ID_SERVICIO = '{id_servicio}' """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_servicio_sql)

def asociar_servicio_usuario(id_servicio, correo):
    asociar_servicio_usuario_sql = f""" INSERT INTO SERVICIOS_USUARIOS(ID_SERVICIO, CORREO) VALUES('{id_servicio}', '{correo}') """
    bd = BaseDeDatos()
    bd.ejecutar_sql(asociar_servicio_usuario_sql)

def eliminar_servicio_usuario(id_servicio):
    eliminar_servicio_usuario_sql = f""" DELETE FROM SERVICIOS_USUARIOS WHERE ID_SERVICIO = '{id_servicio}' """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_servicio_usuario_sql)

def asociar_servicio_lugar(id_servicio, id_lugar):
    asociar_servicio_lugar_sql = f""" INSERT INTO SERVICIOS_LUGARES(ID_SERVICIO, ID_LUGAR) VALUES('{id_servicio}', '{id_lugar}')"""
    bd = BaseDeDatos()
    bd.ejecutar_sql(asociar_servicio_lugar_sql)

def eliminar_servicio_lugar(id_servicio, id_lugar):
    eliminar_servicio_lugar_sql = f""" DELETE FROM SERVICIOS_LUGARES WHERE ID_SERVICIO = '{id_servicio}' AND ID_LUGAR = '{id_lugar}'  """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_servicio_lugar_sql)