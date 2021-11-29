# Alexandre Nobuharu Sato em 26 de novembro de 2021, Ribeirão Pires - SP
# exemplo obtido com Thais Akemi (thais.itocazu@fatec.sp.gov.br) em: https://www.youtube.com/watch?v=fkHkE4gZZVE

import os

from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# src: https://github.com/Azure-Samples/flask-postgresql-app
database_uri = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

app = Flask(__name__)
app.config["DEBUG"] = True
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)

Base = declarative_base()

class Data(Base):
    __tablename__ = 'contratos'
    id = Column(Integer(), primary_key=True)
    contrato = Column(Integer())
    fornecedor = Column(String())
    objeto = Column(String())
    valor = Column(Integer())
    mes = Column(Integer())

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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def api():
    todos_contratos = db.session.query(Data)
    return jsonify(json_list = [i.serialize for i in todos_contratos.all()])

@app.route("/tabela", methods=["GET", "POST"])
def tabela():
    toodos_contratos = db.session.query(Data)
    toodos_contratos = [i.serialize for i in toodos_contratos.all()]
    return render_template("tabela.html", contratos=toodos_contratos)
