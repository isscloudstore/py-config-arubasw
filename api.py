import requests
import json

# Device API details
DEVICE_IP = "192.168.1.1"  # Change to your device's IP
USERNAME = "admin"
PASSWORD = "password"

# API endpoint (Modify based on your device)
API_URL = f"http://{DEVICE_IP}/rest/v10.04/system"  # Example for ArubaOS

# Headers for JSON data
HEADERS = {
    "Content-Type": "application/json"
}

# Authentication (Basic Auth)
auth = (USERNAME, PASSWORD)

try:
    # Send GET request to fetch system details
    response = requests.get(API_URL, auth=auth, headers=HEADERS, verify=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))  # Print formatted response
    else:
        print(f"Failed to connect. Status Code: {response.status_code}, Message: {response.text}")

    # Example: Change hostname on an Aruba device
    CONFIG_API_URL = f"http://{DEVICE_IP}/rest/v10.04/system"
    new_config = {
    "hostname": "New-Aruba-Switch"
    }

    # Send a PUT request to apply configuration
    response = requests.put(CONFIG_API_URL, auth=auth, headers=HEADERS, json=new_config, verify=False)

    if response.status_code == 200:
        print("Configuration updated successfully!")
    else:
        print(f"Failed to update. Status: {response.status_code}, Message: {response.text}")

except Exception as e:
    print(f"Error: {e}")

# Example: Change hostname on an Aruba device
CONFIG_API_URL = f"http://{DEVICE_IP}/rest/v10.04/system"
new_config = {
    "hostname": "New-Aruba-Switch"
}

# Send a PUT request to apply configuration
response = requests.put(CONFIG_API_URL, auth=auth, headers=HEADERS, json=new_config, verify=False)

if response.status_code == 200:
    print("Configuration updated successfully!")
else:
    print(f"Failed to update. Status: {response.status_code}, Message: {response.text}")
