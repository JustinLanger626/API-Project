import requests as re

base_url = "https://www.whenisthenextmcufilm.com/api"

response = re.get(base_url)

if response.ok: 
    print(response.text)
     