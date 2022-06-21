import requests

url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=GBP"
payload = {}
headers= {
  "apikey": "ZahN6x7a0G10OyCWUbLHHcj8XajdFV8K"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(response.text)
url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=USD"
payload = {}
headers= {
  "apikey": "ZahN6x7a0G10OyCWUbLHHcj8XajdFV8K"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(response.text)
url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=EUR"
payload = {}
headers= {
  "apikey": "ZahN6x7a0G10OyCWUbLHHcj8XajdFV8K"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(response.text)
url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=CNY"
payload = {}
headers= {
  "apikey": "ZahN6x7a0G10OyCWUbLHHcj8XajdFV8K"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(response.text)
url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=KZT"
payload = {}
headers= {
  "apikey": "ZahN6x7a0G10OyCWUbLHHcj8XajdFV8K"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(response.text)

