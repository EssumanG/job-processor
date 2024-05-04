import os, json
from typing import List, Dict
from dotenv import load_dotenv
import requests


load_dotenv()

class APIRequestHelper:
    """
    A helper class for calling the external APIs
    """
    API_KEY = os.environ["RAPID_API_KEY"]

    def __make_request(
            self, url: str, headers: dict =None, params: dict = None, payload: dict = None
    ):
        if headers is None:
            headers = {
                "x-rapidapi-key": self.API_KEY,
                "content-type": "application/json"
            }
            print(payload)
            try:
                response = requests.request("POST", url, data=payload, headers=headers)

                print(f"\n request respponse #{response.text}")
                print(f"\n request respponse code #{response.status_code}")
            except Exception as e:
                error = f"error: {e}"
                response = {"error": error}
                print(response)
            
            response = json.loads(response.content)

        return response

    def __get_linkedin_jobs(self, payload: dict) -> List[Dict]:
        __api_url = "https://linkedin-jobs-search.p.rapidapi.com/"
        linkedin_jobs = self.__make_request(url=__api_url, payload=payload)

        return linkedin_jobs
    
    def get_jobs(self, payload: dict) -> List[Dict]:
        payload = json.dumps(payload)
        jobs = self.__get_linkedin_jobs(payload=payload)
        print("received")
        return jobs
    
jobs_api: APIRequestHelper = APIRequestHelper()