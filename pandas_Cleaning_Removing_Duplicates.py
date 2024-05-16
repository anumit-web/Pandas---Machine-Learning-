#   python3 pandas_Read_CSV.py
"""
python3 pandas_Cleaning_Removing_Duplicates.py
"""

import pandas as pd

print("Panda Series")
print("************************************")

df = pd.read_csv('data4.csv')

print(df.duplicated())



print("---------------------------------------------------")

df = pd.read_csv('data4.csv')

df.drop_duplicates(inplace = True)

print(df.duplicated())


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

