import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS



def lemmatize_text(text):
    doc = nlp(text)
    lemmatized_text = " ".join([token.lemma_ for token in doc])
    return lemmatized_text
class DataProcessor:

    def __init__(self,dataframe):
        self.df = dataframe
        self.df_processed = pd.DataFrame()
        self.df_vectorized = pd.DataFrame()


    def preprocess_data(self):
        print(self.df.isnull().sum())
        self.df_processed = self.df.dropna(axis=0)
        self.df_processed = self.df_processed.reset_index(drop=True)


    def vectorize_data(self,column_name):
        #print(self.df[column_name])
        print("vectorizing text...")

        vect = TfidfVectorizer(stop_words=ENGLISH_STOP_WORDS, ngram_range=(1, 3), max_features=3000,token_pattern=r'\b[^\d\W][^\d\W]+\b', max_df=0.7)
        vect.fit(self.df_processed[column_name])
        X = vect.transform(self.df_processed[column_name])
        reviews_transformed = pd.DataFrame(X.toarray(), columns=vect.get_feature_names())
        reviews_transformed["category"] = self.df_processed.category
        # print('Top 5 rows of the DataFrame: \n', reviews_transformed.head())
        self.df_vectorized = reviews_transformed
        return self.df_vectorized


