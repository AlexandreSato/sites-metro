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

    """Serializador ensinado por Thais Akemi Fatec Paula Souza"""
    # @property
    # def serialize(self):
    #     return {
    #         "id":self.id,
    #         "contrato":self.contrato,
    #         "fornecedor":self.fornecedor,
    #         "objeto":self.objeto,
    #         "valor":self.valor,
    #         "mes":self.mes
    #     }


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


# Lista de contratos
class ListaCNs(db.Model):

    __tablename__ = 'lista_cns'
    id = db.Column(db.Integer, primary_key=True)
    cn = db.Column(db.Integer())
    empresa = db.Column(db.String())
    objeto = db.Column(db.String())
    data_termino = db.Column(db.String())
    analista = db.Column(db.String())
    substituto = db.Column(db.String())
    coordenadoria = db.Column(db.String())
    alias = db.Column(db.String())

    def __init__(self, id=None, cn=None, empresa=None, objeto=None, data_termino=None, analista=None, substituto=None, coordenadoria=None, alias=None):
        self.id = id
        self.cn = cn
        self.empresa = empresa
        self.objeto = objeto
        self.data_termino = data_termino
        self.analista = analista
        self.substituto = substituto
        self.coordenadoria = coordenadoria
        self.alias = alias
