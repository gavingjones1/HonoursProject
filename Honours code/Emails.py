#Email script, reads in given email addr, password and imap/smap url.
#Sends email, waits, recieves email then deletes contents of inbox.

import imaplib, smtplib, email, time

user = 'userinthecrypt@gmail.com'
password = ''
imap_url = 'imap.gmail.com'
smtp_url = 'smtp.gmail.com'
###### sending email

def sendEmailKey():
    
    content = 'Subject: Subject 1 \n\n This is the first email'

    mail = smtplib.SMTP(smtp_url, 587)

    mail.ehlo()

    mail.starttls()

    mail.login(user,password)

    mail.sendmail(user, user, content)

def sendEmailPhish():

    content = 'Subject: Subject 2 \n\n This is the second email'

    mail = smtplib.SMTP(smtp_url, 587)

    mail.ehlo()

    mail.starttls()

    mail.login(user,password)

    mail.sendmail(user, user, content)

def sendEmailRans():

    content = 'Subject: Subject 3 \n\n This is the third email'

    mail = smtplib.SMTP(smtp_url, 587)

    mail.ehlo()

    mail.starttls()

    mail.login(user,password)

    mail.sendmail(user, user, content)

###### recieving email

def get_body(msg):

    #detects if multiple parts to email
    if msg.is_multipart():
        #if theres multiple payloads, get the first one
        return get_body(msg.get_payload(0))
        print('Multiple parts')
    else:
        return msg.get_payload(None,True)
        return True


def recieveEmail1():
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    con.select('INBOX')

    result, data  = con.fetch(b'1','(RFC822)')
    time.sleep(10)
    raw = email.message_from_bytes(data[0][1])
    print(get_body(raw))
    if True:
        print('First email has been recieved')

def recieveEmail2():
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    con.select('INBOX')

    result, data  = con.fetch(b'2','(RFC822)')
    time.sleep(10)
    raw = email.message_from_bytes(data[0][1])
    print(get_body(raw))
    if True:
        print('Second email has been recieved')

def recieveEmail3():
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    con.select('INBOX')

    result, data  = con.fetch(b'3','(RFC822)')
    time.sleep(10)
    raw = email.message_from_bytes(data[0][1])
    print(get_body(raw))
    if True:
        print('Third email has been recieved')

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


