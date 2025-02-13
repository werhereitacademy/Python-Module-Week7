import smtplib  # Import the smtplib library to handle sending emails via SMTP
from email.mime.text import MIMEText  # Import MIMEText to create email text content
from email.mime.multipart import MIMEMultipart  # Import MIMEMultipart to create multipart email messages

def send_gmail(recipient_email, subject, body):
    """
    Function to send an email via Gmail.

    :param recipient_email: Recipient's email address (e.g., 'recipient@example.com')
    :param subject: Subject of the email
    :param body: Body content of the email
    :return: Returns True if successful, False if an error occurs.
    """

    sender_email = ""  # Sender's Gmail address (leave empty to be filled)
    sender_password = ""  # Sender's Gmail app password or account password (leave empty to be filled)

    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email  # Set the sender's email address
        msg['To'] = recipient_email  # Set the recipient's email address
        msg['Subject'] = subject  # Set the email subject

        # Attach the email body as plain text
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to Gmail's SMTP server on port 587
        server.starttls()  # Start TLS encryption for a secure connection
        server.login(sender_email, sender_password)  # Log in to the sender's Gmail account
        text = msg.as_string()  # Convert the email message to a string
        server.sendmail(sender_email, recipient_email, text)  # Send the email
        server.quit()  # Disconnect from the SMTP server
        print('Email sent successfully!')  # Print success message
        return True  # Return True to indicate success
    except Exception as e:
        print(f'An error occurred while sending the email: {e}')  # Print error message if an exception occurs
        return False  # Return False to indicate failure

# # Örnek kullanım
# sender_email = 'your_email@gmail.com'  # Gönderenin Gmail adresi
# sender_password = 'your_app_password'  # Gönderenin uygulama şifresi
# recipient_email = 'recipient@example.com'  # Alıcının e-posta adresi
# subject = 'Python ile Gmail Gönderme'
# body = 'Bu bir test e-postasıdır.'

# # Fonksiyonu çağır
# send_gmail(sender_email, sender_password, recipient_email, subject, body)