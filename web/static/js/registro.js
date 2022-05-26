/***********************************************************************/
/*********** INGRESO DE DATOS DEL FORMULARIO DE REGISTRO **************/
/*********************************************************************/
const formulario = document.getElementById('form_registro');
const inputs = document.querySelectorAll('#form_registro input');

/* Expresiones regulares para condicionar los campos del formulario */
const expresiones = {
    nombre: /^[a-zA-Z]{3,40}$/, // Letras
    apellido: /^[a-zA-Z]{3,16}$/, // Letras
    password: /^.{8,16}$/, // 8 a 16 digitos
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
    /*telefono: /^\d{7,9}$/ // 8 a 9 numeros*/
    /* Para crear servicios sirve */
}

const campos = {
    nombre: false,
    apellido: false,
    password: false,
    correo: false
}

/* Validando formulario*/
const validarFormulario = (e) => {
    switch (e.target.name) {
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
            break;

        case "apellido":
            validarCampo(expresiones.apellido, e.target, 'apellido');
            break;

        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
            validarCorreo2();
            break;

        case "confirmCorreo":
            validarCorreo2();
            break;

        case "password":
            validarCampo(expresiones.password, e.target, 'password');
            validarCorreo2();
            break;

        case "confirmPass":
            validarPassword2();
            break;
    }
}

/* Validando cada campo del formulario*/
const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
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

/* Validando coincidencia en confirmación de correo */
const validarCorreo2 = () => {
    const inputCorreo1 = document.getElementById('correo');
    const inputCorreo2 = document.getElementById('confirmCorreo');

    if (inputCorreo1.value !== inputCorreo2.value) {
        document.getElementById(`grupo__conf__correo`).classList.add('grupo__inputs-incorrecto');
        document.getElementById(`grupo__conf__correo`).classList.remove('grupo__inputs-correcto');
        document.querySelector(`#grupo__conf__correo i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__conf__correo i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__conf__correo .mensaje__error__p`).classList.add('mensaje__error__p-activo');
        campos['correo'] = false;
    } else {
        document.getElementById(`grupo__conf__correo`).classList.remove('grupo__inputs-incorrecto');
        document.getElementById(`grupo__conf__correo`).classList.add('grupo__inputs-correcto');
        document.querySelector(`#grupo__conf__correo i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__conf__correo i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__conf__correo .mensaje__error__p`).classList.remove('mensaje__error__p-activo');
        campos['correo'] = true;
    }
}

/* Validando coincidencia en confirmación de contraseña */
const validarPassword2 = () => {
    const inputPassword1 = document.getElementById('password');
    const inputPassword2 = document.getElementById('confirmPass');

    if (inputPassword1.value !== inputPassword2.value) {
        document.getElementById(`grupo__conf__password`).classList.add('grupo__inputs-incorrecto');
        document.getElementById(`grupo__conf__password`).classList.remove('grupo__inputs-correcto');
        document.querySelector(`#grupo__conf__password i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__conf__password i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__conf__password .mensaje__error__p`).classList.add('mensaje__error__p-activo');
        campos['password'] = false;
    } else {
        document.getElementById(`grupo__conf__password`).classList.remove('grupo__inputs-incorrecto');
        document.getElementById(`grupo__conf__password`).classList.add('grupo__inputs-correcto');
        document.querySelector(`#grupo__conf__password i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__conf__password i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__conf__password .mensaje__error__p`).classList.remove('mensaje__error__p-activo');
        campos['password'] = true;
    }
}

/* Función para validar el formulario */
inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario); /* Cuando se presiona una tecla*/
    input.addEventListener('blur', validarFormulario); /* Cuando se presiona fuera del formulario */
});


/*********** Condición para cuando se presiona el botón enviar ***********/
formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    if (campos.nombre && campos.apellido && campos.password && campos.correo) {
        document.getElementById('mensaje__exito__registro').classList.add('mensaje__exito-activo');
        document.querySelectorAll('.grupo__inputs-correcto').forEach((icono) => {
            icono.classList.remove('grupo__inputs-correcto');
        });

        function login() {
            window.location.href = "login";
        };

        setTimeout(() => {
            login();
            formulario.submit();
        }, 7000);

    } else {
        document.getElementById('mensaje__error__vacios').classList.add('mensaje__error-activo');

        setTimeout(() => {
            document.getElementById('mensaje__error__vacios').classList.remove('mensaje__error-activo');
        }, 7000);
    };
});