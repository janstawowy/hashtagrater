import json
import pandas as pd
from messageparser import MessageParser
#read client keys from json file
secrets_file_path = "Keys/secrets.json"

try:
    # Read and parse the JSON file
    with open(secrets_file_path, "r") as secrets_file:
        secrets_data = json.load(secrets_file)

    # Access the client secret
    client_id = secrets_data["client_id"]
    client_secret = secrets_data["client_secret"]
    access_token = secrets_data["access_token"]
    api_base_url = secrets_data["api_base_url"]

except FileNotFoundError:
    print(f"File not found: {secrets_file_path}")
except KeyError:
    print("The 'client_secret' key is missing in the JSON file.")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {str(e)}")

parser = MessageParser(client_id,client_secret,access_token,api_base_url)
messages = parser.returnmessages("DonaldTrump")
print(messages)



