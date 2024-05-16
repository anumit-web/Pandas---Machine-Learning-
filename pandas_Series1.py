#   python3 pandas_test1.py
"""
python3 pandas_test1.py
"""

import pandas as pd

print("Panda Series")
print("************************************")


a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0]) 

a2 = [1, 7, 2]
index2 = ["x", "y", "z"]

myvar2 = pd.Series(a2, index2)

print(myvar2)
print(myvar2["y"])

print("---------------------------------------------------")

calories3 = {"day1": 420, "day2": 380, "day3": 390}

myvar3 = pd.Series(calories3)

print(myvar3)

print("---------------------------------------------------")


calories4 = {"day1": 420, "day2": 380, "day3": 390}

myvar4 = pd.Series(calories4, index = ["day1", "day2"])

print(myvar4)

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

