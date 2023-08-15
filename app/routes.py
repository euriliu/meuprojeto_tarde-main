from app import app, db
from flask import render_template,url_for,flash,redirect,request
from app.forms import Contato, Cadastro
from app.models import ContatoModels, CadastroModels
import time

@app.route('/')
def index():
    return render_template('index.html', title = 'Inicio')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title ='Sobre')

@app.route('/contato', methods =['GET', 'POST'])
def contato():
    formulario = Contato()
    if formulario.validate_on_submit():
        flash('mensagem enviada com sucesso!!')
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        conteudo = formulario.conteudo.data

        novo_contato = ContatoModels(nome = nome, email = email, telefone = telefone, conteudo = conteudo)
        db.session.add(novo_contato)
        db.session.commit()


    return render_template('contato.html', title = 'contato', formulario = formulario)

@app.route('/projetos')
def projeto():
    return render_template('projeto.html', title ='Projetos')


@app.route('/cadastro', methods =['GET', 'POST'])
def cadastro():
    cadastro=Cadastro()
    if cadastro.validate_on_submit():
        flash('Cadastrado com sucesso!!')
        nome = cadastro.nome.data
        email = cadastro.email.data
        senha = cadastro.senha.data
        contato = cadastro.contato.data
        novo_cadastro = CadastroModels(nome = nome, email = email, senha = senha, contato = contato)
        db.session.add(novo_cadastro)
        db.session.commit()


    return render_template('cadastro.html', title = 'Cadastro', cadastro = cadastro)


@app.route('/login')
def login():
    return render_template('login.html', title ='Login')



