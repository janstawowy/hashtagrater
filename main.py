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
#print(df.columns)
#print(df.shape)
#print(df.info())
#print(df.describe())
processor = DataProcessor(df)
data_processed = processor.process_data("clean_text")
print(data_processed.info())
print(data_processed.head())
print(data_processed.describe())
# Define X and y
y = data_processed.category
X = data_processed.drop('category', axis=1)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=456)

# Train a logistic regression
"""
log_reg = LogisticRegression().fit(X_train, y_train)
# Predict the labels
y_predicted = log_reg.predict(X_test)

# Print accuracy score and confusion matrix on test set
print('Accuracy on the test set: ', accuracy_score(y_predicted, y_test))
print(confusion_matrix(y_test, y_predicted)/len(y_test))

# Save the model to disk using joblib
joblib.dump(log_reg, 'temp_model.pkl')

# Create an HDF5 file
with h5py.File(hdf5_filename, 'w') as hf:
    # Store the model in the HDF5 file
    hf.create_dataset('model', data=open('temp_model.pkl', 'rb').read())

# Remove the temporary joblib model file
os.remove('temp_model.pkl')"""

