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
print('- - - - - - - - - - - - - - - - -')
print('Creating and deleting rows and column in dataframe')
print("----------------------------------")
df1 = df
df1['P'] = df1['Y'] + df1['Z']
print(df1)
print('- - - - - - - - - - - - - - - - -')
df2 = df.drop('e')
print(df2)
print('- - - - - - - - - - - - - - - - -')
print("In case you want to mutate df, write: df2 = df.drop('e', inplace= True)")
# df2 = df.drop('e', inplace= True)
print(df)
print('- - - - - - - - - - - - - - - - -')
df3 = df.drop('P', axis = 1)
print(df3)
print('- - - - - - - - - - - - - - - - -')
print('Accessing elements in dataframe')
print("----------------------------------")
df3 = df
df3 = df3['Y']
print(df3)
print('- - - - - - - - - - - - - - - - -')
df4 = df
df4 = df4.loc['a']
print(df4)
print('- - - - - - - - - - - - - - - - -')
df5 = df
df5 = df5.loc['a', 'Y']
print(df5)
print('- - - - - - - - - - - - - - - - -')
print('Conditional accessing in dataframe: ')
print("----------------------------------")
df6 = df
df6 = df > 3
print(df6)
print('- - - - - - - - - - - - - - - - -')
df7 = df
df7 = df[df > 3]
print(df7)
print('- - - - - - - - - - - - - - - - -')
df8 = df
df8 = df[df['Y'] > 3]
print(df8)
print('- - - - - - - - - - - - - - - - -')
df9 = df
df9 = df[df['Y'] > 3][['W','X']]
print(df9)
print('- - - - - - - - - - - - - - - - -')
df10 = df
df10 = df[(df['W'] > 0) & (df['Z'] > 5)]
print(df10)
print('- - - - - - - - - - - - - - - - -')
print('Dealing with missing Data: ')
print("----------------------------------")
d = {'a':[1,2,3,4,5], 'b':[6,7,8,9,np.nan], 'c':[0,1,2,np.nan,np.nan], 'd':[3,4,np.nan,np.nan,np.nan], 'e':[5,np.nan,np.nan,np.nan,np.nan]}
df = pd.DataFrame(d)
print(df)
print('- - - - - - - - - - - - - - - - -')
df1 = df
df1 = df1.dropna(axis= 0)
print('for rows:')
print(df1)
print('- - - - - - - - - - - - - - - - -')
df2 = df
df2 = df2.dropna(axis= 1)
print('for columns:')
print(df2)
print('- - - - - - - - - - - - - - - - -')
df3 = df
df3 = df3.dropna(thresh= 3)
print('for the matrix, with a Threshold:')
print(df3)
print('- - - - - - - - - - - - - - - - -')
df4 = df
df4 = df4.fillna(1)
print('filling the matrix, with a given value:')
print(df4)
print('- - - - - - - - - - - - - - - - -')
df5 = df
df5 = df5['b'].fillna(value= df5['b'].mean())
print('Getting and filling in the average value of a Column:')
print(df5)
print("----------------------------------")
