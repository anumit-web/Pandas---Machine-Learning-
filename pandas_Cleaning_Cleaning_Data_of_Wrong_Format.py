#   python3 pandas_Read_CSV.py
"""
python3 pandas_Cleaning_Empty_Cells.py
"""

import pandas as pd

print("Panda Series")
print("************************************")


print("---------------------------------------------------")

df = pd.read_csv('data3.csv')

new_df = df.dropna()

print(new_df.to_string())

print("---------------------------------------------------")

df = pd.read_csv('data3.csv')

df.dropna(inplace = True)

print(df.to_string()) 

print("---------------------------------------------------")

df = pd.read_csv('data3.csv')

df.fillna(130, inplace = True) 

print(df.to_string()) 

print("---------------------------------------------------")

df = pd.read_csv('data3.csv')

df["Calories"].fillna(130, inplace = True) 

print(df.to_string()) 

print("---------------------------------------------------")

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

