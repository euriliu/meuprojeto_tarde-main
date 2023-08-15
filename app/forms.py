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
    enviar = SubmitField('Enviar')