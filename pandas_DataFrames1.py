#   python3 pandas_test1.py
"""
python3 pandas_test1.py
"""

import pandas as pd

print("Panda Series")
print("************************************")

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 

print("---------------------------------------------------")

#refer to the row index:
print(df.loc[0]) 


print("---------------------------------------------------")

#use a list of indexes:
print(df.loc[[0, 1]])

print("---------------------------------------------------")

#Named Indexes
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
index = ["day1", "day2", "day3"]

df = pd.DataFrame(data, index)

print(df) 

print("---------------------------------------------------")

#refer to the named index:
print(df.loc["day2"])

print("---------------------------------------------------")

#Load Files Into a DataFrame
df = pd.read_csv('data1.csv')

print(df)

"""
x = ["apple", "banana", "cherry"] 	list 	
x = ("apple", "banana", "cherry") 	tuple
x = {"name" : "John", "age" : 36} 	dict 	
x = {"apple", "banana", "cherry"} 	set
"""

"""
x = list(("apple", "banana", "cherry")) 	list 	
x = tuple(("apple", "banana", "cherry")) 	tuple
x = dict(name="John", age=36) 	dict 	
x = set(("apple", "banana", "cherry")) 	set
"""

