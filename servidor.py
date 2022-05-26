from flask import Flask, request, jsonify, Blueprint
from servicios.autenticacion import autenticacion
from servicios.turismo import servicios
from servicios.turismo import lugares
from servicios.turismo import fotos
from servicios.turismo import likes
from servicios.turismo import cambios

app = Flask(__name__)
api_images = Blueprint('api_images', __name__)


#################################################################################
###########################     USUARIOS   #########################################
#################################################################################
########################################
#######    CREAR USUARIO    ###############
########################################
@app.route("/registro", methods=['GET', 'POST'])
def crear_usuario():
    # Validando datos ingresados
    datos_ingresados = request.get_json()
    if 'correo' not in datos_ingresados or not datos_ingresados['correo']:
        return 'El correo es obligatorio', 400
    if 'password' not in datos_ingresados or not datos_ingresados['password']:
        return 'La contraseña es obligatoria', 400
    if 'nombre' not in datos_ingresados or not datos_ingresados['nombre']:
        return 'El nombre es obligatorio', 400
    if 'apellido' not in datos_ingresados or not datos_ingresados['apellido']:
        return 'El apellido es obligatorio', 400
    if 'tipo' not in datos_ingresados or not datos_ingresados['tipo']:
        return 'El tipo es obligatorio', 400

    try:
        autenticacion.crear_usuario(datos_ingresados['correo'], datos_ingresados['password'],
                                    datos_ingresados['nombre'], datos_ingresados['apellido'], datos_ingresados['tipo'])
    except Exception:
        return 'El usuario ya existe', 400
    return "Registro exitoso", 200


###################################################
################# POR HACER ######################
@app.route("/usuarios/<usuario_modificar>", methods=['PUT'])
def modificar_usuario(usuario_modificar):
    # Validando existencia del usuario a modificar
    usuario_a_modificar = autenticacion.buscar_usuario(usuario_modificar)
    if len(usuario_a_modificar) == 0:
        return 'El usuario no existe', 404

    # Validando datos ingresados
    datos_ingresados = request.get_json()
    if 'password' not in datos_ingresados or not datos_ingresados['password']:
        return 'La contraseña no puede quedar vacía', 400
    if 'nombre' not in datos_ingresados or not datos_ingresados['nombre']:
        return 'El nombre no puede quedar vacío', 400
    if 'apellido' not in datos_ingresados or not datos_ingresados['apellido']:
        return 'El apellido no puede quedar vacío', 400
    if 'tipo' not in datos_ingresados or not datos_ingresados['tipo']:
        return 'El tipo no puede quedar vacío', 400

    # Pasando los datos para la modificación en la BD
    autenticacion.modificar_usuario(usuario_modificar, datos_ingresados['password'], datos_ingresados['nombre'],
                                    datos_ingresados['apellido'], datos_ingresados['tipo'])
    return 'Usuario modificado', 200


########################################
#######    INICIO DE SESION  ###############
########################################
@app.route("/login", methods=['GET', 'POST'])
def login():
    # Validando datos ingresados
    datos_ingresados = request.get_json()
    if 'correo' not in datos_ingresados or not datos_ingresados['correo']:
        return 'El correo es requerido', 400
    if 'password' not in datos_ingresados or not datos_ingresados['password']:
        return 'La contraseña es requerida', 400

    try:
        datos_usuario = autenticacion.login(datos_ingresados['correo'])
        nombre_usuario = datos_usuario['nombre']
        correo = datos_ingresados['correo']
        tipo = datos_usuario['tipo']
        estado = datos_usuario['estado']

        if int(estado) == 0:
            mensaje = 'El usuario está inactivo desde ' + str(datos_usuario['fecha_inactivo'])
            return mensaje, 404
        else:
            if str(datos_usuario['password']) != str(datos_ingresados['password']):
                return 'Contraseña incorrecta', 404
            else:
                sesion = autenticacion.crear_sesion(datos_ingresados['correo'])
                return jsonify({"id_sesion": sesion['id_sesion'],
                                "nombre": nombre_usuario,
                                "correo": correo,
                                "tipo": tipo,
                                "fecha_hora": sesion['fecha_hora']})
    except Exception:
        return 'Usuario no existe', 404


