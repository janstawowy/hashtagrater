
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import joblib

from sklearn.linear_model import LogisticRegression

class SentimentAnalyser:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.model_file_path = 'model/post_rater.pkl'
        self.vectorizer_file_path = 'model/tfidf_vectorizer.pkl'
        self.model ={}
        self.vectorizer = {}

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

        self.dataframe['sentiment_textblob'] = sentiment_results

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

        self.dataframe['sentiment_vader'] = sentiment_results
        return self.dataframe

    def analyze_sentiment_model(self, text_column):

        loaded_model = {}
        try:

            with open(self.model_file_path, 'rb') as file:
                self.model  = joblib.load(file)
                print("model loaded")

        except FileNotFoundError:
            print(f"File not found: {self.model_file_path}")
            return self.dataframe
        try:

            with open(self.vectorizer_file_path, 'rb') as file:
                self.vectorizer  = joblib.load(file)
                print("vectorizer loaded")

        except FileNotFoundError:
            print(f"File not found: {self.vectorizer_file_path}")
            return self.dataframe

        text_vectorized = self.vectorizer.transform(self.dataframe[text_column])
        sentiment = self.model.predict(text_vectorized)
        self.dataframe["sentiment_model"] = sentiment

        return self.dataframe


