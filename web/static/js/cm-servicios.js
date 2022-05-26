/***********************************************************************/
/*********** INGRESO DE DATOS DEL FORMULARIO DE SERVICIOS *************/
/*********************************************************************/

var elemento = '';
var elemento_inputs = '';

if (document.getElementById('form__crear__servicio') != null) {
    elemento = 'form__crear__servicio';
    elemento_inputs = '#form__crear__servicio input';

} else {
    elemento = 'form__modificar__servicio';
    elemento_inputs = '#form__modificar__servicio input';
}

const formulario = document.getElementById(elemento);
const inputs = document.querySelectorAll(elemento_inputs);

/* Expresiones regulares para condicionar los campos del formulario */
const expresiones = {
    nombre: /^[\w\s,.]{5,40}$/, // Letras, números, espacios, comas y puntos
    tipo: /^[a-zA-Z]+$/, //Solo se permiten letras
    descripcion: /^[a-zA-Z0-9\s,.;+-_"']{10,}$/, // Letras, números y espacios
    direccion: /^[A-Za-z0-9'\.\-\s\,]$/,
    contacto: /^[a-zA-Z\s]+$/, //Solo se permiten letras y espacios
    nro_contacto: /^[0-9\s-]{8,}$/
}

const campos = {
    nombre: false,
    tipo: false,
    descripcion: false,
    direccion: false,
    contacto: false,
    nro_contacto: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
            break;

        case "tipo":
            validarCampo(expresiones.tipo, e.target, 'tipo');
            break;

        case "descripcion":
            validarCampo(expresiones.descripcion, e.target, 'descripcion');
            break;

        case "direccion":
            validarCampo(expresiones.direccion, e.target, 'direccion');
            break;

        case "contacto":
            validarCampo(expresiones.contacto, e.target, 'contacto');
            break;

        case "nro__contacto":
            validarCampo(expresiones.nro_contacto, e.target, 'nro__contacto');
            break;
    }
}

/* Validando cada campo del formulario y agregando iconos*/
const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('grupo__inputs-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('grupo__inputs-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} .mensaje__error`).classList.remove('mensaje__error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('grupo__inputs-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('grupo__inputs-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .mensaje__error`).classList.add('mensaje__error-activo');
		campos[campo] = false;
	}
}

/* Función para validar el formulario */
inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario); /* Cuando se presiona una tecla */
    input.addEventListener('blur', validarFormulario); /* Cuando se presiona fuera del formulario */
});

/*********** Condición para cuando se presiona el botón confirmar ***********/
formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    
    if (campos.nombre && campos.tipo && campos.descripcion && campos.direccion && campos.contacto && campos.nro_contacto){
        document.querySelectorAll('.grupo__inputs-correcto').forEach((icono) => {
            icono.classList.remove('grupo__inputs-correcto');
        });
        formulario.submit(); 

    }else {
        document.getElementById('mensaje__error__registro__js').classList.add('mensaje__error__registro__js-activo');

        setTimeout(() => {
            document.getElementById('mensaje__error__registro__js').classList.remove('mensaje__error__registro__js-activo');
        },7000);
    };
});