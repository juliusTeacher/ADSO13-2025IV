import sqlite3

from flask import Flask, g, jsonify, request

app = Flask(__name__)


#-- Conexion a SQLite --
def bd_conexion():
    try:
        if'conexion' not in g:
            g.conexion = sqlite3.connect("E:/ADSO-13/clinica/clinica.db")
        return g.conexion
    except Exception:
        return 'No hay conexión con la base de datos'

def cerrar_bd():
    conexion = g.pop('conexion', None)
    if conexion is not None:
        conexion.close()



@app.route('/')
def index():
    return '<h1>Es una prueba inicial para desarrollar el sistema HOSPITAL</h1>'

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        sqlString = "SELECT * FROM usuario"
        conexion = bd_conexion()
        cursor = conexion.cursor()
        cursor.execute(sqlString)
        datos = cursor.fetchall()
        usuarios = []
        for fila in datos:
            user = {'id_usuario': fila[0], 'nombres': fila[1], 'direccion': fila[2], 'telefono': fila[3], 'email': fila[4]}
            usuarios.append(user)
        return jsonify({'usuarios': usuarios, 'mensaje': 'Usuarios en línea'})
    except Exception:
        return jsonify({'mensaje': 'Error'})
    finally:
        cerrar_bd()
        
@app.route('/usuarios', methods=['POST'])
def registrar_usuario():
    try:
        conexion = bd_conexion()
        cursor = conexion.cursor()
        sqlString = """INSERT INTO usuario(id_usuario, nombres, direccion, telefono, email)
        VALUES({0},'{1}','{2}',{3},'{4}')""".format(request.json['id_usuario'], request.json['nombres'],
                                             request.json['direccion'], request.json['telefono'],
                                             request.json['email'])
        cursor.execute(sqlString)
        conexion.commit()
        return jsonify({'mensaje': 'Usuario registrado'})
    except Exception:
        return jsonify({'mensaje': 'Error'})
    finally:
        cerrar_bd()


@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def listar_usuarios_id(id_usuario):
    try:
        conexion = bd_conexion()
        cursor = conexion.cursor()
        sqlString = "SELECT * FROM usuario WHERE id_usuario = '{0}'".format(id_usuario)
        cursor.execute(sqlString)
        datos = cursor.fetchone()
        if(datos != None):
            user = {'id_usuario': datos[0], 'nombres': datos[1], 'direccion': datos[2], 'telefono': datos[3], 'email': datos[4]}
            return jsonify({'usuarios': user, 'mensaje': 'Usuarios en lista'})
        else:
            return jsonify({'mensaje': 'Usuario no encontrado'})
    except Exception:
        return jsonify({'mensaje': 'Error'})
    finally:
        cerrar_bd()
        
@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    try:
        conexion = bd_conexion()
        cursor = conexion.cursor()
        sqlString = """UPDATE usuario SET nombres = '{0}', direccion = '{1}', telefono = {2}, email = '{3}'
        WHERE id_usuario = '{4}'""".format(request.json['nombres'], request.json['direccion'], 
                                           request.json['telefono'], request.json['email'], request.json['id_usuario'])
        cursor.execute(sqlString)
        conexion.commit()
        return jsonify({'mensaje': 'Usuario actualizado'})
    except Exception:
        return jsonify({'mensaje': 'Error'})
    finally:
        cerrar_bd()

@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    try:
        conexion = bd_conexion()
        cursor = conexion.cursor()
        sqlString = "DELETE FROM usuario WHERE id_usuario = '{0}'".format(id_usuario)
        cursor.execute(sqlString)
        conexion.commit()
        return jsonify({'mensaje': 'Usuario eliminado'})
    except Exception:
        return jsonify({'mensaje': 'Error'})
    finally:
        cerrar_bd()

if(__name__ == '__main__'):
    app.run(debug=True)