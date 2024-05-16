#   python3 pandas_Read_CSV.py
"""
python3 pandas_Analyzing_DataFrames.py
"""

import pandas as pd

print("Panda Series")
print("************************************")


print("---------------------------------------------------")


df = pd.read_csv('data2.csv')

print(df.head(10)) 

print("---------------------------------------------------")

df = pd.read_csv('data2.csv')

print(df.head())  

print(df.tail())  

print(df.info())  



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

