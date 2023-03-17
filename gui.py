import requests

# URL of Flask server endpoint
url = "http://127.0.0.1:8000/data"

# Data to send in the POST request
data = {
"from":"ankara",
"goTo": "istanbul",
"way": "one way",
"date": "30.04.2023",
"returnDate": False
}

# Headers for the POST request
headers = {"Content-Type": "application/json"}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
print(response.status_code)
print(response.json())
