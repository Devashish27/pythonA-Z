import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)  # Here smtp along with portno..!

server.starttls()  # Here tls = transport layer security.!

server.login('newbietesting007@gmail.com', 'Rajanadhikipoleda007')

server.sendmail('newbietesting007@gmail.com', 'kayrakyzaghan11turkishgods.com@gmail.com', 'Hello newbie mail has been sent')  # Here we are specifying sender and receiver of the mail...!!

print('Mail Sent!!')
