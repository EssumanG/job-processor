import os
from typing import Callable
import pika

from dotenv import load_dotenv

load_dotenv()

class CloudAMQPConsumer:
    """ The interface between this project and CloudAMQP """
    QUEUE_NAME = "job_notifier_queue"

    def __init__(self) -> None:
        """ Sets up a connection and a channel when this class is instantiated """
        url = os.environ["CLOUDAMQP_URL"]
        params = pika.URLParameters(url)

        self.__connection = pika.BlockingConnection(params) # Connect to the cloud
    def __create_channel(self) -> pika.BlockingConnection:
        channel = self.__connection.channel() #create a channel
        return channel
    
    def __create_queue(self) -> None:
        """ Declares a queue """
        channel = self.__create_channel()

        channel.queue_declare(queue=self.QUEUE_NAME)

    def consume_message(self, callback: Callable) -> None:
        """ Reads a message publiched to a queue it's bound to """
        self.__create_queue()
        channel = self.__create_channel()

        channel.basic_consume(
            self.QUEUE_NAME,
            callback,
            auto_ack=True
        )

        channel.start_consuming()
        # self.__connection.close()/


cloudamqp: CloudAMQPConsumer = CloudAMQPConsumer()