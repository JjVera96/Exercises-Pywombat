from smtplib import SMTP

email = input("Destinatario: ")
subject = input("Título del correo: ")
body = input("Contenido: ")

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

if len(body) > 30:
    print("El cuerpo del correo, supera los 30 caracteres")
else:
    msg = "From: {}\r\nTo: {}\r\nSubject: {}\r\n{}".format(EMAIL_HOST_USER, email, subject, body)
    server = SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(EMAIL_HOST_USER, email, msg)
    server.quit()