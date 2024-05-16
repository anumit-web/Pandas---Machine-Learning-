#   python3 pandas_Read_CSV.py
"""
python3 pandas_Cleaning_Fixing_Wrong_Data.py
"""

import pandas as pd

print("Panda Series")
print("************************************")

df = pd.read_csv('data4.csv')

df.loc[7, 'Duration'] = 45

print(df.to_string())


print("---------------------------------------------------")

df = pd.read_csv('data4.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())


print("---------------------------------------------------")

df = pd.read_csv('data4.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())

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

