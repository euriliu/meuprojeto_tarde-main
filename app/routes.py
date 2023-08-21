from app import app, db, bcrypt
from flask import render_template,url_for,flash,redirect,request,session
from app.forms import Contato, Cadastro
from app.models import ContatoModels, CadastroModels
from flask_bcrypt import check_password_hash
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
        try:
            flash('Cadastrado com sucesso!!')
            nome = cadastro.nome.data
            email = cadastro.email.data
            senha = cadastro.senha.data
            contato = cadastro.contato.data
            hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
           
            novo_cadastro = CadastroModels(nome = nome, email = email, senha = hash_senha, contato = contato)
            db.session.add(novo_cadastro)
            db.session.commit()
        
        except Exception as e:
            flash('ocorreu um erro ao cadastrar! Entre em contato com o suporte!')
            print(str(e))

    return render_template('cadastro.html', title = 'Cadastro', cadastro = cadastro)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        user = CadastroModels.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.senha, senha):
            session['email'] = user.email
            session['nome'] = user.nome
            flash('Seja bem vindo!')
            time.sleep(2)
            return redirect(url_for('index'))
        else:
            flash('Senha ou email incorreto')
    
    return render_template('login.html', title='Login')


@app.route('/editar', methods=['GET', 'POST'])
def editar():
    if 'email' not in session:
        return redirect(url_for('login'))
    usuario = CadastroModels.query.filter_by(email = session['email']).first()
    if request.method == 'POST':
        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')
        senha = request.form.get('senha')
        usuario.senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        db.session.commit()
        flash('Seus dados foram atualizados com sucesso!')
    return render_template('editar.html', titulo = 'Editar', usuario = usuario)


@app.route('/sair')
def sair():
    session.pop('email',None)
    session.pop('nome',None)
    return redirect(url_for('login'))

