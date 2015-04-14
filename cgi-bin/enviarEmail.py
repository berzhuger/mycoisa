#!/Python27/python

import cgi
import cgitb
import smtplib
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields

gmail_user = "igornoia89@gmail.com"
gmail_pwd = "xubasafera"
FROM = 'igornoia89@gmail.com'
#TO = ['igornoia89@gmail.com', 'igor.v@outlook.com','robsonklein23@gmail.com'] #must be a list
TO = ['igornoia89@gmail.com'] #must be a list

SUBJECT = "Testing sending using gmail"
#TEXT = form.getvalue('mensagem')
#email = []
#email.append(form.getvalue('emailEnvio'))
#TO = email

TEXT = """
    Testing sending mail using gmail servers with python motherfucker
    eh ois charlinhos employ, pega o caraio do host la que vai bomba essa
    piroca loca de site."""

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
    #server = smtplib.SMTP(SERVER) 
    server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    #server.quit()
    server.close()
    print 'successfully sent the mail'
    #first_name = form.getvalue('first_name')
    #last_name = form.getvalue('last_name')
    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Hello - Second CGI Program</title>"
    print "</head>"
    print "<body>"
    print "<h2>email enviado</h2>"
    print "</body>"
    print "</html>"
except:
    print "failed to send mail"
