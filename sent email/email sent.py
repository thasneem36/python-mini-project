import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv('PASSWORD')

senter_email = "thasneem9mt@gmail.com"
receiver_email = "thasneem9mt@gmail.com"

subject = "Python Email test case 2"
message = """
message is 
"""

text = f"Subject : {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)

server.starttls()
server.login(senter_email,password)

server.sendmail(senter_email,receiver_email,text)
print("email has been sent")