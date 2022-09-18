import pandas as pd
import numpy as np

s = pd.Series([1,2,3])
print (s)

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)

# Es kann auch ein eigener Index vergeben werden

data = np.array(['a','b','c','d'])
index = [100,101,102,103]
s = pd.Series(data,index=index)
print (s)


data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s)

print(s[1])   #1.
print(s[1:3])   #1. 2.
print(s['c']) #2.

print(s[['a', 'c']]) # 0. 2.