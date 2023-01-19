import requests
import json

# Set the API endpoint and parameters
api_url = 'https://www.helioviewer.org/api/v2/events'
params = {'event_type': 'FL', 'event_starttime': '2022-01-01', 'event_endtime': '2022-02-01'}

# Send a GET request to the API endpoint
response = requests.get(api_url, params=params)

# Parse the JSON data returned by the API
data = json.loads(response.text)

# Access the events in the data
events = data['events']

# Print the details of the events
for event in events:
    print("Event Type:", event['event_type'])
    print("Event Start Time:", event['event_starttime'])
    print("Event End Time:", event['event_endtime'])
