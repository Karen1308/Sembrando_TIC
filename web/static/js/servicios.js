const servicio_recomendado = document.getElementById('recomendado');

if (servicio_recomendado != null){
    var valor_sr = servicio_recomendado.textContent;
    if (valor_sr == 1) {
        document.getElementById('serv__recomendado').classList.add('serv__recomendado-inactivo');
    };
};
