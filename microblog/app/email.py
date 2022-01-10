from flask_mail import Message
from app import mail
from app.forms import PrenotationForm, Newsform

#function per l'invio della mail a chi effettua alla prenotazione
def send_email():
    form = PrenotationForm()#form della prenotazione
    #la mail viene inviata dalla nostra email a quella inserita durante la prenotazione
    msg = Message('prenotazione effettuta', sender='MAIL_USERNAME', recipients=[form.email.data])
    msg.body = 'xyz'
    # corpo della mail
    msg.html = '<div> Lo staff di BnB ilsole le comunica che la sua prenotazione è stata effettuata con successo. </div>'
    mail.send(msg)

#function per l'invio della mail a chi si registra alla newsletter
def send_emailN():
    form = Newsform() #form della newsletter
    # la mail viene inviata dalla nostra email a quella inserita durante la registrazione
    msg = Message('Iscrizione newsletter', sender='MAIL_USERNAME', recipients=[form.news_email.data])
    msg.body = 'xyz'
    # corpo della mail
    msg.html = '<div> Congratulazioni sei iscritt* alla newsletter. </div>'
    mail.send(msg)

