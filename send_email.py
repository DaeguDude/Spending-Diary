# Import smtplib module
import smtplib

EMAIL_ID = 'PUT YOUR EMAIL ADDRESS'

# If you created an app password, put 16 digits generated password
# that you were given to 'EMAIL_PW'
EMAIL_PW = 'PUT YOUR PASSWORD'


# Opening the connection
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    # Put SMTP connection in TLS mode
    smtp.starttls()
    
    # Identify yourself since you've put connection in TLS mode
    smtp.ehlo()

    # Login with your ID and PASSWORD
    smtp.login(EMAIL_ID, EMAIL_PW)

    subject = "This is a test"
    body = "This is working? YAY!"

    # If you don't know this form of string, look up 'f string'
    msg = f'Subject: {subject}\n\n{body}'

    # smtp.sendmail(SENDER, RECEIVER, MESSAGE)
    smtp.sendmail(EMAIL_ID, EMAIL_ID, msg)
