import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text       

    def load_json(self):
        data = self.get_response_body()
        result = json.loads(data)
        return result 
