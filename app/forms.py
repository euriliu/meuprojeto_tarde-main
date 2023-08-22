from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TelField,TextAreaField,SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect


class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email',validators=[DataRequired()])
    telefone = TelField('telefone', validators=[DataRequired()])
    conteudo = TextAreaField('conteudo')
    enviar = SubmitField('Enviar')


class Cadastro(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email',validators=[DataRequired()])
    contato = TelField('telefone', validators=[DataRequired()])
    senha = PasswordField('senha',validators=[DataRequired()])
    cpf = StringField('cpf', validators=[DataRequired()])
    rua = StringField('rua', validators=[DataRequired()])
    num = StringField('num', validators=[DataRequired()])
    bairro = StringField('bairro', validators=[DataRequired()])
    cidade = StringField('cidade', validators=[DataRequired()])
    uf = StringField('uf', validators=[DataRequired()])
    enviar = SubmitField('Enviar')