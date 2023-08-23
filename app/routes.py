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

@app.route('/projeto2')
def projeto2():
    return render_template('projeto2.html', title = 'projeto2')

@app.route('/projeto1')
def projeto1():
    return render_template('projeto1.html', title = 'Projeto1')

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
            cpf = cadastro.cpf.data
            rua = cadastro.rua.data
            num = cadastro.num.data
            bairro = cadastro.bairro.data
            cidade = cadastro.cidade.data
            uf = cadastro.uf.data
            hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
            
            novo_cadastro = CadastroModels(nome = nome, email = email, senha = hash_senha, contato = contato, cpf =  cpf, rua = rua, num = num, bairro=bairro, cidade = cidade, uf = uf)
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
        session['email'] = usuario.email
        session['nome'] = usuario.nome
        session['senha'] = usuario.senha
        session['cpf'] = usuario.cpf
        session['contato'] = usuario.contato
        session['rua'] = usuario.rua
        session['num'] = usuario.num
        session['bairro'] = usuario.bairro
        session['cidade'] = usuario.cidade
        session['uf'] = usuario.uf
        db.session.commit()
        
        flash('Seus dados foram atualizados com sucesso!')
    return render_template('editar.html', titulo = 'Editar', usuario = usuario)


@app.route('/excluir_conta', methods=['GET'])
def excluir_conta():
    if 'email' not in session:
        return redirect(url_for('login'))
    usuario = CadastroModels.query.filter_by(email= session['email']).first()
    db.session.delete(usuario)
    db.session.commit()
    session.clear()
    flash('adeus ... queria dizer que foi bom ... mas não foi, muleke insuportavel')
    return redirect(url_for('cadastro'))







@app.route('/sair')
def sair():
    session.pop('email',None)
    session.pop('nome',None)
    session.pop('senha',None)
    session.pop('contato',None)
    return redirect(url_for('login'))

