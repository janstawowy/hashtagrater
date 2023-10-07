import pandas as pd
from dataprocessor import DataProcessor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import joblib
import h5py
import os
path_to_data = "./data/Twitter_Data.csv"
model_filename = './model/post_rater.pkl'
df = pd.read_csv(path_to_data)

#print(df.head())
#print(df.columns)
#print(df.shape)
#print(df.info())
#print(df.describe())
processor = DataProcessor(df)
processor.preprocess_data()
data_processed = processor.vectorize_data("clean_text")
print(data_processed.info())
print(data_processed.head())
print(data_processed.describe())
# Define X and y
y = data_processed.category
X = data_processed.drop('category', axis=1)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=456)

# Train a logistic regression

log_reg = LogisticRegression(max_iter=200,solver='liblinear',penalty = 'l1', C=0.3)
print("training the model...")
log_reg.fit(X_train, y_train)
# Predict the labels
y_predicted = log_reg.predict(X_test)

# Print accuracy score and confusion matrix on test set
print('Accuracy on the test set: ', accuracy_score(y_predicted, y_test))
print(confusion_matrix(y_test, y_predicted)/len(y_test))

# Save the model to disk using joblib
joblib.dump(log_reg, model_filename)



