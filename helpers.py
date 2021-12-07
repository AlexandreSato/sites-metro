# Alexandre Nobuharu Sato, 7 de dezembro de 2021

from flask import render_template, session, redirect
from functools import wraps


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


"""função para converter valores decimais de ponto para vírgula"""
def brl(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


"""função para converter o objeto de sqlalchemy.query em uma lista iterável"""
row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}


"""Render message as an apology to user."""
def apology(message, code=400):
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("oops.html", top=code, bottom=escape(message)), code
