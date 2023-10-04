import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS

class DataProcessor:

    def __init__(self,dataframe):
        self.df = dataframe
        self.df_transformed = pd.DataFrame()


    def process_data(self,column_name):
        #print(self.df[column_name])
        self.df = self.df.dropna(axis=0)
        self.df = self.df.reset_index(drop=True)
        vect = TfidfVectorizer(stop_words=ENGLISH_STOP_WORDS, ngram_range=(1, 2), max_features=200,token_pattern=r'\b[^\d\W][^\d\W]+\b').fit(self.df[column_name])

        X = vect.transform(self.df[column_name])
        reviews_transformed = pd.DataFrame(X.toarray(), columns=vect.get_feature_names())
        reviews_transformed["category"] = self.df.category
        # print('Top 5 rows of the DataFrame: \n', reviews_transformed.head())
        self.df_transformed = reviews_transformed
        return self.df_transformed

