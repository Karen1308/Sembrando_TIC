from datos.base_de_datos import BaseDeDatos

def crear_lugar(nombre, historia, lat_long, descripcion, actividades, caracteristicas):
    crear_lugar_sql = f"""
            INSERT INTO LUGARES (NOMBRE, HISTORIA, LAT_LONG, DESCRIPCION, ACTIVIDADES, CARACTERISTICAS)
            VALUES (UPPER('{nombre}'), '{historia}', '{lat_long}', '{descripcion}', '{actividades}', '{caracteristicas}')
        """

    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_lugar_sql)

    ultimo_lugar_ingresado_sql = f"""  SELECT MAX(ID_LUGAR) FROM LUGARES"""
    resultado = bd.ejecutar_sql(ultimo_lugar_ingresado_sql)
    return resultado

def asociar_lugar_usuario(id_lugar, correo):
    asociar_lugar_usuario_sql = f""" INSERT INTO LUGARES_USUARIOS (ID_LUGAR, CORREO) VALUES ('{id_lugar}' , '{correo}' ) """

    bd = BaseDeDatos()
    bd.ejecutar_sql(asociar_lugar_usuario_sql)

def modificar_lugar(id_lugar, nombre, historia, lat_long, descripcion, actividades, caracteristicas):
    modificar_lugar_sql = f""" 
    UPDATE LUGARES SET
    NOMBRE = '{nombre}', 
    HISTORIA = '{historia}',
    LAT_LONG = '{lat_long}',
    DESCRIPCION = '{descripcion}',
    ACTIVIDADES = '{actividades}',
    CARACTERISTICAS = '{caracteristicas}'
    WHERE ID_LUGAR = '{id_lugar}' """

    bd = BaseDeDatos()
    return bd.ejecutar_sql(modificar_lugar_sql)

def eliminar_lugar(id_lugar):
    eliminar_lugar_sql = f""" DELETE FROM LUGARES WHERE ID_LUGAR = '{id_lugar}' """

    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_lugar_sql)

def eliminar_lugar_usuario(id_lugar):
    eliminar_lugar_usuario_sql = f""" DELETE FROM LUGARES_USUARIOS WHERE ID_LUGAR = '{id_lugar}' """

    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_lugar_usuario_sql)

def eliminar_lugar_cambio(id_lugar):
    eliminar_lugar_cambio_sql = f""" DELETE FROM CAMBIO WHERE LUGAR = '{id_lugar}' """

    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_lugar_cambio_sql)

def buscar_x_id(id_lugar):
    buscar_x_id_sql = f""" SELECT * FROM LUGARES WHERE ID_LUGAR = '{id_lugar}' """

    bd = BaseDeDatos()
    return [{"nombre": resultado[1],
                "historia": resultado[2],
                "lat_long": resultado[3],
                "descripcion": resultado[4],
                "actividades": resultado[5],
                "caracteristicas": resultado[6]} for resultado in bd.ejecutar_sql(buscar_x_id_sql)]

def all_lugares():
    buscar_lugares_sql = f""" SELECT *, (SELECT COUNT (CORREO) AS MG FROM LIKES WHERE ID_LUGAR = LUGARES.ID_LUGAR) AS MG FROM LUGARES """

    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(buscar_lugares_sql)
    return resultado

def buscar_x_nom_lugar(nombre):
    buscar_x_nom_lugares_sql = f""" SELECT *, (SELECT COUNT (CORREO) AS MG FROM LIKES WHERE ID_LUGAR = LUGARES.ID_LUGAR) AS MG FROM LUGARES WHERE NOMBRE LIKE UPPER('%{nombre}%') """

    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(buscar_x_nom_lugares_sql)
    return resultado

def buscar_x_caracteristica(caracteristica):
    buscar_x_caracteristica_sql = f""" SELECT *, (SELECT COUNT (CORREO) AS MG FROM LIKES WHERE ID_LUGAR = LUGARES.ID_LUGAR) AS MG FROM LUGARES WHERE CARACTERISTICAS LIKE  '%{caracteristica}%' """

    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(buscar_x_caracteristica_sql)
    return resultado

def buscar_x_actividad(actividad):
    buscar_x_actividad_sql = f""" SELECT *, (SELECT COUNT (CORREO) AS MG FROM LIKES WHERE ID_LUGAR = LUGARES.ID_LUGAR) AS MG FROM LUGARES WHERE ACTIVIDADES LIKE  '%{actividad}%' """

    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(buscar_x_actividad_sql)
    return resultado

##################################################
def lugar_segun_servicio(id_servicio):
    lugar_segun_servicio_sql = f""" 
    SELECT L.ID_LUGAR, L.NOMBRE, S.ID_SERVICIO, S.NOM_SERVICIO
    FROM LUGARES AS L, SERVICIOS_LUGARES AS SL, SERVICIOS AS S
    WHERE L.ID_LUGAR = SL.ID_LUGAR
    AND S.ID_SERVICIO = SL.ID_SERVICIO
    AND S.ID_SERVICIO = '{id_servicio}' """

    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(lugar_segun_servicio_sql)
    return resultado