# from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr


def send_email(data):
    # get form data
    file_name = data.file_name
    f_name = file_name[:-4]
    m_date = data.meeting_date
    meeting_date = str(m_date)
    # smtpserver = smtplib.SMTP("smtp.office365.com",587)
    sender_email = 'grp7be.fcrit@outlook.com'
    sender_password = 'Fcrit@grp7'
    sender_name = 'SumMeet'
    # smtpserver.ehlo()
    # smtpserver.starttls()
    # smtpserver.ehlo
    # smtpserver.login(sender_email, sender_password)
    recipient_emails = data.mailing_list
    subject = 'Minutes of meeting conducted on: '+meeting_date
    body = 'Greetings!\n Please find the MoM attached herewith.'
    file_path = 'summeet_package/generated_pdfs/'+f_name+'_summarized.pdf'

    # save PDF file to disk
    # file_path = 'uploads/' + file.filename
    # file.save(file_path)

    # create message object instance
    message = MIMEMultipart()

    # set email content
    message["From"] = formataddr((sender_name, sender_email))
    message["To"] = ", ".join(recipient_emails)
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # attach PDF file
    with open(file_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), _subtype="pdf")
        part.add_header("Content-Disposition", "attachment", filename=f_name+'_summarized.pdf')
        message.attach(part)

    # create SMTP session
    with smtplib.SMTP("smtp.office365.com", 587) as session:
        session.starttls()
        session.login(sender_email, sender_password)
        text = message.as_string()
        session.sendmail(sender_email, recipient_emails, text)

    return 'Email sent with PDF attachment to ' + ', '.join(recipient_emails)