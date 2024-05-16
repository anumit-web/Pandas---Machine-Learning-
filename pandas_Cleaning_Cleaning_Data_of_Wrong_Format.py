#   python3 pandas_Read_CSV.py
"""
python3 pandas_Cleaning_Cleaning_Data_of_Wrong_Format.py
"""

import pandas as pd

print("Panda Series")
print("************************************")

df = pd.read_csv('data4.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

print("---------------------------------------------------")



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