########################################
#######    ACTIVAR CUENTA  ###############
########################################
@app.route("/activar", methods=['GET', 'POST'])
def activar():
    datos_ingresados = request.get_json()
    correo = datos_ingresados['correo']

    try:
        autenticacion.activar_cuenta(correo)
        return "Cuenta habilitada con exito", 200
    except Exception:
        return "No se pudo habilitar la cuenta", 404


########################################
#####    DESACTIVAR CUENTA  #############
########################################
@app.route("/desactivar/<correo>", methods=['PUT'])
def usuario_desactivar(correo):
    try:
        autenticacion.desactivar_cuenta(correo)
        return "Cuenta desactivada con exito", 200
    except Exception:
        return "No se pudo desactivar la cuenta", 404


#################################################################################
###########################     LUGARES    #########################################
#################################################################################
########################################
##########    CREAR LUGAR  ###############
########################################
@app.route("/crear_lugar", methods=['GET', 'POST'])
def crear_lugar():
    datos_ingresados = request.get_json()
    if 'nombre' not in datos_ingresados or not datos_ingresados['nombre']:
        return 'El campo "nombre" es obligatorio', 400
    if 'historia' not in datos_ingresados or not datos_ingresados['historia']:
        return 'El campo "historia" es obligatorio', 400
    if 'correo' not in datos_ingresados:
        return 'El campo "correo" es obligatorio', 400

    # Verificar si existe lugar con el mismo nombre -- Por hacer
    try:
        # Crear lugar y asociar al usuario
        lugar_creado_id = \
            lugares.crear_lugar(datos_ingresados['nombre'], datos_ingresados['historia'], datos_ingresados['lat_long'],
                                datos_ingresados['descripcion'], datos_ingresados['actividades'],
                                datos_ingresados['caracteristicas'])[0]

        lugares.asociar_lugar_usuario(lugar_creado_id[0], datos_ingresados['correo'])
    except Exception:
        return 'Otro problema', 400
    return 'Lugar creado correctamente', 200


########################################
##########    MODIFICAR LUGAR  ###########
########################################
@app.route("/lugar/<id_lugar>", methods=['PUT'])
def modificar_lugar(id_lugar):
    datos_ingresados = request.get_json()
    if 'nombre' not in datos_ingresados or not datos_ingresados['nombre']:
        return 'El nombre es obligatorio', 400
    if 'historia' not in datos_ingresados or not datos_ingresados['historia']:
        return 'La historia del lugar es obligatoria', 400
    if 'lat_long' not in datos_ingresados:
        return "El campo 'lat_long' del lugar es obligatorio", 400
    if 'descripcion' not in datos_ingresados:
        return "El campo 'descripcion' del lugar es obligatorio", 400
    if 'actividades' not in datos_ingresados:
        return "El campo 'actividades' del lugar es obligatorio", 400
    if 'caracteristicas' not in datos_ingresados:
        return "El campo 'caracteristicas' del lugar es obligatorio", 400

    try:
        print("Entra en el try")
        resultado = lugares.modificar_lugar(id_lugar, datos_ingresados['nombre'], datos_ingresados['historia'],
                                            datos_ingresados['lat_long'], datos_ingresados['descripcion'],
                                            datos_ingresados['actividades'], datos_ingresados['caracteristicas'])

        print(resultado)
    except Exception:
        return 'Puede ser base bloqueada', 404
    return 'Lugar modificado correctamente', 200


