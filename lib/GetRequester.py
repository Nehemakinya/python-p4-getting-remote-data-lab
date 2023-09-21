import requests
import json 

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  
            return response.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")

    def load_json(self):
        try:
            response_body = self.get_response_body()
            data = json.loads(response_body)  
            return data
        except ValueError as e:
            raise Exception(f"Failed to load JSON: {str(e)}")


if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)

    try:
        json_data = requester.load_json()
        print(json_data)  
    except Exception as e:
        print(f"An error occurred: {str(e)}")
