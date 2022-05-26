/****************************************************************************************************************/
/********************************  MOSTRANDO LOS MENSAJES DEL SERVIDOR  ****************************************/
/**************************************************************************************************************/
if (document.getElementById('mensaje__exito') != null) {
    document.getElementById('mensaje__exito').classList.add('mensaje__exito-activo');
    setTimeout(() => {
        document.getElementById('mensaje__exito').classList.remove('mensaje__exito-activo');
    }, 7000);
};

if (document.getElementById('mensaje__error') != null) {
    document.getElementById('mensaje__error').classList.add('mensaje__error-activo');

    const btn_activar = document.getElementById('btn__activar');
    const btn_no_activar = document.getElementById('btn__no__activar');

    var inactivo = document.getElementById('mensaje__error').textContent;

    if (inactivo.includes('inactivo')) {
        document.getElementById('registro__pass').classList.add('registro_pass-inactivo');
        document.getElementById('form__activar__cuenta').classList.add('form__activar__cuenta-activo');

        btn_no_activar.addEventListener('click', (e) => {
            document.getElementById('form__activar__cuenta').classList.remove('form__activar__cuenta-activo');
            document.getElementById('registro__pass').classList.remove('registro_pass-inactivo');
            document.getElementById('mensaje__error').classList.remove('mensaje__error-activo');
            document.getElementById('correo').value = '';
            document.getElementById('password').value = '';
        });

        btn_activar.addEventListener('click', (e) => {
            document.getElementById('mensaje__error').classList.remove('mensaje__error-activo');
        });

    } else {
        setTimeout(() => {
            document.getElementById('mensaje__error').classList.remove('mensaje__error-activo');
        }, 7000);
    };

};
