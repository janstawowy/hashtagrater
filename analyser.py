
import pandas as pd
from textblob import TextBlob

class SentimentAnalyser:
    def __init__(self, dataframe):
        self.dataframe = dataframe


    def analyze_sentiment(self, text_column):
        sentiment_results = []

        for text in self.dataframe[text_column]:
            post_blob= TextBlob(text)

            # Print out the sentiment
            sentiment_results.append(post_blob.sentiment.polarity)

        self.dataframe['Sentiment'] = sentiment_results

        return self.dataframe


