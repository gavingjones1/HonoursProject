#Email script, reads in given email addr, password and imap/smap url.
#Sends email, waits, recieves email then deletes contents of inbox.

import imaplib, smtplib, email, time

user = 'it@room42.lu'
password = 'QQfrtgHHvv'
imap_url = 'dt.room42.lu'
smtp_url = 'dt.room42.lu'
###### sending email

def sendEmail():

    content = 'sample email'

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


def recieveEmail():
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    con.select('INBOX')

    result, data  = con.fetch(b'1','(RFC822)')
    time.sleep(10)
    raw = email.message_from_bytes(data[0][1])
    print(get_body(raw))
    if True:
        print('emails can be sent and recieved')

###### delete files
def deleteEmail():
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    con.select('INBOX')
    typ, data = con.search(None, 'ALL')
    for num in data[0].split():
        con.store(num, '+FLAGS', '\\Deleted')
    con.expunge()
    con.close()

sendEmail()
recieveEmail()

