const btn__buscar = document.getElementById('btn__buscar');
const formulario_busqueda = document.getElementById('form_busqueda');
const input_buscador = document.getElementById('buscador');
const select_buscador = document.getElementById('filtro__lugares');
const mensaje_buscador = document.getElementById('mensaje__buscador');
const mensaje_servidor = document.getElementById('mensaje__error__registro');

const usuario_logueado = document.getElementById('dato__usuario');
const tipo_usuario = document.getElementById('dato__tipo');
const btn_mg = document.getElementById('btn__mg');
const formulario_mg = document.getElementById('form_mg');
const ancla_mg = document.getElementsByName('ancla_mg');

const ventana_eliminar = document.getElementById('ventana__eliminar');
const ventana_baja_usuario = document.getElementById('ventana__baja__usuario');
const ventana_sugerencia = document.getElementById('ventana__sugerencia');

const ancla__confirmar = document.getElementById('ancla__confirmar'); // Boton de la ventana del Admin
const ancla_modificar = document.getElementById('ancla_modificar');
const ancla__enviar = document.getElementById('ancla__enviar'); // Boton de la ventana de sugerencia para confirmar formulario sugerencia
const formulario_sugerencia = document.getElementById('form_sugerencia');

/* Submit de los formularios manual */
function envio_manual(formulario) {
    formulario.addEventListener('submit', (e) => {
        e.preventDefault();
    });
};

envio_manual(formulario_busqueda);
envio_manual(formulario_mg);

/****************************************************************************************************************/
/****************************************  VALIDACIÓN PARA EL BUSCADOR  ****************************************/
/**************************************************************************************************************/
btn__buscar.addEventListener('click', (e) => {
    var valor = input_buscador.value;

    if (select_buscador.value == 1) {
        mensaje_buscador.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Error: Debe seleccionar un opción de búsqueda';

        document.getElementById('mensaje__buscador__error').classList.add('mensaje__error-activo');
        setTimeout(() => {
            document.getElementById('mensaje__buscador__error').classList.remove('mensaje__error-activo');
        }, 7000);

    } else {
        if (valor.length == 0 && select_buscador.value != 6) {

            mensaje_buscador.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Error: El campo de búsqueda no puede quedar vacío.';

            document.getElementById('mensaje__buscador__error').classList.add('mensaje__error-activo');
            setTimeout(() => {
                document.getElementById('mensaje__buscador__error').classList.remove('mensaje__error-activo');
            }, 7000);

        } else {
            formulario_busqueda.submit();
        }
    }
});

// /******************************************************************************************/
// /***************************  VENTANAS: ELIMINAR - SUGERENCIAS ****************************/
// /******************************************************************************************/
function mostrar_ventana(boton) {
    if (usuario_logueado != null) {
        var tipo = tipo_usuario.textContent;

        if (tipo.includes('Administrador')) {
            ventana_eliminar.classList.add('mostrar');
        } else {
            if (boton.id != 'btn__mg') {
                ventana_sugerencia.classList.add('mostrar');
            }
        };

    } else { // Creo el mensaje para mostrar que debe iniciar sesión 
        if (document.getElementById('mensaje__eliminar') == null) {
            var mensaje = document.getElementById("mensajes");
            var mensaje_eliminar = document.createElement("div");
            mensaje_eliminar.setAttribute("id", "mensaje__eliminar");

            var p_mensaje = document.createElement("p");
            p_mensaje.setAttribute("id", "p__mensaje__eliminar");


            mensaje_eliminar.classList.add('mensaje__error');
            mensaje_eliminar.classList.add('mensaje__error-activo');

            if (boton.id == 'btn__eliminar') {
                p_mensaje.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Debe iniciar sesion para eliminar el lugar';
            } else if (boton.id == 'btn__modificar') {
                p_mensaje.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Debe iniciar sesion para modificar el lugar';
            } else if (boton.id == 'btn__agregar') {
                p_mensaje.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Debe iniciar sesion para agregar un lugar';
            } else if (boton.id == 'btn__mg') {
                p_mensaje.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Debe iniciar sesion para dar me gusta a un lugar';
            }

            mensaje_eliminar.appendChild(p_mensaje); // Agrego el texto a otra división 
            mensaje.appendChild(mensaje_eliminar); // Agrego al div de mensajes para que se muestre

            setTimeout(() => {
                mensaje_eliminar.classList.remove('mensaje__error-activo');
            }, 7000);

        } else {
            if (boton.id == 'btn__eliminar') {
                document.getElementById('p__mensaje__eliminar').innerHTML = '<i class="fas fa-exclamation-triangle"></i> Debe iniciar sesion para eliminar el lugar';
            } else if (boton.id == 'btn__modificar') {
                document.getElementById('p__mensaje__eliminar').innerHTML = '<i class="fas fa-exclamation-triangle"></i> Debe iniciar sesion para modificar el lugar';
            } else if (boton.id == 'btn__agregar') {
                document.getElementById('p__mensaje__eliminar').innerHTML = '<i class="fas fa-exclamation-triangle"></i> Debe iniciar sesion para agregar un lugar';
            } else if (boton.id == 'btn__mg') {
                document.getElementById('p__mensaje__eliminar').innerHTML = '<i class="fas fa-exclamation-triangle"></i> Debe iniciar sesion para dar me gusta a un lugar';
            }
            document.getElementById('mensaje__eliminar').classList.add('mensaje__error-activo');
        };
    };
};

function cerrar_ventana(ventana) {
    ventana.classList.remove('mostrar');
};

/******************************************************************************************/
/***************** PASANDO LOS DATOS AL LOS BOTONES ***************************************/
/******************************************************************************************/
function tipo_cambio(tipo, id, nombre_lugar) {

    console.log(tipo + " - " + id);
    var input_cambio = document.getElementById('tipo_cambio');
    input_cambio.value = input_cambio.value + tipo + " " + nombre_lugar;

    if (tipo == 'Eliminar') {
        ancla__confirmar.href = "/lugares/" + id;
    }

    if (tipo == 'Agregar') {
        id = '0';
    }

    if (tipo != 'MG') {
        ancla__enviar.href = "/cambio/" + id;
        formulario_sugerencia.action = "/cambio/" + id;
    }
};