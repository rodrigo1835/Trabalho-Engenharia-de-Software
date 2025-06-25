from . import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    senha = db.Column(db.String(100))
    feiras = db.relationship('Feira', backref='criador')
    expositores = db.relationship('Expositor', backref='criador')
    produtos = db.relationship('Produto', backref='criador')
    ingressos = db.relationship('Ingresso', backref='criador')

class Feira(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.Text)
    data_inicio = db.Column(db.Date)
    data_fim = db.Column(db.Date)
    local = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(2))
    criador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    expositores = db.relationship('Expositor', backref='feira', cascade='all, delete')

class Expositor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.Text)
    contato = db.Column(db.String(100))
    feira_id = db.Column(db.Integer, db.ForeignKey('feira.id'))
    criador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    produtos = db.relationship('Produto', backref='expositor', cascade='all, delete')

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.Text)
    preco = db.Column(db.Float)
    expositor_id = db.Column(db.Integer, db.ForeignKey('expositor.id'))
    criador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Ingresso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50))
    data_emissao = db.Column(db.Date, default=datetime.utcnow)
    feira_id = db.Column(db.Integer, db.ForeignKey('feira.id'))
    criador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    feira = db.relationship('Feira')
