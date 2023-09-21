from mastodon import Mastodon

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
        hashtag = hashtag

        # Fetch posts with the hashtag
        hashtag_posts = mastodon.timeline_hashtag(hashtag)
        for post in hashtag_posts:
            print(post["content"])








