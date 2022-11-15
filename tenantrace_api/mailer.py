import smtplib
from django.conf import settings
from email.message import EmailMessage
from forms.models import ApplicationFormResponse


def _send_email(recipient, body):
    msg = EmailMessage()
    msg.set_content(body)

    msg['Subject'] = "Subject: New application response"
    msg['From'] = settings.EMAIL_SENDER_ADDRESS
    msg['To'] = recipient

    try:
        server = smtplib.SMTP(settings.MAILER_SERVER_HOST, settings.MAILER_SERVER_PORT)
        server.ehlo()
        server.starttls()
        server.login(settings.MAILER_SMTP_USERNAME, settings.MAILER_SMTP_PASSWORD)
        server.send_message(msg)
        server.close()
    except:
        raise "Email failed to send"


def _parse_to_email_body(response_value: list):
    body = ""
    for section in response_value:
        title = section.get('title')
        questions = section.get('questions')

        if body != "":
            body = f"""{body}"""
        section_details = ""
        for q in questions:
            if section_details == "":
                section_details = f"""{q['label']}: {q['value']}"""
            else:
                section_details = f"""
                {section_details}
                {q['label']}: {q['value']}
                """
        body = f""" 
        {body}
        {title}
        {"=" * len(title)}
        {section_details}
        """

    body = """    
    A new application response has been submitted.
    {body_}
    """.format(
        body_=body,
    )

    return body


def send_application_response_email(recipient, response: ApplicationFormResponse):
    body = _parse_to_email_body(response.value)
    _send_email(recipient, body)
