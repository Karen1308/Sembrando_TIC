/******************************************************************************************/
/***************** PASANDO LOS DATOS AL BOTÓN ELIMINAR ************************************/
/******************************************************************************************/
const nombre_usuario = document.getElementById('dato__usuario');
const titulo_ventana = document.getElementById('titulo__ventana');
const cuenta_eliminar = document.getElementById('eliminar_cuenta');
const ancla__delete = document.getElementById('ancla__delete');

function datos_usuario(correo) {
    if (nombre_usuario != null) {
        var nombre = nombre_usuario.textContent;
        titulo_ventana.textContent = titulo_ventana.textContent + nombre;
        cuenta_eliminar.textContent = cuenta_eliminar.textContent + correo + '?';
        ancla__delete.href = "/baja/" + correo;
    }
};

function mostrar_ventana(ventana) {
    ventana.classList.add('mostrar');
};

function cerrar_ventana(ventana) {
    ventana.classList.remove('mostrar');
};