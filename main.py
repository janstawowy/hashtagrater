import pandas as pd
from dataprocessor import DataProcessor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import joblib
import h5py
import os
path_to_data = "./data/Twitter_Data.csv"
hdf5_filename = './model/your_model_filename.h5'
df = pd.read_csv(path_to_data)

#print(df.head())
#print(df.shape)
#print(df.info())
#print(df.describe())
processor = DataProcessor(df)
data_processed = processor.process_data("clean_text")


