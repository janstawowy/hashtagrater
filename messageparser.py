from mastodon import Mastodon
from bs4 import BeautifulSoup
import pandas as pd
class MessageParser:
     def __init__(self,client_id,client_secret,access_token,api_base_url):
         self.client_id = client_id
         self.client_secret = client_secret
         self.access_token = access_token
         self.api_base_url = api_base_url

     def returnmessages(self,hashtag):
        mastodon = Mastodon(
            client_id=self.client_id,
            client_secret=self.client_secret,
            access_token=self.access_token,
            api_base_url=self.api_base_url
        )
        # Fetch posts with the hashtag
        hashtag_posts = mastodon.timeline_hashtag(hashtag)
        data = []
        for post in hashtag_posts:
            soup = BeautifulSoup(post['content'], 'html.parser')
            for a_tag in soup.find_all('a'):
                a_tag.decompose()
            text_content = soup.get_text()
            text_without_spaces = " ".join(text_content.split())
            data.append({"raw_text":post['content'],"text":text_without_spaces})

        df = pd.DataFrame(data)
        return df







