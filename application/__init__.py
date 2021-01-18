from flask import Flask, request, Response, json
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#load data
df = pd.read_csv("./bankData/bank.csv", header = None)

#drop campaign related columns
df.drop(df.iloc[:, 8:16], inplace = True, axis = 1)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

#extract numeric features 
numeric_data = df.iloc[:, [0, 5]].values
numeric_df = pd.DataFrame(numeric_data, dtype = object)
numeric_df.columns = ['age', 'balance']

#standard scaling age
age_std_scale = StandardScaler()
numeric_df['age'] = age_std_scale.fit_transform(numeric_df[['age']])
#standard scaling balance
balance_std_scale = StandardScaler()
numeric_df['balance'] = balance_std_scale.fit_transform(numeric_df[['balance']])

#extract categoric features
X_categoric = df.iloc[:, [1,2,3,4,6,7]].values

#onehotencoding
ohe = OneHotEncoder()
categoric_data = ohe.fit_transform(X_categoric).toarray()
categoric_df = pd.DataFrame(categoric_data)
categoric_df.columns = ohe.get_feature_names()

#combine numeric and categorix
X_final = pd.concat([numeric_df, categoric_df], axis = 1)

#train model
rfc = RandomForestClassifier(n_estimators = 100)
rfc.fit(X_final, y)

#create flask instance
app = Flask(__name__)

#create api
@app.route('/api', methods=['GET', 'POST'])
def predict():
    #get data from request
    data = request.get_json(force=True)
    data_categoric = np.array([data["job"], data["marital"], data["education"], data["default"], data["housing"], data["loan"]])
    data_categoric = np.reshape(data_categoric, (1, -1))
    data_categoric = ohe.transform(data_categoric).toarray()
 
    data_age = np.array([data["age"]])
    data_age = np.reshape(data_age, (1, -1))
    data_age = np.array(age_std_scale.transform(data_age))

    data_balance = np.array([data["balance"]])
    data_balance= np.reshape(data_balance, (1, -1))
    data_balance = np.array(balance_std_scale.transform(data_balance))

    data_final = np.column_stack((data_age, data_balance, data_categoric))
    data_final = pd.DataFrame(data_final, dtype=object)

    #make predicon using model
    prediction = rfc.predict(data_final)
    return Response(json.dumps(prediction[0]))

