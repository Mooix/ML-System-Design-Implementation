import numpy as np
import pandas as pd
import pickle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("data.csv")

data = data.dropna()
data = data.reset_index()
data = data.drop('id', axis = 1)
data = data.drop('Unnamed: 0', axis = 1)
data = data.drop('Age', axis = 1)
data = data.drop('index', axis = 1)
data = data.drop('Gender', axis = 1)
data = data.drop_duplicates()

i = 0
count = 0
while True:
    d = data['satisfaction'][i]
    #print(d + '\t')
    #print(i)
    if d == 'neutral or dissatisfied' and count != 3000:
        data=data.drop(i, axis = 0, inplace = False)
        count+=1
    i+=1
    if count == 3000:
        break




label_encoder = preprocessing.LabelEncoder()
encode=['Customer Type','Type of Travel', 'Class', 'satisfaction']
for i in encode:
    data[i] = label_encoder.fit_transform(data[i])


X =data.iloc[:,:-1]
y =data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rnd = RandomForestClassifier()
rnd.fit(X_train, y_train)

pickle.dump(rnd, open("pik.pkl", "wb"))
#rnd_pred = rnd.predict(X_test)

#from sklearn.metrics import classification_report
#from sklearn.metrics import confusion_matrix
#print('Random forest' + '\n')
#print(classification_report(y_test,rnd_pred))
#print('\n')
#sns.heatmap(confusion_matrix(y_test,rnd_pred),cmap='Greys_r',annot=True,fmt='g')
#plt.title('Confusion matrix', y=1.1)

