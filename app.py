# Alexandre Nobuharu Sato em 06 de dezembro de 2021, Ribeirão Pires - SP
import os

from flask import Flask, jsonify, render_template, request, redirect, session, flash
from flask_session import Session
from werkzeug.utils import redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from tempfile import mkdtemp
from helpers import brl, row2dict, apology, login_required
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

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

# Custom filter
app.jinja_env.filters["brl"] = brl

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
migrate = Migrate(app, db)
from models import Contratos, ListaCNs, Usuarios # common for db interactions


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log User in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not (request.form.get("email") and request.form.get("senha")):
            return apology("faltou preencher algum campo", 400)
            
        email = request.form.get("email")
        senha = request.form.get("senha")
        user = Usuarios.query.filter_by(email=email).first()
        if user and (user.senha.strip() == senha.strip()):
            session["user_id"] = user.id
            flash (f"Bem vindo de volta {user.nome}")
            return render_template("index.html")
        else:
            flash ("email ou senha incorretos")
            return render_template("login.html")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/")
@login_required
def index():
    flash("Site em construção")
    return render_template("index.html")


@app.route("/api")
def api():
    contratos = Contratos.query.all()
    CONTRATOS = [row2dict(contrato) for contrato in contratos]
    return jsonify(CONTRATOS)
    # return jsonify(json_list = [i.serialize for i in contratos])


@app.route("/tabela")
@login_required
def tabela():
    contratos = Contratos.query.all()
    CONTRATOS = [row2dict(contrato) for contrato in contratos]
    for contrato in CONTRATOS:
        contrato["valor"] = brl(float(contrato["valor"]))
    return render_template("tabela.html", contratos=CONTRATOS)


@app.route("/lancar", methods=["GET", "POST"])
@login_required
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


@app.route("/lista_cns")
@login_required
def lista_cns():
    contratos = ListaCNs.query.all()
    CONTRATOS = [row2dict(contrato) for contrato in contratos]
    # for contrato in CONTRATOS:
    #     contrato["valor"] = brl(float(contrato["valor"]))
    return render_template("lista_cns.html", contratos=CONTRATOS)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)