import requests
import os

# Get credentials from GitHub secrets
SN_CLIENT_ID = os.getenv("SN_CLIENT_ID")
SN_CLIENT_SECRET = os.getenv("SN_CLIENT_SECRET")
SN_INSTANCE = os.getenv("SN_INSTANCE")

# The simple API call we will use. You can use any public API endpoint.
api_url = f"{SN_INSTANCE}/api/now/v2/stats"

# Headers for the request. We don't need a token yet for this simple call.
headers = {
  "Content-Type": "application/json"
    }

  print(f"Pinging ServiceNow instance at: {api_url}")

try:
  response = requests.get(api_url, headers=headers)
  response.raise_for_status()  # This will raise an HTTPError for bad responses
        
  print("Successfully pinged the instance. Response status code:", response.status_code)
  print("Instance is active!")

except requests.exceptions.RequestException as e:
  print(f"An error occurred: {e}")
  print("Could not reach the ServiceNow instance. Is it offline?")
