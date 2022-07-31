from cProfile import label
from hashlib import new
from http import client
from unicodedata import name
import pandas as pd
from traitlets import Int

# lists of values
name = ['Carol', 'Sven', 'Nicolas', 'Maria', 'Peter']
age = [27, 25, 30, 22, 40]
score = [123, 200, 142, 150, 160]


# empty dictionary
data = dict()

# add key - values to dictionary data
data['Name'] = name
data['Age'] = age
data['Score'] = score

data_frame = pd.DataFrame(data)

print(data_frame)

# creating data frame from list of lists

# empty list
data = list()

# merge lists 
def new_row(list1, list2, list3):
    i = 0
    while i < len(name):
        row = [list1[i]] + [list2[i]] + [list3[i]]
        data.append(row)
        i += 1
    else:
        return data
        
    
new_row(name, age, score)
print(data)

# DataFrame from list of lists
data_frame = pd.DataFrame(data)

#headers
data_frame = pd.DataFrame(data, columns=['Name', 'Age', 'Score'])
print(data_frame)

#load data from xlsx file
file_path = 'results.xlsx'
results = pd.read_excel(file_path)

#top five rows from data frame
print(results.head())

# describe, selecting columns
print(results.describe())

# selected column
print(results.columns[0])

#all columns
print(results.columns)

# columns by name
print(results['czas'])

# selected row printing
print(results.iloc[120])

selected_range = results.loc[120:135]
selected_range_details = selected_range.describe()
print(selected_range_details)

mask = results.loc[:,'TE28'] > 100

above_hundred = pd.DataFrame(results[mask])
print(above_hundred) 

print(above_hundred['TE28'].unique())

#manipulating DatFrames

data = {'first':['Carl','Francis','Sam'], 
        'last': ['Po', 'Popo', 'Smith'],
        'age': ['22','45','55']}

clients = pd.DataFrame(data)

clients.rename(columns={'last':'Surname'}, inplace=True)
'''clients.rename(index={0:'a', 1:'b', 2: 'c'}, inplace=True)

clients.reset_index(inplace=True)'''
clients.drop(columns='first', inplace=True)
clients.drop(index=0, inplace=True)

clients['new_column'] = (1,2)
print(clients.new_column.astype(float))


new_data = {'first':['Samantha','Oksana'],
            'Surname':['Rankler','Maple'],
            'age':['22', '44']}

new_clients = pd.DataFrame(new_data)
new_clients.loc[1, 'age'] = 100
print(new_clients)

data= [clients, new_clients]
clients = pd.concat(data, ignore_index=True), 

print(clients)








