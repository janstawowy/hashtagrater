from bs4 import BeautifulSoup
from langdetect import detect_langs
import pandas as pd
class MessageCleaner:
     def __init__(self):
         self.posts = []
         self.posts_dataframe = pd.DataFrame()


     def return_messages(self,posts):
        self.posts = posts
        data = []
        for post in self.posts:

            soup = BeautifulSoup(post, 'html.parser')
            for a_tag in soup.find_all('a'):
                a_tag.decompose()
            text_content = soup.get_text()
            text_without_spaces = " ".join(text_content.split())

            if(len(text_without_spaces)>0):
                languages = detect_langs(text_without_spaces)
                print(languages)
                language = str(languages[0])[0:2]
                if (language != "en"):
                    print(language)
                    continue
                data.append({"raw_text":post,"text":text_without_spaces})

        self.posts_dataframe = pd.DataFrame(data)
        return self.posts_dataframe







