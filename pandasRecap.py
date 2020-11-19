import numpy as np
import pandas as pd

print("Pandas recap")
print("==================================")
x = ['a','b','c','d','e']
y = [1,2,3,4,5]
z = {1:'a',2:'b',3:'c',4:'d',5:'e'}
print(x)
print(y)
print(z)
print('- - - - - - - - - - - - - - - - -')
print('Series: ')
a = pd.Series(data = x)
print(a)
print('- - - - - - - - - - - - - - - - -')
print(type(a))
print('- - - - - - - - - - - - - - - - -')
a = pd.Series(data = x, index = y)
print(a)
print('- - - - - - - - - - - - - - - - -')
b = pd.Series(z)
print(b)
print("----------------------------------")
print()