########################################
###########    ELIMINAR LUGAR   ###########
########################################
@app.route("/lugares/<id_lugar>", methods=['DELETE'])
def eliminar_lugar(id_lugar):
    mensaje = None
    try:
        try: # Eliminando relación en tabla usuarios_lugares
            lugares.eliminar_lugar_usuario(id_lugar)
        except Exception:
            mensaje = 'No es posible eliminar los datos en: usuarios_lugares'

        try:  # Eliminando relación en tabla cambios
            lugares.eliminar_lugar_cambio(id_lugar)
        except Exception:
            mensaje = 'No es posible eliminar los datos en: cambio/sugerencias'

        try: # Eliminando lugar
            lugares.eliminar_lugar(id_lugar)
        except Exception:
            mensaje = 'No es posible eliminar los datos en: lugares'
    except Exception:
        return mensaje, 400

    else:
        return 'Lugar eliminado con exito', 200


########################################
#######    TODOS LOS LUGARES  ###########
########################################
# Lo ideal seria listar los 'x' con mas me gustas' #
@app.route("/lugares", methods=['GET'])
def listado_lugares():
    return jsonify(lugares.all_lugares())


########################################
##########    LUGAR POR ID ###############
########################################
@app.route("/lugar/<id_lugar>", methods=['GET'])
def lugar_por_id(id_lugar):
    return jsonify(lugares.buscar_x_id(id_lugar))


########################################
#######    LUGARES SEGUN FILTRO  ########
########################################
@app.route("/lugares/", methods=['GET'])
def listado_lugares_filtro():
    datos_ingresados = request.get_json()
    filtro = int(datos_ingresados['filtro'])
    valor = datos_ingresados['valor']
    resultado = ''

    if filtro == 2:
        resultado = lugares.buscar_x_nom_lugar(valor)
    elif filtro == 3:
        resultado = lugares.buscar_x_caracteristica(valor)
    elif filtro == 4:
        resultado = lugares.buscar_x_actividad(valor)
    elif filtro == 5:
        return "Aun no se ha implementado los eventos de los lugares", 404
    elif filtro == 6:
        resultado = lugares.all_lugares()

    if not resultado:
        return "No hay coincidencias", 404
    return jsonify(resultado)


################################################################################
##################     CAMBIOS - SUGERENCIAS    ####################################
################################################################################
@app.route("/cambio", methods=['GET', 'POST'])
def cambio():
    if request.method == 'GET':
        resultado = cambios.listar_cambios()
        return jsonify(resultado)
    elif request.method == 'POST':
        datos_ingresados = request.get_json()
        try:
            cambios.agregar_cambio(datos_ingresados['tipo'], datos_ingresados['cambio'], datos_ingresados['lugar'])
        except Exception:
            return 'No se pudo agregar la sugerencia', 404
        return "Sugerencia enviada correctamente", 200


################################################################################
###########################     SERVICIOS    #######################################
################################################################################
###################################################
################# POR HACER ######################
@app.route("/servicios", methods=['POST'])
def crear_servicio():
    datos_ingresados = request.get_json()
    if 'tipo' not in datos_ingresados or not datos_ingresados['tipo']:
        return 'El campo "tipo" es obligatorio', 400
    if 'nom_servicio' not in datos_ingresados or not datos_ingresados['nom_servicio']:
        return 'El campo "nom_servicio" es obligatorio', 400
    if 'direccion' not in datos_ingresados or not datos_ingresados['direccion']:
        return 'El campo "direccion" es obligatorio', 400
    if 'tel_contacto' not in datos_ingresados or not datos_ingresados['tel_contacto']:
        return 'El campo "tel_contacto" es obligatorio', 400
    if 'nom_contacto' not in datos_ingresados or not datos_ingresados['nom_contacto']:
        return 'El campo "nom_contacto" es obligatorio', 400
    if 'correo' not in datos_ingresados or not datos_ingresados['correo']:
        return 'El campo "correo" es obligatorio', 400
    if 'id_lugar' not in datos_ingresados or not datos_ingresados['id_lugar']:
        return 'El campo "id_lugar" es obligatorio', 400

    # Verificar si existe mismo nombre -- Por hacer

    # Validando usuario que desea crear el servicio
    usuario_servicio = autenticacion.buscar_usuario(datos_ingresados['correo'])
    if len(usuario_servicio) == 0:
        return "El ususario que desea ingresar el servicio, no existe", 400

    # Validando que el lugar al que se quiere asociar el servicio existe
    lugar_servicio = lugares.buscar_x_id(datos_ingresados['id_lugar'])
    if len(lugar_servicio) == 0:
        return "El lugar al que pertenece el servicio no existe", 400

    # Creando servicio y obteniendo id
    id_servicio = servicios.crear_servicio(datos_ingresados['tipo'], datos_ingresados['nom_servicio'],
                                           datos_ingresados['lat_long'],
                                           datos_ingresados['descripcion'], datos_ingresados['direccion'],
                                           datos_ingresados['tel_contacto'], datos_ingresados['nom_contacto'])

    # Asociar servicio a usuario que lo crea
    servicios.asociar_servicio_usuario(id_servicio[0][0], usuario_servicio['correo'])
    # Asociar servicio a lugar que pertenece
    servicios.asociar_servicio_lugar(id_servicio[0][0], lugar_servicio['id_lugar'])
    return 'Servicio creado', 201


