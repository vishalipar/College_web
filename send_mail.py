import smtplib, ssl


def send_mail(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'patilv2942@gmail.com'
    password = 'qpnc wovs tkbm ayvp'

    receiver = 'patilv2942@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
