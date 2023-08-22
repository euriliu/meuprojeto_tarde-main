from app import app,db
class ContatoModels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    telefone = db.Column(db.String(14), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Contato{self.nome}>'

class CadastroModels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique = True)
    senha = db.Column(db.String(12), nullable=False)
    contato = db.Column(db.String(10), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique = True)
    rua = db.Column(db.String(30), nullable=False)
    num = db.Column(db.String(30), nullable=False)
    bairro = db.Column(db.String(30), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    uf = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return 'Cadastro'

