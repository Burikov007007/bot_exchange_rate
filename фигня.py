import requests

url = "https://api.apilayer.com/fixer/latest?symbols=EUR%2CUSD%2CGBP%2CKZT%2CCNY&base=RUB"

payload = {}
headers= {
  "apikey": "ZahN6x7a0G10OyCWUbLHHcj8XajdFV8K"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(response.text)

