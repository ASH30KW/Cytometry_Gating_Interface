import requests

APIBaseURL = "http://cp-traefik/core"

class APIService():
    def __init__(self, token):
        self.token = token
        self.authHeader = headers = {'Authorization': token}

    def getSelf(self):
        return requests.get(APIBaseURL+"/user/self", headers=self.authHeader).json()