from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from dotenv import load_dotenv
from django.utils.html import strip_tags
import os

from django.template import loader


load_dotenv()



class EmailHelper:
    username = os.environ["EMAIL_HOST_USER"]
    password = os.environ["EMAIL_HOST_PASSWORD"]
    use_tls = os.environ["EMAIL_USE_TLS"]
    port = os.environ["EMAIL_PORT"]
    host = os.environ["EMAIL_HOST"]

    def send_email(self, to, message):
        """ Send an email to the provided email address"""
        print("kjo")
        cleaned_job_url = message[0]['linkedin_job_url_cleaned'],
        company_name = message[0]['company_name'],
        company_url = message[0]['linkedin_company_url_cleaned'],
        job_title = message[0]['job_title'],
        job_location = message[0]['job_location'],
        print(f"Sending Mail \nJob URL: {cleaned_job_url}\nCompany Name: {company_name}\nCompany URL: {company_url}\nJob Location: {job_location}" )
        html_message = loader.render_to_string("job_list.html", {
            "cleaned_job_url": cleaned_job_url,
            "company_name": company_name,
            "company_url": company_url,
            "job_location": job_location,
            "job_title": job_title,
            'job_list':message
        })
        try:
            message = send_mail(
                subject="Jobs Available",
                message="Hello there",
                from_email= self.username,
                recipient_list = [to,],
                html_message=html_message,
                fail_silently=False
            )

            print("kojo")
        except Exception as e:
            print("Error: {0}".format(e))


emailhelper : EmailHelper = EmailHelper()