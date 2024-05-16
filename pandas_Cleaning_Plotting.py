#   python3 pandas_Read_CSV.py
"""
python3 pandas_Cleaning_Plotting.py
"""

import pandas as pd

import matplotlib.pyplot as plt


print("************************************")

df = pd.read_csv('data6.csv')

df.plot()

plt.show()


print("---------------------------------------------------")

df = pd.read_csv('data6.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()


print("---------------------------------------------------")

df = pd.read_csv('data6.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show() 

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

