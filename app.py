# Alexandre Nobuharu Sato em 30 de novembro de 2021, Ribeirão Pires - SP

import os

from flask import Flask, jsonify, render_template, url_for, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def api():
    from models import Contratos
    contratos = Contratos.query.all()
    return jsonify(json_list = [i.serialize for i in contratos])

@app.route("/tabela", methods=["GET", "POST"])
def tabela():
    from models import Contratos
    contratos = Contratos.query.all()
    return render_template("tabela.html", contratos=contratos)
