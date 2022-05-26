import secrets

from flask import Flask, url_for, redirect, request, render_template, session, flash

from web.servicios import autenticacion as validacion_usuario, lugares as validacion_lugares, \
    servicios as validacion_servicios, likes as validacion_likes, cambios as validacion_cambios

app = Flask(__name__)


#### Se procesa la información que viene de las páginas HTML ####
########## Ingreso a página principal  ##########
@app.route('/')
def index():
    if 'correo_usuario' not in session:
        nombre = ''
        tipo = ''
        correo = ""
    else:
        nombre = session['nombre_usuario']
        tipo = session['tipo_usuario']
        correo = session['correo_usuario']
    return render_template('index.html', usuario=nombre, tipo_usuario=tipo, correo=correo)


#################################################################################
###########################     USUARIOS    #########################################
#################################################################################

##################################
#####    REGISTRO DE USUARIO   #####
##################################
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        validacion = validacion_usuario.registro(request.form['correo'], request.form['password'],
                                                 request.form['nombre'], request.form['apellido'],
                                                 request.form.get('tipo__usuario'))
        if validacion.status_code != 200:
            flash(validacion.text, 'mensaje__error')
            return render_template('registro.html')
        elif validacion.status_code == 200:
            return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('registro.html')


##################################
#####     LOGIN DE USUARIO   ########
##################################
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        validacion = validacion_usuario.validar_usuario(request.form['correo'], request.form['password'])

        if validacion.status_code != 200:
            session['correo_inactivo'] = request.form['correo']
            flash(validacion.text, 'mensaje__error')
            return render_template('login.html')

        elif validacion.status_code == 200:
            datos = validacion.json()

            usuario = datos['nombre']
            correo = datos['correo']
            tipo = int(datos['tipo'])

            # Valores a la sesion para poder utilizarlos en otro endpoint #
            session['nombre_usuario'] = usuario
            session['correo_usuario'] = correo

            if tipo == 1:
                tipo_usuario = "Administrador"
                session['tipo_usuario'] = tipo_usuario
                return redirect(url_for('index'))
            elif tipo == 2:
                tipo_usuario = "Empresa"
                session['tipo_usuario'] = tipo_usuario
                return redirect(url_for('servicios'))
            elif tipo == 3:
                tipo_usuario = "Usuario"
                session['tipo_usuario'] = tipo_usuario
                return redirect(url_for('lugares'))

    elif request.method == 'GET':
        return render_template('login.html')


##################################
#####     ACTIVAR CUENTA    ##########
##################################
@app.route('/activar')
def activar():
    correo = session['correo_inactivo']
    resultado = validacion_usuario.activar_usuario(correo)

    if resultado.status_code != 200:
        flash(resultado.text, 'mensaje__error')
        return redirect(url_for('login'))
    elif resultado.status_code == 200:
        flash(resultado.text, 'mensaje__exito')
        return redirect(url_for('login'))


##################################
##########     LOGOUT   #############
##################################
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


##################################
#####     BAJA DE USUARIO    #########
##################################
@app.route('/baja/<correo>')
def baja(correo):
    cuenta_desactivada = validacion_usuario.desactivar_cuenta(correo)
    if cuenta_desactivada.status_code != 200:
        flash(cuenta_desactivada.text, 'mensaje__error')
        return render_template('index.html')
    elif cuenta_desactivada.status_code == 200:
        flash(cuenta_desactivada.text, 'mensaje__exito')
        return render_template('index.html'), session.clear()


#################################################################################
###########################     LUGARES    #########################################
#################################################################################

##################################
##########    CREAR LUGAR   ########
##################################
@app.route('/lugar', methods=['GET', 'POST'])
def lugar():
    if 'correo_usuario' not in session:
        flash('Debe iniciar sesion para agregar un lugar', 'mensaje__error')
        return render_template('lugares.html', lugares=validacion_lugares.obtener_lugares())
    else:
        correo = session['correo_usuario']
        nombre = session['nombre_usuario']
        tipo = session['tipo_usuario']

        if str(tipo) != "Administrador":
            flash('Sólo el tipo "Administrador" puede agregar lugares', 'mensaje__error')
            return render_template('lugares.html', lugares=validacion_lugares.obtener_lugares(), usuario=nombre,
                                   tipo_usuario=tipo)
        else:
            if request.method == 'POST':
                validacion = validacion_lugares.crear_lugar(correo, request.form['nombre'], request.form['historia'],
                                                            request.form['latlong'], request.form['descripcion'],
                                                            request.form['actividades'],
                                                            request.form['caracteristicas'])
                if validacion.status_code != 200:
                    flash(validacion.text, 'mensaje__error')
                    return render_template('c-lugares.html')
                elif validacion.status_code == 200:
                    flash(validacion.text, 'mensaje__exito')
                    return redirect(url_for('lugar'))
                    # return render_template('c-lugares.html', usuario=nombre, tipo_usuario=tipo)

            elif request.method == 'GET':
                return render_template('c-lugares.html', usuario=nombre, tipo_usuario=tipo)


