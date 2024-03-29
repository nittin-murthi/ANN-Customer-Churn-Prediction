# -*- coding: utf-8 -*-
"""PreProcessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bT049aoae7boPnscD1ioo6zsm-zbZenL
"""

#import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
#Enable inline plotting for graphics to appear
# %matplotlib inline

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

#Load dataset and then print first 5 rows
data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
data.head()

#Remove customerID column due for improved performance
data.drop('customerID', axis='columns', inplace=True)
data.head()

#Print data type of each column in dataset
data.dtypes

#Convert values in TotalCharges column to boolean indicating presence of value
pd.to_numeric(data.TotalCharges, errors='coerce').isnull()

print(data[pd.to_numeric(data.TotalCharges,errors='coerce').isnull()].shape)
data[pd.to_numeric(data.TotalCharges,errors='coerce').isnull()]

data.iloc[488]

data.iloc[488]['TotalCharges']

updated_data = data[data.TotalCharges != ' ']

data.shape

updated_data.shape

updated_data.TotalCharges = pd.to_numeric(updated_data.TotalCharges)

updated_data.TotalCharges.dtypes

tenure_no_churn = updated_data[updated_data.Churn=='No'].tenure
tenure_yes_churn = updated_data[updated_data.Churn=='Yes'].tenure

plt.hist([tenure_yes_churn, tenure_no_churn], color=['green', 'red'],label=['Churn = Yes', 'Churn = No'])
plt.xlabel("Tenure")
plt.ylabel("Number of Customers")
plt.title("Customer Churn vs Tenure")
plt.legend()

for column in data:
  print(column)

for column in data:
  if updated_data[column].dtypes == 'object':
    print(f'{column} : {updated_data[column].unique()}')

updated_data.replace('No internet service', 'No', inplace = True)
updated_data.replace('No phone service', 'No', inplace = True)

for column in data:
  if updated_data[column].dtypes == 'object':
    print(f'{column} : {updated_data[column].unique()}')

updated_data['gender'].replace({'Female': 1, 'Male': 0}, inplace = True)

boolean_columns = ['Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'Churn']

for column in boolean_columns:
  updated_data[column].replace({'Yes': 1, 'No': 0}, inplace = True)

for column in data:
  print(f'{column} : {updated_data[column].unique()}')

new_data = pd.get_dummies(data = updated_data, columns = ['InternetService', 'Contract', 'PaymentMethod'])
new_data.head()

normalization_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']

new_data[normalization_columns] = scaler.fit_transform(new_data[normalization_columns])

new_data.head()