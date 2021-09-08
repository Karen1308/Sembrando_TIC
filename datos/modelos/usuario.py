from datos.base_de_datos import BaseDeDatos


def crear_usuario(correo, password, nombre, apellido, tipo):
    crear_usuario_sql = f"""
        INSERT INTO USUARIOS(CORREO, PASSWORD, NOMBRE, APELLIDO, TIPO)
        VALUES ('{correo}', '{password}', '{nombre}', '{apellido}', '{tipo}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)