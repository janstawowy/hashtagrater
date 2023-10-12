from datetime import datetime
import pandas as pd
from mastodonpostman import MastodonPostman
from messagecleaner import MessageCleaner
from jsonreader import JsonReader
from analyser import SentimentAnalyser
from displayer import Displayer
from pyexcel_ods import save_data

pd.set_option('display.expand_frame_repr', False)
ods_file_path = 'data/output.ods'

#read config file
config_file_path = "./config.json"
config = JsonReader(config_file_path).readjson()
print(config)
#read client keys from json file
secrets_file_path = "Keys/secrets.json"
secrets_data = JsonReader(secrets_file_path).readjson()



# Access the client secret
client_id = secrets_data["client_id"]
client_secret = secrets_data["client_secret"]
access_token = secrets_data["access_token"]
api_base_url = secrets_data["api_base_url"]


postman = MastodonPostman(client_id,client_secret,access_token,api_base_url)
messages = postman.returnmessages(config["hashtag"])
message_cleaner = MessageCleaner()
messages_cleaned = message_cleaner.returnmessages(messages)
analyser = SentimentAnalyser(messages_cleaned,config)
sentiment = analyser.analyze_sentiment_textblob("text")
sentiment = analyser.analyze_sentiment_vader("text")
sentiment = analyser.analyze_sentiment_model("text")
final_verdict = analyser.final_verdict()

#save data
# Convert the DataFrame to a dictionary
today_date = datetime.today().date().strftime('%d/%m/%Y')
df_dict = {today_date: sentiment.to_dict(orient='split')['data']}

# Save the data to the ODS file
save_data(ods_file_path, df_dict)

displayer = Displayer(sentiment)
displayer.display_sentiment()




