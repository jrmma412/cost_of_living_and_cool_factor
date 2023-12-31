# import requests

# # Set up API endpoint and parameters
# api_endpoint = "http://api.example.com/data"
# params = {
#     'api_key': 'YourAPIKey',
#     'query': '2 bed 2 bath',  # Your specific query
#     # ... other parameters
# }

# # Make the request
# response = requests.get(api_endpoint, params=params)

# # Check the response status and process the data
# if response.status_code == 200:
#     data = response.json()
#     # Process and analyze your data
# else:
#     print("Failed to retrieve data:", response.status_code)

import pandas as pd
data = pd.read_csv('./realtor-data.zip.csv')
print(data.head())