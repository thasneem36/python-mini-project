import imaplib
import email
import time

imap_server = "imap.gmail.com"
email_address = "thasneem9mt@gmail.com"
password = input("pass : ")

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

status, msgnums = imap.search(None, "ALL")

# Reverse the order of message numbers
msgnums = msgnums[0].split()[::-1]

for msgnum in msgnums:
    status, data = imap.fetch(msgnum, "(RFC822)")
    
    message = email.message_from_bytes(data[0][1])
    time.sleep(1)
    print("__________________________________")
    print(f"Message Number: {msgnum.decode()}")
    print(f"Date: {message.get('Date')}")
    print(f"{message.get('From')}||\t||{message.get('Subject')}")
    print("__________________________________")
    print()
    # print(f"To: {message.get('To')}")
    # print(f"BCC: {message.get('BCC')}")
    # print(f"Subject: {message.get('Subject')}")
    print()
    time.sleep(1)
    # print("Content:")
    
    # for part in message.walk():
    #     if part.get_content_type() == "text/plain":
    #         charset = part.get_content_charset()
    #         if charset is None:
    #             charset = 'utf-8'
    #         content = part.get_payload(decode=True).decode(charset, errors='replace')
    #         print(content)
    
    # print()

imap.close()
imap.logout()
