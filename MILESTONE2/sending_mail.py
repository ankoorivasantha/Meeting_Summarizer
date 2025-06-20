import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def send_email(subject, body, recipients, sender_email, sender_password):
    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Change to your SMTP server
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the email account
            
            # Send the email
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    # Create a Tkinter root window
    Tk().withdraw()  # Hide the root window

    # Ask the user to select the transcription file
    transcription_file_path = askopenfilename(title="Select Transcription File", filetypes=[("Text Files", "*.txt")])
    
    if not transcription_file_path:
        print("No file selected. Exiting...")
        return
    
    # Prompt for sender's email and password
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password (consider using an app password): ")
    
    # Prompt for recipient emails
    recipients_input = input("Enter recipient email addresses separated by commas: ")
    recipients = [email.strip() for email in recipients_input.split(",")]  # Split by comma and strip whitespace
    
    # Read the transcription text
    with open(transcription_file_path, 'r') as file:
        transcription_content = file.read()
    
    # Specify email subject
    subject = "Transcription Report"
    
    # Send the email
    send_email(subject, transcription_content, recipients, sender_email, sender_password)

if __name__ == "__main__":
    main()
