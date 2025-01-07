import smtplib
from email.mime.text import MIMEText
from mcstatus import JavaServer
from csv import reader

with open('email_credentials.csv', 'r') as credentials_obj, open('hosts.csv', 'r') as hosts_obj:
    credentials_reader = reader(credentials_obj)
    credentials_list_rows = list(credentials_reader)
    credentials_rows = len(credentials_list_rows) - 1

    hosts_reader = reader(hosts_obj)
    hosts_list_rows = list(hosts_reader)
    hosts_rows = len(hosts_list_rows)
    
    subject = "Minecraft Server Outage"
    sender_email = credentials_list_rows[credentials_rows][0]
    sender_password = credentials_list_rows[credentials_rows][1]
    recipient_email = credentials_list_rows[credentials_rows][2]

    def send_email(subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Message sent!")

    def check_server_status(server_address):
        try:
            server = JavaServer.lookup(server_address)
            status = server.status()
            print(f"{server_address} is online. Players: {status.players.online}/{status.players.max}")
        except Exception as e:
            print(f"{server_address} is offline or unreachable. Error: {e}")
            body = f"{server_address} is offline or unreachable. Error: {e}"
            send_email(subject, body, sender_email, recipient_email, sender_password)
    
    while hosts_rows >= 2:
        hosts_rows = hosts_rows - 1
        server = hosts_list_rows[hosts_rows][0]
        check_server_status(server)