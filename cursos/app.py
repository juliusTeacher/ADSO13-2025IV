import sqlite3

from flask import Flask, g, render_template, request, redirect, url_for

app = Flask(__name__)

#---- Conexion a la base de datos: SQLite ----
def sql_connection():
    try:
        if 'con' not in g:
            g.con = sqlite3.connect("C:/Users/DELL/Documents/ADSO-13/cursos/database/cursos.db")
        return g.con
    except Exception as Error:
        print(Error)

def close_db():
    con = g.pop('con', None)
    if con is not None:
        con.close()

#---- Fin a la conexión con SQLite ----


@app.route('/cursos/add')
def add_curso():
    return render_template('cursos.html')

#-- Manejo de los endpoints (rutas)

#-- Listar cursos
@app.route('/', methods=['GET', 'POST'])
def listar_cursos():
    con = sql_connection()
    cursor = con.cursor()
    
    if request.method == 'POST' and 'txtCodigo' in request.form:
        sqlString = "SELECT * FROM curso WHERE idCurso LIKE '%" + request.form['txtCodigo'] + "%'"
    else:
        sqlString = "SELECT * FROM curso"
    
    cursor.execute(sqlString)
    datos = cursor.fetchall()
    con.close()
    return render_template('lista.html', cursos=datos)

#-- Agregar cursos
@app.route('/cursos/add', methods=['POST'])
def guardar_cursos():
    codigo = request.form['txtCodigo']
    nombre = request.form['txtNombre']
    creditos = request.form['txtCreditos']
    
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute("INSERT INTO curso(idCurso, nomCurso, creditos) VALUES(?,?,?)",(codigo, nombre, creditos))
    con.commit()
    con.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)