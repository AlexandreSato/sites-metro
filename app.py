# Alexandre Nobuharu Sato em 30 de novembro de 2021, Ribeirão Pires - SP

import os

from flask import Flask, jsonify, render_template, url_for, request, redirect
from werkzeug.utils import redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from helpers import apology


database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
migrate = Migrate(app, db)
from models import Contratos # common for db interactions

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def api():
    contratos = Contratos.query.all()
    return jsonify(json_list = [i.serialize for i in contratos])

@app.route("/tabela")
def tabela():
    contratos = Contratos.query.all()
    return render_template("tabela.html", contratos=contratos)

@app.route("/lancar", methods=["GET", "POST"])
def lancar():
    if request.method == "POST":
        id = None
        contrato = request.form.get("contrato")
        fornecedor = request.form.get("fornecedor")
        objeto = request.form.get("objeto")
        valor = request.form.get("valor")
        mes = request.form.get("mes")

        lancamento = Contratos(id, contrato, fornecedor, objeto, valor, mes)
        db.session.add(lancamento)
        db.session.commit()
        return redirect("/tabela")
    else:
        return render_template("lancar.html")