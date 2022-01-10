from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm,  RegistrationForm, PrenotationForm, Newsform
from flask_login import current_user, login_user
from app.models import User, Prenotation, N_email
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.email import send_email, send_emailN


@app.route('/')
def redir():
    return redirect(url_for('index'))

#funzione di visualizzazione dell'index(pagina principale)
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Newsform() #form per la newsletter
    if form.validate_on_submit():
        # inserimento della mail nel database
        n_email = N_email(news_email=form.news_email.data)
        send_emailN()
        db.session.add(n_email)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', title='Email', form=form)

#funzione di visualizzazione del login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm() #form per il login
    if form.validate_on_submit():
        # controllo all'interno del database per vedere se l'utente è registrato
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Username o password non validi')
            return redirect(url_for('login'))
        # function di Flask-Login che imposterà l'utente come loggato (la variabile current_user sarà attiva sulle pagine future)
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        # se l'URL login non ha l'argomento "next" allora si viene reindirizzati all'index
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

#funzione di visualizzazione del logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#funzione di visualizzazione della registrazione
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm() #form della registrazione
    if form.validate_on_submit():
        # salvataggio dell'utente nel database
        user = User(username=form.username.data, email=form.email.data, nome=form.nome.data, cognome=form.cognome.data )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulazioni, sei registrato!')
        # reindirizzamento alla pagina di login
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#funzione di visualizzazione della registrazione
@app.route('/Prenot', methods=['GET', 'POST'])
def Prenot():
    form = PrenotationForm() #form della prenotazione
    if form.validate_on_submit():
        # creazione di una prenotazione
        prenotation = Prenotation(nome_cognome=form.nome_cognome.data, tel=form.tel.data, check_in=form.check_in.data,
                                  ospiti=form.ospiti.data, struttura=form.struttura.data, user_email=form.email.data,
                                  check_out=form.check_out.data, stanza=form.stanza.data)
        # gestione degli errori
        if form.struttura.data == 'Struttura' or form.ospiti.data == 'Numero di ospiti' or form.stanza.data == 'Tipo di camera':
            flash('seleziona opzioni valide')
            return redirect(url_for('Prenot'))

        if form.check_in.data>form.check_out.data:
            flash('Date non valide')
            return redirect(url_for('Prenot'))
        # salvataggio della prenotazione nel database
        send_email()
        db.session.add(prenotation)
        db.session.commit()

        return redirect(url_for('Success'))
    return render_template('Prenot.html', title='Prenotazione', form=form)



#funzione di visualizzazione della pagina di visualizzazione della città di Napoli
@app.route('/Describe1')
def Describe1():
      return render_template('Describe1.html')

#funzione di visualizzazione della pagina che indica che la prenotazione è stata effettuata con successo
@app.route('/Succes')
def Success():
    return render_template('Success.html')

