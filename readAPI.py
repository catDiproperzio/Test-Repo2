import requests
import json 

response = requests.get('http://api.stackexchange.com/2.3/answers?order=desc&sort=activity&site=stackoverflow')

print(response.json())