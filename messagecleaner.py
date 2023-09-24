from bs4 import BeautifulSoup
import pandas as pd
class MessageCleaner:
     def __init__(self):
         self.posts = []
         self.posts_dataframe = pd.DataFrame()


     def returnmessages(self,posts):
        self.posts = posts
        data = []
        for post in self.posts:
            soup = BeautifulSoup(post, 'html.parser')
            for a_tag in soup.find_all('a'):
                a_tag.decompose()
            text_content = soup.get_text()
            text_without_spaces = " ".join(text_content.split())
            data.append({"raw_text":post,"text":text_without_spaces})

        self.posts_dataframe = pd.DataFrame(data)
        return self.posts_dataframe







