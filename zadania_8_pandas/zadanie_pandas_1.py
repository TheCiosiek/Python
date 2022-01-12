import pandas
import numpy
# from matplotlib import pyplot

data = pandas.read_csv('train.csv')

data_copy = data.drop(columns=["PassengerId", "SibSp", "Parch", "Ticket", "Cabin"])
# data_copy.drop(columns=["Name"], inplace=True)
data_copy.dropna(inplace=True)

titles = []
passenger_names = data_copy['Name'].values
for passenger_name in passenger_names:
    titles.append(passenger_name.split(',')[1].split('.')[0].strip())
data_copy['Title'] = titles


gender_values = data_copy['Sex'].values
gender_values_encoded = []
for gender_value in gender_values:
    if gender_value == 'male':
        gender_values_encoded.append(0)
    else:
        gender_values_encoded.append(1)

gender_values_encoded = [0 if gender_value=='male' else 1 for gender_value in gender_values]

age_values = data_copy['Age'].values
age_encode=[]
for age in age_values:
    if age<20:
        age_encode.append(round(data_copy.loc[data_copy.Age<20].Age.mean(),0))
    elif age in range (20,28):
        age_encode.append(round(data_copy.loc[(data_copy.Age>=20) & (data_copy.Age<28)].Age.mean(),0))
    elif age in range (28,38):
        age_encode.append(round(data_copy.loc[(data_copy.Age>=28) & (data_copy.Age<38)].Age.mean(),0))
    else:
        age_encode.append(round(data_copy.loc[(data_copy.Age>=38)].Age.mean(),0))
data_copy['Age']=age_encode

#data_copy.Fare.describe()
fare_values = data_copy['Fare'].values
fare_encode=[]
for fare in fare_values:
    if fare<8.05:
        fare_encode.append(8)
    elif ((fare>=8.05) and (fare<15.64585)):
        fare_encode.append(12)
    elif ((fare>=15.64585) and (fare<33)):
        fare_encode.append(24)
    else:
        fare_encode.append(33)
data_copy['Fare']=fare_encode
data_copy

#data_copy.Embarked.unique()
embarked_values = data_copy['Embarked'].values
embarked_encode=[]
for embarked in embarked_values:
    if embarked=="S":
        embarked_encode.append(1)
    elif embarked=="C":
        embarked_encode.append(2)
    elif embarked=="Q":
        embarked_encode.append(3)
data_copy['Embarked']=embarked_encode
data_copy

#data_copy.groupby('Title').Title.count().sort_values()
title_values = data_copy['Embarked'].values
title_encode=[]
for title in title_values:
    if title=="Mr":
        title_encode.append(1)
    elif title=="Miss":
        title_encode.append(2)
    elif title=="Mrs":
        title_encode.append(3)
    else:
        title_encode.append(4)
data_copy['Title']=embarked_encode
print(data_copy)