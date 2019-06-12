import smtplib

EMAIL_ADDRESS = 'dudeindaegu@gmail.com'
EMAIL_PASSWORD = 'Tkdgkr92!'

# if the optional host and port parameters are given,
# the SMTP connect() method is called with those parameters
# during initialization.
# So here we are connecting to 'smtp.gmail.com', with port 587
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Hey this is a test EMail!'
    body = 'Is it working well?'

    message = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'dudeindaegu@gmail.com', message)