###################################################
###### SERVICIOS DEL USUARIO LOGUEADO  ###########
###################################################
@app.route("/servicios/<usuario>", methods=['GET'])
def listado_servicios(usuario):
    valor_encontrado = servicios.all_servicios_usuario(usuario)

    if len(valor_encontrado) == 0:
        return 'El usuario logueado no tiene ningún servicio asociado', 404
    else:
        return jsonify(valor_encontrado)


###################################################
################# POR HACER ######################
@app.route("/servicios/<nom_servicio>", methods=['GET'])
def listado_nom_servicio(nom_servicio):
    valor_encontrado = servicios.buscar_x_nom_servicio(nom_servicio)
    if not valor_encontrado or not ['nom_servicio'] or len(valor_encontrado) == 0:
        return "No hay coincidencias"

    return str(valor_encontrado), 200


###################################################
################# POR HACER ######################
@app.route("/servicios/<direccion>", methods=['GET'])
def listado_direccion(direccion):
    valor_encontrado = servicios.buscar_x_direccion(direccion)
    if not valor_encontrado or not ['direccion'] or len(valor_encontrado) == 0:
        return "No hay coincidencias"

    return str(valor_encontrado), 200


###################################################
################# POR HACER ######################
@app.route("/servicios/<id_servicio>,<id_lugar>", methods=['GET'])
def listado_servicios_x_lugar(id_servicio, id_lugar):
    lista_encontrada = servicios.buscar_servicios_x_lugar(id_servicio, id_lugar)
    return str(lista_encontrada), 200


###################################################
################# POR HACER ######################
@app.route("/servicios/<id_servicio>", methods=['PUT'])
def modificar_servicio(id_servicio):
    # Verificando que existe
    servicio_a_modificar = servicios.buscar_servicio(id_servicio)
    if id_servicio not in str(servicio_a_modificar[0]):
        return "El servicio que desea modificar no existe", 404

    datos_ingresados = request.get_json()
    if 'tipo' not in datos_ingresados or not datos_ingresados['tipo']:
        return 'El tipo es obligatorio', 400
    if 'nom_servicio' not in datos_ingresados or not datos_ingresados['nom_servicio']:
        return 'El nombre del servicio es obligatorio', 400
    if 'direccion' not in datos_ingresados or not datos_ingresados['direccion']:
        return 'La direccion es obligatoria', 400
    if 'tel_contacto' not in datos_ingresados or not datos_ingresados['tel_contacto']:
        return 'Es obligatorio un telefono de contacto', 400
    if 'nom_contacto' not in datos_ingresados or not datos_ingresados['nom_contacto']:
        return 'Es obligatorio el nombre del contacto', 400

    servicios.modificar_servicio(id_servicio, datos_ingresados['tipo'], datos_ingresados['nom_servicio'],
                                 datos_ingresados['lat_long'],
                                 datos_ingresados['descripcion'], datos_ingresados['direccion'],
                                 datos_ingresados['tel_contacto'], datos_ingresados['nom_contacto'])
    return 'Servicio modificado', 200


