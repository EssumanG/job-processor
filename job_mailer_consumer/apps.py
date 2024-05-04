from django.apps import AppConfig
from .main import callback
from .utils.consumer import cloudamqp

class JobMailerConsumerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'job_mailer_consumer'


    def ready(self):
        print("\n main function invoked ")
        cloudamqp.consume_message(callback=callback)
    
    
