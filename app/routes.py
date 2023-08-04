from app import app
from flask import render_template,url_for,flash,redirect,request
from app.forms import Contato
import time

@app.route('/')
def index():
    return render_template('index.html', title = 'Inicio')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title ='Sobre')

@app.route('/contato', methods =['GET', 'POST'])
def contato():
    dados_formulario = None
    formulario = Contato()
    if request.method == 'POST':
        flash('mensagem enviada com sucesso!!')
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        conteudo = request.form.get('contato')

        dados_formulario = {
            'nome':nome,
            'email':email,
            'telefone':telefone,
            'conteudo':conteudo 
        }
    return render_template('contato.html', title = 'contato', formulario = formulario, dados_formulario = dados_formulario)
@app.route('/projetos')
def projeto():
    return render_template('projeto.html', title ='Projetos')

