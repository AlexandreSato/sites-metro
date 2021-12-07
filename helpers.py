# Alexandre Nobuharu Sato, 6 de dezembro de 2021

"""função para converter valores decimais de ponto para vírgula"""
def brl(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

"""função para converter o objeto de sqlalchemy.query em uma lista iterável"""
row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
