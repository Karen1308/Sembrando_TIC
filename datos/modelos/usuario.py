from datos.base_de_datos import BaseDeDatos

def crear_usuario(correo, password, nombre, apellido, tipo):
    crear_usuario_sql = f""" INSERT INTO USUARIOS(CORREO, PASSWORD, NOMBRE, APELLIDO, TIPO, ESTADO, FECHA_INACTIVO) VALUES ('{correo}', '{password}', '{nombre}', '{apellido}', '{tipo}', true,NULL) """

    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)

def crear_sesion(correo, datetime_ingreso):
    crear_sesion_sql = f''' INSERT INTO SESIONES (CORREO, FECHA_HORA) VALUES ('{correo}', '{datetime_ingreso}')'''

    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)

def obtener_ultima_sesion(correo):
    obtener_sesion_sql= f''' SELECT MAX(ID) , FECHA_HORA FROM SESIONES WHERE CORREO = '{correo}' '''

    bd = BaseDeDatos()
    return [{"id_sesion": resultado[0],
                "fecha_hora": resultado[1]} for resultado in bd.ejecutar_sql(obtener_sesion_sql)]

def login(correo):
    buscar_usuario_sql = f""" SELECT * FROM USUARIOS WHERE CORREO = '{correo}' """

    bd = BaseDeDatos()
    return [{"correo": resultado[0],
                "password": resultado[1],
                "nombre": resultado[2],
                "apellido": resultado[3],
                "tipo": resultado[4],
                "estado": resultado[5],
                "fecha_inactivo": resultado[6]
             } for resultado in bd.ejecutar_sql(buscar_usuario_sql)]

def activar_cuenta(correo):
    activar_cuenta_sql = f""" UPDATE USUARIOS SET ESTADO = 1, FECHA_INACTIVO = NULL WHERE CORREO = '{correo}' """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(activar_cuenta_sql)

def buscar_usuario(correo):
    buscar_usuario_sql = f""" SELECT * FROM USUARIOS WHERE CORREO = '{correo}' """

    bd = BaseDeDatos()
    return [{"correo": resultado[0],
                "password": resultado[1],
                "nombre": resultado[2],
                "apellido": resultado[3],
                "tipo": resultado[4],
             } for resultado in bd.ejecutar_sql(buscar_usuario_sql)]


def modificar_usuario(correo, password, nombre, apellido, tipo):
    modificar_usuario_sql = f""" 
    UPDATE USUARIOS SET 
    PASSWORD = UPPER('{password}'), 
    NOMBRE = UPPER('{nombre}'),
    APELLIDO = UPPER('{apellido}'),
    TIPO = '{tipo}'
    WHERE CORREO = '{correo}' """

    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)

def desactivar_cuenta(correo, datetime_ingreso):
    desactivar_cuenta_sql = f""" UPDATE USUARIOS SET ESTADO = 0, FECHA_INACTIVO = '{datetime_ingreso}' WHERE CORREO = '{correo}' """

    bd = BaseDeDatos()
    return bd.ejecutar_sql(desactivar_cuenta_sql)
