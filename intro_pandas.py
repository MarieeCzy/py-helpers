from unicodedata import name
import pandas as pd

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

print(results.describe())

