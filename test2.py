import requests

# Define the API endpoint
url = "https://passwordinator.onrender.com?num=true&char=true&caps=true&len=18"

# Make a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (the generated password)
    print("Generated Password:", response.text)
else:
    # Print an error message if the request was unsuccessful
    print("Failed to fetch password. Status code:", response.status_code)
