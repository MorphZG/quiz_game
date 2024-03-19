"""
Pulls the questions from opentdb.com
Go to https://opentdb.com/api_config.php to customize the questions.
After generating the API URL, copy the parameters from the URL to the
parameters dictionary down below.
Note: question type can only be boolean.
"""
import requests

parameters = {
    'amount': 10,
    'type': 'boolean',
}

response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
data = response.json()

# question_data is now filled with 10 new questions on every runtime
question_data = data['results']

