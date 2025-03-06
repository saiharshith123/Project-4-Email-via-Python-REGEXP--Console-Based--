import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

x = True
while x:
    pattern = re.compile(r'^[A-Za-z ]+')
    text = input("Enter Name: ")
    matches = pattern.fullmatch(text)
    if matches != None: 
        name = matches.group()
        x = False
    else:
        print("Enter Name in correct format")
print(f"name: {name}")

x = True
while x:
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    dob1 = input("Enter Date of Birth (dd-mm-yyyy): ")
    matches = pattern.fullmatch(dob1)
    if matches != None:
        dob = matches.group()
        x = False
    else:
        print("Enter DOB in correct format")
print(f"Dob: {dob}")

x = True
while x:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    phone1 = input("Enter Mobile Number: ")
    matches = pattern.fullmatch(phone1)
    if matches != None:
        phone = matches.group()
        x = False
    else:
        print("Enter Mobile in correct format")
print(f"Phone: {phone}")
insta = input("Enter Insta Id: ")
print(f"Insta Id: {insta}")

x = True
while x:
    pattern = re.compile(r'^[a-zA-Z0-9]*+@gmail.com\Z')
    email1 = input("Enter Email: ")
    matches = pattern.fullmatch(email1)
    if matches != None:
        email = matches.group()
        x = False
    else:
        print("Enter Email in correct format")
print(f"Email: {email}")

sub = "Your Profile Details"
body = f"""
Name: {name}
Date of Birth: {dob}
Phone: {phone}
Instagram Id: {insta}
Email: {email}
"""
msg = MIMEMultipart()
msg['From'] = "bachina123456789@gmail.com"
msg['To'] = email
msg['Subject'] = sub
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("bachina123456789@gmail.com", "wxku ntdz virr qyjf")  
    server.send_message(msg)
    server.quit()
    print(f"Email sent successfully to {email}")
    print(f"Thank You")
except Exception as e:
    print(f"Error sending email: {e}")
    
