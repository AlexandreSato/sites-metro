# Alexandre Nobuharu Sato em 30 de novembro de 2021, Ribeirão Pires - SP
import os

from flask import Flask, jsonify, render_template, request, redirect, session, flash
from flask_session import Session
from werkzeug.utils import redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from tempfile import mkdtemp

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    TEMPLATES_AUTO_RELOAD = True,
    SECRET_KEY = os.environ["SECRET_KEY"],

    # Configure session to use filesystem (instead of signed cookies)
    SESSION_FILE_DIR = mkdtemp(),
    SESSION_PERMANENT = False,
    SESSION_TYPE = "filesystem"
)
Session(app)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
migrate = Migrate(app, db)
from models import Contratos, Usuarios # common for db interactions


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # TODO
        if not (request.form.get("nome") and request.form.get("email") and request.form.get("senha")):
            flash ("Miss someting")
            return render_template("login.html")
        usuario = request.form.get("nome")
        usuario = Usuarios.query.filter_by(nome=usuario)
        return render_template("usuarios.html", usuarios=usuario)
    else:
        return render_template("login.html")

@app.route("/")
def index():
    flash("Site em construção")
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