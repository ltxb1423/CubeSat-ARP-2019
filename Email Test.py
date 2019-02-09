import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = '<email address here>'
email_send = '<email address here>'
subject = 'Images'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

content = 'Images'
msg.attach(MIMEText(content,'plain'))


try: 
    filename = 'Photo.png'
    attachment = open(filename,'rb')
    print(filename+" successfully loaded.")
except:
    print(filename+ " could not be loaded.")

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content Desposition',"attachment; filename= "+filename)


msg.attach(part)
text = msg.as_string()


mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()
try:
    mail.starttls()
    mail.login(email_user,'<password here>')
    print("Log in success.")
except:
    print("Log in failure.")
    
for i in range (1,2):
    try:
        mail.sendmail(email_user,email_send, text)
        print("Message sent successfully.")
    except:
        print("Error! Message not sent.")

mail.quit()
mail.close()

