var btn_sugerencia = 0;
var btn_usuarios = 0;

function mostrar_ventana(ventana) {
    var ventana_clases = ventana.classList;

    if (ventana_clases.contains('mostrar_2')) {
        ventana.classList.remove('mostrar_2');
    } else {
        ventana.classList.add('mostrar_2');
    };
};

function mostrar_opciones (ventana, boton) {
    var botones = document.querySelectorAll(".btn_opcion");
    for (var i = 0; i < botones.length; i++) {
        botones[i].classList.remove('btn_opcion-activo');
    }

    var ventanas = document.querySelectorAll(".opciones");
    for (var i = 0; i < ventanas.length; i++) {
        ventanas[i].classList.remove('mostrar_2');
    }

    boton.classList.add('btn_opcion-activo');
    ventana.classList.add('mostrar_2');
}