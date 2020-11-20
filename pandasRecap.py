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
print('DataFrames, frames of Series: ')
print("----------------------------------")
A = [1,2,3,4]
B = [5,6,7,8]
C = [9,0,1,2]
D = [3,4,5,6]
E = [7,8,9,0]
print('df = pd.DataFrame(data, index or rows, columns)')
df = pd.DataFrame([A,B,C,D,E], ['a','b','c','d','e'], ['W','X','Y','Z'])
print()
print(df)
print()
print('cmd + ctrl + spacebar')
print('😃')
print()
print("----------------------------------")
