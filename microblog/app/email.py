from flask_mail import Message
from app import mail
from app.forms import PrenotationForm, Newsform


def send_email():
    form = PrenotationForm()
    msg = Message('prenotazione effettuta', sender='MAIL_USERNAME', recipients=[form.email.data])
    msg.body = 'xyz'
    msg.html = '<div> Lo staff di BnB ilsole le comunica che la sua prenotazione è stata effettuata con successo. </div>'
    mail.send(msg)

def send_emailN():
    form = Newsform()
    msg = Message('Iscrizione newsletter', sender='MAIL_USERNAME', recipients=[form.news_email.data])
    msg.body = 'xyz'
    msg.html = '<div> Congratulazioni sei iscritt* alla newsletter. </div>'
    mail.send(msg)

