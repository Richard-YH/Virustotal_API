import requests
from config import API_KEY

ip = "IP"

# Get IP address report
url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
}

response = requests.get(url, headers=headers)

print(response.text)
