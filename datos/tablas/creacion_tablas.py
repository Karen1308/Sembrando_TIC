import sqlite3

sql_tabla_lugares = '''CREATE TABLE LUGARES ( 
                    ID_LUGAR INTEGER PRIMARY KEY AUTOINCREMENT,  
                    NOMBRE STRING NOT NULL, 
                    HISTORIA STRING NOT NULL, 
                    LAT_LONG STRING, 
                    DESCRIPCION STRING, 
                    ACTIVIDADES STRING, 
                    CARACTERISTICAS STRING) '''

sql_tabla_fotos = '''CREATE TABLE FOTOS(
                 ID_FOTO INTEGER PRIMARY KEY AUTOINCREMENT,
                 FOTO STRING NOT NULL,
                 FECHA DATE)'''

sql_tabla_lugares_fotos = '''CREATE TABLE FOTOS_LUGARES( 
                 ID_LUGAR INTEGER NOT NULL,
                 ID_FOTO INTEGER NOT NULL,
                 CONSTRAINT PK_LUGARES_FOTOS PRIMARY KEY(ID_LUGAR, ID_FOTO),
                 CONSTRAINT FK_LUGARES FOREIGN KEY(ID_LUGAR) REFERENCES LUGARES(ID_LUGAR),
                 CONSTRAINT FK_FOTOS FOREIGN KEY(ID_FOTO) REFERENCES FOTOS(ID_FOTO))'''

sql_tabla_servicios = '''CREATE TABLE SERVICIOS( 
                 ID_SERVICIO INTEGER PRIMARY KEY AUTOINCREMENT, 
                 TIPO STRING NOT NULL, 
                 NOM_SERVICIO STRING NOT NULL, 
                 LAT_LONG STRING, 
                 DESCRIPCION STRING, 
                 DIRECCION STRING NOT NULL, 
                 TEL_CONTACTO INTEGER NOT NULL, 
                 NOM_CONTACTO STRING NOT NULL,
                 RECOMENDADO BOOLEAN) '''

sql_tabla_usuario = '''CREATE TABLE USUARIOS( 
                 CORREO STRING UNIQUE PRIMARY KEY NOT NULL,
                 PASSWORD STRING NOT NULL, 
                 NOMBRE STRING NOT NULL, 
                 APELLIDO STRING NOT NULL, 
                 TIPO INTEGER NOT NULL,
                 ESTADO BOOLEAN NOT NULL,
                 FECHA_INACTIVO	STRING) '''

sql_tabla_usuario_lugares = '''CREATE TABLE LUGARES_USUARIOS( 
                 ID_LUGAR INTEGER NOT NULL, 
                 CORREO STRING NOT NULL, 
                 CONSTRAINT PK_USUARIOS_LUGARES PRIMARY KEY(ID_LUGAR, CORREO), 
                 CONSTRAINT FK_LUGARES FOREIGN KEY(ID_LUGAR) REFERENCES LUGARES(ID_LUGAR), 
                 CONSTRAINT FK_USUARIOS FOREIGN KEY(CORREO) REFERENCES USUARIOS(CORREO))'''

sql_tabla_usuario_servicios = '''CREATE TABLE SERVICIOS_USUARIOS( 
                 ID_SERVICIO INTEGER NOT NULL, 
                 CORREO STRING NOT NULL, 
                 CONSTRAINT PK_USUARIOS_SERVICIOS PRIMARY KEY(ID_SERVICIO, CORREO), 
                 CONSTRAINT FK_SERVICIOS FOREIGN KEY(ID_SERVICIO) REFERENCES SERVICIOS(ID_SERVICIO), 
                 CONSTRAINT FK_USUARIOS FOREIGN KEY(CORREO) REFERENCES USUARIOS(CORREO))'''

sql_tabla_servicios_lugares = '''CREATE TABLE SERVICIOS_LUGARES ( 
                 ID_SERVICIO INT NOT NULL, 
                 ID_LUGAR NOT NULL, 
                 CONSTRAINT PK_SERVICIOS_LUGARES PRIMARY KEY(ID_SERVICIO, ID_LUGAR), 
                 CONSTRAINT FK_SERVICIOS FOREIGN KEY(ID_SERVICIO) REFERENCES SERVICIOS(ID_SERVICIO), 
                 CONSTRAINT FK_LUGARES FOREIGN KEY(ID_LUGAR) REFERENCES LUGARES(ID_LUGAR))'''

sql_tabla_likes_lugares_servicios = '''CREATE TABLE LIKES (
                CORREO NOT NULL,
                ID_LUGAR	INT,
                ID_SERVICIO INT,
                CONSTRAINT FK_LIKES_LUGARES FOREIGN KEY(ID_LUGAR) REFERENCES LUGARES(ID_LUGAR),
                CONSTRAINT FK_LIKES_USUARIOS FOREIGN KEY(CORREO) REFERENCES USUARIOS(CORREO),
                CONSTRAINT FK_LIKES_SERVICIO FOREIGN KEY(ID_SERVICIO) REFERENCES SERVICIOS(ID_SERVICIO))'''

sql_tabla_sesiones = ''' CREATE TABLE SESIONES(
                ID INTEGER PRIMARY KEY,
                CORREO STRING,
                FECHA_HORA STRING,
                FOREIGN KEY(CORREO) REFERENCES USUARIOS(CORREO))'''

sql_tabla_cambios = ''' CREATE TABLE CAMBIOS(
                TIPO STRING,
                CAMBIO STRING,
                FECHA	STRING,
                LUGAR	INTEGER
                FOREIGN KEY(LUGAR) REFERENCES LUGARES (ID_LUGAR)) '''


if __name__ == '__main__':
    try:
        print('Creando base de datos...')
        conexion = sqlite3.connect('../../turismo.db')

        print('Creando tablas...')
        conexion.execute(sql_tabla_lugares)
        conexion.execute(sql_tabla_fotos)
        conexion.execute(sql_tabla_lugares_fotos)
        conexion.execute(sql_tabla_servicios)
        conexion.execute(sql_tabla_usuario)
        conexion.execute(sql_tabla_usuario_lugares)
        conexion.execute(sql_tabla_usuario_servicios)
        conexion.execute(sql_tabla_servicios_lugares)

        conexion.execute(sql_tabla_likes_lugares_servicios)
        conexion.execute(sql_tabla_sesiones)
        conexion.execute(sql_tabla_cambios)

        conexion.close()
        print('Creación finalizada.')
    except Exception as e:
        print(f' Error creando la base de datos: {e}', e)