##################################
####### MODIFICAR LUGAR   #########
##################################
@app.route('/lugar/<id_lugar>', methods=['GET', 'POST'])
def modificar_lugar(id_lugar):
    if 'correo_usuario' not in session:
        flash('Debe iniciar sesion para modificar un lugar', 'mensaje__error')
        return render_template('lugares.html', lugares=validacion_lugares.obtener_lugares())
    else:
        nombre = session['nombre_usuario']
        tipo = session['tipo_usuario']

        if str(tipo) != "Administrador":
            flash('Sólo el tipo "Administrador" puede modificar los lugares', 'mensaje__error')
            return render_template('lugares.html', lugares=validacion_lugares.obtener_lugares(), usuario=nombre,
                                   tipo_usuario=tipo)
        else:
            if request.method == 'GET':
                datos_lugar = validacion_lugares.lugar_por_id(id_lugar)
                return render_template('m-lugares.html', lugar=datos_lugar[0], usuario=nombre, tipo_usuario=tipo)

            if request.method == 'POST':
                print("Entra en el post")
                validacion = validacion_lugares.modificar_lugar(id_lugar, request.form['nombre'],
                                                                request.form['historia'], request.form['latlong'],
                                                                request.form['descripcion'],
                                                                request.form['actividades'],
                                                                request.form['caracteristicas'])
                print(validacion.status_code)
                if validacion.status_code != 200:

                    flash(validacion.text, 'mensaje__error')
                    return redirect(url_for('modificar_lugar', id_lugar=id_lugar))
                    #return render_template('m-lugares.html', usuario=nombre, tipo_usuario=tipo)

                elif validacion.status_code == 200:
                    flash(validacion.text, 'mensaje__exito')
                    return redirect(url_for('modificar_lugar', id_lugar=id_lugar))
            return render_template('m-lugares.html')


##################################
####### ELIMINAR LUGAR   ##########
##################################
@app.route("/lugares/<id_lugar>")
def eliminar_lugar(id_lugar):
    if 'correo_usuario' not in session:
        flash('Debe iniciar sesion para eliminar un lugar', 'mensaje__error')
        return render_template('lugares.html', lugares=validacion_lugares.obtener_lugares())
    else:
        nombre = session['nombre_usuario']
        tipo = session['tipo_usuario']

        if str(tipo) != "Administrador":
            flash('Sólo el tipo "Administrador" puede eliminar los lugares', 'mensaje__error')
            return render_template('lugares.html', lugares=validacion_lugares.obtener_lugares(), usuario=nombre,
                                   tipo_usuario=tipo)
        else:
            validacion = validacion_lugares.eliminar_lugar(id_lugar)
            if validacion.status_code != 200:
                flash(validacion.text, 'mensaje__error')
                return redirect(url_for('lugares', usuario=nombre, tipo_usuario=tipo))
            elif validacion.status_code == 200:
                flash(validacion.text, 'mensaje__exito')
                list_lugares = validacion_lugares.obtener_lugares()
                return render_template('lugares.html', lugares=list_lugares, usuario=nombre, tipo_usuario=tipo)


##################################
##### LISTADO DE LUGARES   ########
##################################
@app.route('/lugares', methods=['GET', 'POST'])
def lugares():
    if 'correo_usuario' not in session:
        nombre = ''
        tipo = ''
    else:
        nombre = session['nombre_usuario']
        tipo = session['tipo_usuario']

    if request.method == 'GET':
        list_lugares = validacion_lugares.obtener_lugares()
        return render_template('lugares.html', usuario=nombre, tipo_usuario=tipo, lugares=list_lugares)

    elif request.method == 'POST':
        filtro_lugares = request.form.get('filtro__lugares')
        valor_buscador = request.form['buscador']

        valor = int(filtro_lugares)

        resultado = validacion_lugares.lugares_segun_filtro(valor, valor_buscador)

        if resultado.status_code != 200:
            flash(resultado.text, 'mensaje__error')
            return render_template('lugares.html', lugares=validacion_lugares.obtener_lugares(), usuario=nombre, tipo_usuario=tipo)
        elif resultado.status_code == 200:
            return render_template('lugares.html', lugares=resultado.json(), usuario=nombre, tipo_usuario=tipo)


