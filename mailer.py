from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
def sendMyEmail(sender, recipient, subject, fname, lname, email, content):
    """
    Takes in email details to send an email to whoever.
    """
    message = f"""Message from {fname} {lname}: \n\n{content} \n\n
    Email: {email}
    """

    # Sendgrid client
    email = Mail(
        from_email=sender,
        to_emails=recipient,
        subject=subject,
        html_content=message
    )
    
    # Sending the email 
    response = sg.send(email)
    
    # Returning either a successful message or not
    if response.status_code==202:
        return "Email has been accepted!"
    
    return "Email wasn't sent"

