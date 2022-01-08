from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    nome = db.Column(db.String(64), index=True, unique=False)
    cognome = db.Column(db.String(64), index=True, unique=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Prenotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_cognome = db.Column(db.String(120), index=True)
    tel = db.Column(db.String(120), index=True)
    check_in = db.Column(db.Date, index=True)
    ospiti = db.Column(db.String(120), index=True)
    struttura = db.Column(db.String(120), index=True)
    user_email = db.Column(db.String(120), db.ForeignKey('user.email'))
    check_out = db.Column(db.Date, index=True)
    stanza = db.Column(db.String(120), index=True)

class N_email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_email = db.Column(db.String(120), index=True, unique=False)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


