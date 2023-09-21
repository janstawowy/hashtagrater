import pandas as pd
import spacy

class SentimentAnalyser:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.nlp = spacy.load("en_core_web_sm")

    def analyze_sentiment(self,column):
        sentiment_results = []

        for text in self.dataframe[column]:
            doc = self.nlp(text)

