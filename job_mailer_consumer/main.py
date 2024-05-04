from .utils.api_helper import jobs_api
import json
from .utils.email_helper import emailhelper

def callback(ch, method, properties, body):
    """ The logic for grabbing jobs and sending an email will be invoked here"""
    body = json.loads(body.decode("utf-8"))
    search_term = body.get("search_term")
    location = body.get("location")
    email = body.get("email")


    payload = {
        "search_terms": search_term,
        "location": location
    }

    print(payload)

    jobs = jobs_api.get_jobs(payload=payload)
    print("hjhjj", jobs)

    emailhelper.send_email(email, jobs)
    