###################################################
################# POR HACER ######################
@app.route("/servicios/<id_servicio>", methods=['DELETE'])
def eliminar_servicio(id_servicio):
    # Verificando que existe
    servicio_a_eliminar = servicios.buscar_servicio(id_servicio)
    if id_servicio not in str(servicio_a_eliminar):
        return 'El servicio que desea eliminar no existe', 404

    # Buscando relación tabla servicios-lugares
    lugares_segun_servicio = lugares.lugar_segun_servicio(id_servicio)
    lista_id_lugares = []
    for valores in lugares_segun_servicio:
        lista_id_lugares.append(valores[0])

    if len(lugares_segun_servicio) > 0:
        contador = 0
        while contador < len(lista_id_lugares):
            servicios.eliminar_servicio_lugar(servicio_a_eliminar['id_servicio'], lista_id_lugares[contador])
            contador = contador + 1

    servicios.eliminar_servicio_usuario(servicio_a_eliminar['id_servicio'])
    servicios.eliminar_servicio(id_servicio)
    return 'Servicio eliminado', 200


#################################################################################
###########################     FOTOS    ###########################################
#################################################################################
##################################################
############# POR HACER ######################
##################################################
@app.route("/fotos", methods=['POST'])
def agregar_fotos():
    datos_ingresados = request.get_json()
    if 'fecha' not in datos_ingresados or not datos_ingresados['fecha']:
        return 'El campo "fecha" es obligatorio', 400
    if 'foto' not in datos_ingresados or not datos_ingresados['foto']:
        return 'El campo "foto" es obligatorio', 400
    if 'id_lugar' not in datos_ingresados or not datos_ingresados['id_lugar']:
        return 'El campo "id_lugar" es obligatorio', 400

    id_foto = fotos.crear_foto(datos_ingresados['fecha'], datos_ingresados['foto'])
    id_lugar = lugares.buscar_x_id(datos_ingresados['id_lugar'])

    if len(id_lugar) == 0:
        return "No existe el lugar al que desea asociar la foto", 400
    fotos.asociar_foto_lugar(id_foto[0][0], id_lugar['id_lugar'])
    return 'OK', 201


###################################################
################# POR HACER ######################
@app.route("/fotos", methods=['GET'])
def listado_fotos():
    valor_encontrado = fotos.buscar_fotos()
    return str(valor_encontrado), 200


###################################################
################# POR HACER ######################
@app.route("/fotos/<id_foto>", methods=['DELETE'])
def eliminar_foto(id_foto):
    foto_a_eliminar = fotos.buscar_foto(id_foto)
    if len(foto_a_eliminar) == 0:
        return "La foto no existe", 400

    fotos.eliminar_foto_lugar(id_foto)
    fotos.eliminar_foto(id_foto)
    return 'Foto eliminada', 200


################################################################################
###########################     LIKES    ############################################
################################################################################
########################################
#####   ME GUSTA  LUGAR - USUARIO  #######
########################################
@app.route("/lugar/mg", methods=['GET', 'POST', 'DELETE'])
def mg_lugar_usuario():
    datos_ingresados = request.get_json()
    correo = datos_ingresados['correo']
    id_lugar = datos_ingresados['id_lugar']

    if request.method == 'GET':
        mg_existe = likes.existe_mg_lugar_usuario(correo, id_lugar)
        if len(mg_existe) == 0:
            return 'No existe el me gusta', 404
        else:
            return 'Ya existe el me gusta', 200

    elif request.method == 'POST':
        likes.nuevo_like_lugar(correo, id_lugar)
        return 'Agregado', 200

    elif request.method == 'DELETE':
        likes.eliminar_like_lugar(correo, id_lugar)
        return 'Eliminado', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
