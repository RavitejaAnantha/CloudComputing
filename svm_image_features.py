
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('image_features.csv', header=0, sep=' ')
df=df.dropna()
trainX = df.drop(['genre','image_name','movie_name'], axis=1)
trainX_col_headers = trainX.columns.values.tolist()
data = pd.DataFrame()
for cols in trainX_col_headers:

    df1=pd.get_dummies(trainX[cols])
    df1_col_headers = df1.columns.values.tolist()
    for i in range(len(df1_col_headers)):
        data[df1_col_headers[i]]=df1.iloc[:,i]
trainY = df.iloc[:, -1:].values
clf=linear_model.SGDClassifier()

clf.fit(data, trainY)

df_test=pd.read_csv('test.csv', header=0, sep=' ')
testX = df.drop(['genre','image_name','movie_name'], axis=1)
testX_col_headers = testX.columns.values.tolist()
testdata = pd.DataFrame()
for cols in testX_col_headers:
    df1=pd.get_dummies(testX[cols])
    df1_col_headers = df1.columns.values.tolist()
    for i in range(len(df1_col_headers)):
        testdata[df1_col_headers[i]]=df1.iloc[:,i]
for index, row in testdata.iterrows():
    print(clf.predict(row))
    print(row)