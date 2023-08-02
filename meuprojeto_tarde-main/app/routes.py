from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', title = 'Inicio')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title ='Sobre')

@app.route('/contato')
def contato():
    return render_template('contato.html', title ='Contato')

@app.route('/projetos')
def projeto():
    return render_template('projeto.html', title ='Projetos')
