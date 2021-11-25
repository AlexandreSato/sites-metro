from app import db


class Contratos(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'contratos'
    id = db.Column(db.Integer, primary_key=True)
    contrato = db.Column(db.Integer))
    fornecedor = db.Column(db.String(50))
    objeto = db.Column(db.String(255))
    valor = db.Column(db.Integer))
    mes = db.Column(db.Integer))

    def __init__(self, name=None, email=None):
        self.contrato = contrato
        self.fornecedor = fornecedor
        self.objeto = objeto
        self.valor = valor
        self.mes = mes