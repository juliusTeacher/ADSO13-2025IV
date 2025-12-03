from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<nombre>')
def render(nombre=None):
    return render_template('index.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)