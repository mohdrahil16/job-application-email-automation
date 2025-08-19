

import smtplib
from email.message import EmailMessage
import logging
from pathlib import Path

# -----------------------------
# Step 0: Pre-defined Credentials
# -----------------------------
EMAIL_ADDRESS = 'email'
EMAIL_PASSWORD = 'passsword'  # Use Gmail App Password for 2FA

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(filename='email_log.txt', 
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# -----------------------------
# Step 1: Inputs
# -----------------------------
def get_hr_emails():
    emails = input("Enter HR email(s), separated by comma: ").split(',')
    return [email.strip() for email in emails]

# -----------------------------
# Step 2: Email content
# -----------------------------
def create_email(sender_email, recipient_email, subject, body, resume_path):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(body)

    # Attach Resume
    if Path(resume_path).is_file():
        with open(resume_path, 'rb') as f:
            file_data = f.read()
            file_name = Path(resume_path).name
            msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)
    else:
        logging.warning(f"Resume file not found: {resume_path}")
    
    return msg

# -----------------------------
# Step 3: Send Email
# -----------------------------
def send_email(sender_email, password, msg):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
        logging.info(f"Email successfully sent to {msg['To']}")
        print(f"Email successfully sent to {msg['To']}!")
    except Exception as e:
        logging.error(f"Failed to send email to {msg['To']}: {e}")
        print(f"Failed to send email to {msg['To']}. Check logs.")

# -----------------------------
# Step 4: Main function
# -----------------------------
def main():
    hr_emails = get_hr_emails()
    
    subject = "Application for Data Analyst Role"
    body = """
Dear HR,

I hope this email finds you well. I am writing to express my interest in the Data Analyst position.
    """
    
    resume_path = 'path'  # Ensure resume is in the same folder
    
    for hr_email in hr_emails:
        msg = create_email(EMAIL_ADDRESS, hr_email, subject, body, resume_path)
        send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, msg)
    
    print("All emails processed. Check 'email_log.txt' for details.")

if __name__ == "__main__":
    main()