##################################
###### ME GUSTAS - LUGAR   ########
##################################
@app.route('/mg/<id_lugar>')
def mg(id_lugar):
    correo = session['correo_usuario']
    existe_mg = validacion_likes.existe_mg(correo, id_lugar)

    if existe_mg.status_code != 200:
        # Si no existe se agrega #
        validacion_likes.agregar_mg(correo, id_lugar)
    elif existe_mg.status_code == 200:
        # Si existe se elimina #
        validacion_likes.eliminar_mg(correo, id_lugar)
    return redirect(url_for('lugares'))


################################################################################
###############     CAMBIOS Y SUGERENCIAS - LUGARES    ############################
################################################################################
##################################
###### AGREGAR CAMBIO  ##########
##################################
@app.route('/cambio/<id_lugar>', methods=['GET', 'POST'])
def cambio(id_lugar):
    if request.method == 'POST':
        cambio_ = str(request.form.get('cambio'))
        tipo_cambio = str(request.form.get('tipo_cambio'))

        if 'Eliminar' in tipo_cambio:
            tipo_cambio = 'Eliminar'
        elif 'Modificar' in tipo_cambio:
            tipo_cambio = 'Modificar'
        elif 'Agregar' in tipo_cambio:
            tipo_cambio = 'Agregar'

        resultado = validacion_cambios.agregar_cambio(tipo_cambio, cambio_, id_lugar)

        if resultado.status_code != 200:
            flash(resultado.text, 'mensaje__error')
        elif resultado.status_code == 200:
            flash(resultado.text, 'mensaje__exito')

    return redirect(url_for('lugares'))


################################################################################
###########################     SERVICIOS    #######################################
################################################################################

##################################
####### CREAR SERVICIO ###########
##################################
@app.route('/servicio', methods=['GET', 'POST'])
def servicio():
    correo = session['correo_usuario']
    nombre = session['nombre_usuario']
    tipo = session['tipo_usuario']

    if request.method == 'POST':
        recomendado = request.form.get("recomendado")

        validacion = validacion_servicios.crear_servicio(correo, request.form['nombre'], request.form['tipo'],
                                                         request.form['ubicacion'], request.form['descripcion'],
                                                         request.form['direccion'], request.form['contacto'],
                                                         request.form['nro__contacto'], recomendado)

        if validacion.status_code != 200:
            mensaje = validacion.text
            flash(mensaje, 'mensaje__error')
            return render_template('c-servicios.html')
        elif validacion.status_code == 200:
            mensaje = validacion.text
            flash(mensaje, 'mensaje__exito')
            return render_template('c-servicios.html', exito=mensaje, usuario=nombre, tipo_usuario=tipo)

    elif request.method == 'GET':
        return render_template('c-servicios.html', usuario=nombre, tipo_usuario=tipo)


##################################
#### LISTADO DE SERVICIOS ########
##################################
@app.route('/servicios')
def servicios():
    if 'correo_usuario' not in session:
        flash('Debe iniciar sesion para acceder a este item', 'mensaje__error')
        return render_template('index.html')
    elif session['tipo_usuario'] != "Empresa":
        flash('El usuario logueado no es del tipo "Empresa", no puede acceder a este item', 'mensaje__error')
        return render_template('index.html')
    else:
        correo = session['correo_usuario']
        nombre = session['nombre_usuario']
        tipo = session['tipo_usuario']

        # valor_buscador = str(request.args.get('buscador'))

        list_servicios = validacion_servicios.obtener_servicios_usuario(correo)

        if list_servicios.status_code != 200:
            mensaje = list_servicios.text
            flash(mensaje, 'mensaje__error')
            return render_template('servicios.html', usuario=nombre, tipo_usuario=tipo)
        elif list_servicios.status_code == 200:
            return render_template('servicios.html', usuario=nombre, tipo_usuario=tipo, servicios=list_servicios)

        # hacer un elif para cuando el buscador tiene datos #


################################################################################
######################     ADMINISTRADOR    #######################################
################################################################################
@app.route('/administrar')
def administrar():
    nombre = session['nombre_usuario']
    tipo = session['tipo_usuario']

    list_sugerencias = validacion_cambios.lista_cambios()
    return render_template('administrar.html', usuario=nombre, tipo_usuario=tipo, sugerencias=list_sugerencias)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = secrets.token_urlsafe(20)
    app.debug = True
    app.run(port=5002)
