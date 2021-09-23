import os
import smtplib

server=smtplib.SMTP_SSL('smtp.gmail.com',465)


server.login('example@gmail.com',"password")
email=input("Enter the email address :")

subject='This is s Test Email'
body='Email is sent from using python program'

msg=f'subject:{subject}\n\n{body}'
server.sendmail('example@gmail.com',email,msg)
server.quit()

#Shows an error at output that usernme and password are not accepted, change your gmail settings ad allow access to all apps

