
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import joblib

from sklearn.linear_model import LogisticRegression

class SentimentAnalyser:
    def __init__(self, dataframe,config):
        self.dataframe = dataframe
        self.model_file_path = config["model_file_path"]
        self.vectorizer_file_path = config["vectorizer_file_path"]
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

    def final_verdict(self):
        final_verdict = self.dataframe[['sentiment_textblob', 'sentiment_vader', 'sentiment_model']].mean(axis=1)
        self.dataframe["verdict_mean"] = final_verdict
        # Define the bin edges and labels
        bin_edges = [-2, -0.6, -0.3, 0.3, 0.6,2]
        bin_labels = ['Very Negative', 'Negative', 'Neutral', 'Positive', "Very Positive"]

        # Use pd.cut() to categorize the values and assign labels
        self.dataframe["final_verdict"] = pd.cut(final_verdict, bins=bin_edges, labels=bin_labels)

        return self.dataframe


