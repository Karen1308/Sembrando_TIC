from datos.base_de_datos import BaseDeDatos


############################################################
################ CAMBIOS - SUGERENCIAS #####################
############################################################
def agregar_cambio(tipo, cambio, fecha, lugar):
    ingreso_cambio_sql = f''' INSERT INTO CAMBIOS (TIPO, CAMBIO, FECHA, LUGAR)
                                                VALUES ('{tipo}', '{cambio}', '{fecha}', '{lugar}') '''
    bd = BaseDeDatos()
    return bd.ejecutar_sql(ingreso_cambio_sql)


def listar_cambios():
    # listar_cambios_sql = f""" SELECT * FROM CAMBIOS, LUGARES WHERE CAMBIOS.LUGAR = LUGARES.ID_LUGAR """
    listar_cambios_sql = f""" SELECT *, 
        (SELECT ID_LUGAR FROM LUGARES WHERE ID_LUGAR=CAMBIOS.LUGAR) AS ID_LUGAR,
        (SELECT NOMBRE FROM LUGARES WHERE ID_LUGAR=CAMBIOS.LUGAR) AS NOMBRE,
        (SELECT HISTORIA FROM LUGARES WHERE ID_LUGAR=CAMBIOS.LUGAR) AS HISTORIA, 
        (SELECT LAT_LONG FROM LUGARES WHERE ID_LUGAR=CAMBIOS.LUGAR) AS LAT_LONG, 
        (SELECT DESCRIPCION FROM LUGARES WHERE ID_LUGAR=CAMBIOS.LUGAR) AS DESCRIPCION, 
        (SELECT ACTIVIDADES FROM LUGARES WHERE ID_LUGAR=CAMBIOS.LUGAR) AS ACTIVIDADES, 
        (SELECT CARACTERISTICAS FROM LUGARES WHERE ID_LUGAR=CAMBIOS.LUGAR) AS CARACTERISTICAS
        FROM CAMBIOS """

    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(listar_cambios_sql)
    return resultado
