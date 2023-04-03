import requests
import json

# Set the Joomla API endpoint URL
joomla_api_url = 'https://your-joomla-website.com/api/rest/articles'

# Set the authorization credentials
username = 'your-joomla-username'
password = 'your-joomla-password'

# Set the article data
data = {
    'title': 'My new article',
    'alias': 'my-new-article',
    'introtext': 'This is the introduction to my new article.',
    'fulltext': 'This is the full content of my new article.',
    'catid': 1  # The ID of the category where the article will be posted
}

# Set the HTTP headers with the authorization credentials and content type
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + str(base64.b64encode((username + ':' + password).encode("utf-8")), "utf-8")
}

# Send the HTTP POST request to create the article
response = requests.post(joomla_api_url, headers=headers, data=json.dumps(data))

# Check the HTTP response status code
if response.status_code == 201:
    # The article was successfully created
    print('Article created successfully')
else:
    print('Failed to create article')