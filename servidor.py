from flask import Flask, request
from servicios.autenticacion import autenticacion

app = Flask(__name__)


@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuarios = request.get_json()
    if 'correo' not in datos_usuarios:
        return 'El correo es obligatorio', 412

    if 'password' not in datos_usuarios:
        return 'La contraseña es obligatoria', 412

    autenticacion.crear_usuario(datos_usuarios['correo'], datos_usuarios['password'], datos_usuarios['nombre'], datos_usuarios['apellido'], datos_usuarios['tipo'])
    return 'OK', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
