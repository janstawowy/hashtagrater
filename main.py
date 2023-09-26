
import pandas as pd
from mastodonpostman import MastodonPostman
from messagecleaner import MessageCleaner
from jsonreader import JsonReader
from analyser import SentimentAnalyser

pd.set_option('display.expand_frame_repr', False)

#read client keys from json file
secrets_file_path = "Keys/secrets.json"
secretsjson = JsonReader(secrets_file_path)
secrets_data = secretsjson.readjson()

# Access the client secret
client_id = secrets_data["client_id"]
client_secret = secrets_data["client_secret"]
access_token = secrets_data["access_token"]
api_base_url = secrets_data["api_base_url"]


postman = MastodonPostman(client_id,client_secret,access_token,api_base_url)
messages = postman.returnmessages("DonaldTrump")
message_cleaner = MessageCleaner()
messages_cleaned = message_cleaner.returnmessages(messages)
analyser = SentimentAnalyser(messages_cleaned)
sentiment = analyser.analyze_sentiment("text")
print(sentiment)




