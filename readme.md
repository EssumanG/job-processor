# Job Processor

## Overview

The Job Processor is a microservice responsible for consuming requests from the job request queue, searching for available jobs using an external API, and emailing the response to the user. This service acts as the processing engine for job requests, ensuring that users receive relevant job listings based on their requests.

## Features

- Consumes requests from the job request queue
- Searches for available jobs using an external API
- Emails job listings to users


## Technical Details

- **Programming**: Language:Python
- **Framework**: Django
- **Queueing System**: RabbitMQ
- **External API**: 

## Setup and Installation

1. Clone the repository: git clone (https://github.com/EssumanG/job-processor.git)
2. Install dependencies: pip install -r requirements.txt 
3. Configure environment variables (e.g., queue connection settings, API keys)
4. Start the service: 
    ```bash
    python manage.py runserver
