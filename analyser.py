
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
class SentimentAnalyser:
    def __init__(self, dataframe):
        self.dataframe = dataframe


    def analyze_sentiment_textblob(self, text_column):
        sentiment_results = []

        for text in self.dataframe[text_column]:
            post_blob= TextBlob(text)

            # Print out the sentiment
            if post_blob.sentiment.polarity >= 0.05:
                sentiment_results.append(1)

            elif post_blob.sentiment.polarity <= - 0.05:
                sentiment_results.append(-1)

            else:
                sentiment_results.append(0)
            #sentiment_results.append(post_blob.sentiment.polarity)

        self.dataframe['Sentiment_textblob'] = sentiment_results

        return self.dataframe

    def analyze_sentiment_vader(self,text_column):
        vader = SentimentIntensityAnalyzer()
        sentiment_results= []
        for text in self.dataframe[text_column]:
            sentiment_dict = vader.polarity_scores(text)
            if sentiment_dict['compound'] >= 0.05:
                sentiment_results.append(1)

            elif sentiment_dict['compound'] <= - 0.05:
                sentiment_results.append(-1)

            else:
                sentiment_results.append(0)

        self.dataframe['Sentiment_vader'] = sentiment_results
        return self.dataframe




