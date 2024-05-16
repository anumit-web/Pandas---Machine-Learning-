#   python3 pandas_test1.py
"""

python3 pandas_test4.py

"""

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


a2 = [3, 9, 2]
index2 = ["x", "y", "z"]

myvar2 = pd.Series(a2, index2)

print(myvar2)
print(myvar2["y"]) 
