import requests

# Define the URL of the web page you want to fetch
url = 'https://www.example.com Send an HTTP GET request to the specified URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # The request was successful, so we can access the response data
    html_content = response.text
    print(html_content)
else:
    # The request failed, so we can handle the error
    print('An error occurred while fetching the web page.')
