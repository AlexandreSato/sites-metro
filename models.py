from app import db


class Contratos(db.Model):

    __tablename__ = 'contratos'
    id = db.Column(db.Integer, primary_key=True)
    contrato = db.Column(db.Integer())
    fornecedor = db.Column(db.String())
    objeto = db.Column(db.String())
    valor = db.Column(db.Integer())
    mes = db.Column(db.Integer())

    def __init__(self, id=None, contrato=None, fornecedor=None, objeto=None, valor=None, mes=None):
        self.id = id
        self.contrato = contrato
        self.fornecedor = fornecedor
        self.objeto = objeto
        self.valor = valor
        self.mes = mes

    @property
    def serialize(self):
        return {
            "id":self.id,
            "contrato":self.contrato,
            "fornecedor":self.fornecedor,
            "objeto":self.objeto,
            "valor":self.valor,
            "mes":self.mes
        }

# Controle de acesso
class Usuarios(db.Model):

    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    email = db.Column(db.String())
    senha = db.Column(db.Integer())

    def __init__(self, id=None, nome=None, email=None, senha=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha