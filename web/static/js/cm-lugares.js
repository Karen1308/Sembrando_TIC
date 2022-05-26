const btn_confirmar = document.getElementById('btn__confirmar');

var elemento = '';
var elemento_inputs = '';
var elemento_textarea = '';

/***********************************************************************/
/*********** INGRESO DE DATOS DEL FORMULARIO DE LUGARES ***************/
/*********************************************************************/
if (document.getElementById('form__crear__lugar') != null){
    elemento = 'form__crear__lugar';
    elemento_inputs = '#form__crear__lugar input';
    elemento_textarea = '#form__crear__lugar textarea';
    
    }else {
    elemento = 'form__modificar__lugar';
    elemento_inputs = '#form__modificar__lugar input';
    elemento_textarea = '#form__modificar__lugar textarea';
}

const formulario = document.getElementById(elemento);
const inputs = document.querySelectorAll(elemento_inputs);
const textarea = document.querySelectorAll(elemento_textarea);

/* Expresiones regulares para condicionar los campos del formulario */
const expresiones = {
    nombre: /^[\w\s,.]{5,40}$/, // Letras, números, espacios, comas y puntos
    historia: /^[a-zA-Z0-9\s,.;+-_"']{20,}$/, // letras, números, símbolos, mínimo de 20 dígitos
    latlong: /[\-?\d+(\.\d+)?),\s*(\-?\d+(\.\d+)?)]$/, // Formato '12.2323,-1.53452' 
    descripcion: /^[a-zA-Z0-9\s,.;+-_"']{20,}$/, // Letras, números y espacios
    actividades: /^[a-zA-Z\s,]+$/, // Formato: surfear, escalar
    caracteristicas: /^[a-zA-Z\s,ñ]+$/ // Formato: playa, montaña
}

const campos = {
    nombre: false,
    historia: false,
    latlong: false,
    descripcion: false,
    actividades: false,
    caracteristicas: false
}

const validarFormulario = (e) => {
    switch(e.target.name){
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
            break;
        
        case "historia":
            validarCampo(expresiones.historia, e.target, 'historia');
            break;

        case "latlong":
            validarCampo(expresiones.latlong, e.target, 'latlong');
            break;
            
        case "descripcion":
            validarCampo(expresiones.descripcion, e.target, 'descripcion');
            break;

        case "actividades":
            validarCampo(expresiones.actividades, e.target, 'actividades');
            break;

        case "caracteristicas":
            validarCampo(expresiones.caracteristicas, e.target, 'caracteristicas');
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
		document.querySelector(`#grupo__${campo} .mensaje__error__p`).classList.remove('mensaje__error__p-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('grupo__inputs-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('grupo__inputs-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .mensaje__error__p`).classList.add('mensaje__error__p-activo');
		campos[campo] = false;
	}
}

/* Función para validar mientras va escribiendo */
inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario); /* Cuando se presiona una tecla */
    input.addEventListener('blur', validarFormulario); /* Cuando se presiona fuera del formulario */
});

textarea.forEach((textarea) => {
    textarea.addEventListener('keyup', validarFormulario); /* Cuando se presiona una tecla */
    textarea.addEventListener('blur', validarFormulario); /* Cuando se presiona fuera del formulario */
});

btn_confirmar.addEventListener('click', (e) => {
        
        if (campos.nombre && campos.historia && campos.latlong && campos.descripcion && campos.actividades && campos.caracteristicas){
            document.querySelectorAll('.grupo__inputs-correcto').forEach((icono) => {
                icono.classList.remove('grupo__inputs-correcto');
            });
            formulario.submit();
            formulario.reset(); 
        }else {
            document.getElementById('mensaje__error__vacios').classList.add('mensaje__error-activo');
    
            setTimeout(() => {
                document.getElementById('mensaje__error__vacios').classList.remove('mensaje__error-activo');
            },7000);
        };
    });