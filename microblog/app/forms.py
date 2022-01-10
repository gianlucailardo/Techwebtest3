from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, N_email, Prenotation

#form del login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Accedi')

#form della registrazione
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    cognome = StringField('Cognome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrati')

    # function che controlla se l'username inserito è già presente nel database
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    # function che controlla se l'email inserita è già presente nel database
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

#form della prenotazione
class PrenotationForm(FlaskForm):
    nome_cognome = StringField('Nome e cognome', validators=[DataRequired()])
    tel = StringField('Numero di telefono', validators=[DataRequired()])
    check_in = DateField('Check in', format='%Y-%m-%d')
    # attraverso il selectfield viene implementato il menu a tendina
    ospiti = SelectField('Numero di ospiti', choices=[("Numero di ospiti","Numero di ospiti"),('1', '1'), ('2', '2'), ('3', '3'), ('4+', '4+')], validators=[DataRequired()])
    struttura = SelectField('Struttura', choices=[("Struttura","Struttura"),('Napoli', 'Napoli'), ('Roma', 'Roma'), ('Firenze', 'Firenze'),
                                                   ('Milano', 'Milano'), ('Oristano', 'Oristano'), ('Palau', 'Palau'),
                                                   ('Sorrento', 'Sorrento'), ('Venezia', 'Venezia')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    check_out = DateField('Check out', format='%Y-%m-%d')
    stanza = SelectField('Tipo di camera', choices=[("Tipo di camera","Tipo di camera"),('Camerata', 'Camerata'), ('Camera singola', 'Camera singola'),
                                                    ('Camera doppia', 'Camera doppia'), ('Camera familiare', 'Camera familiare')], validators=[DataRequired()])
    submit = SubmitField('Prenota')

#form della newsletter
class Newsform (FlaskForm):
    news_email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Iscriviti')
