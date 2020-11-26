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
print('- - - - - - - - - - - - - - - - -')
print('Analysing data using groupby: ')
print("----------------------------------")
p = {'item':['apple','apple','orange','orange','gun','gun','gun'], 'day':['mon','tue','wed','thu','fri','sat','sun'], 'sales':[100,20,48,54,6,1,33]}
print(p)
print('- - - - - - - - - - - - - - - - -')
df = pd.DataFrame(p)
print('put in a dataframe:')
print(df)
print('- - - - - - - - - - - - - - - - -')
x = df.groupby('item')
averageSalesPerItem = x.mean()
print(x)
print('getting the average sales per item:')
print(averageSalesPerItem)
print('- - - - - - - - - - - - - - - - -')
totalSalesPerItem = x.sum()
print('getting the total sales per item:')
print(totalSalesPerItem)
print('- - - - - - - - - - - - - - - - -')
standardDeviationPerItem = x.std()
print('standard deviation per item:')
print(standardDeviationPerItem)
print('- - - - - - - - - - - - - - - - -')
countDaysPerItem = x.count()
print('selling days per item:')
print(countDaysPerItem)
print('- - - - - - - - - - - - - - - - -')
describeTheWholeTablePerItem = x.describe()
print('Or simply dewcribe the whole table per item:')
print(describeTheWholeTablePerItem)
print('- - - - - - - - - - - - - - - - -')
tableTransposed = x.describe().transpose()
print(tableTransposed)
print('- - - - - - - - - - - - - - - - -')
print('Joining DataFrames: ')
print("----------------------------------")
print('dictionaries:')
d1 = {'a':[1,2,3], 'b':[4,5,6]}
print(d1)
d2 = {'c':[3,4,5], 'd':[2,3,6]}
print(d2)
x = pd.DataFrame(d1, index = ['p1','p2','p3'])
y = pd.DataFrame(d2, index = ['p1','p2','p3'])
print()
print('converted to dataframes:')
print(x)
print()
print(y)
print('- - - - - - - - - - - - - - - - -')
joinedDs = x.join(y)
print('dataframes joined:')
print(joinedDs)
print('- - - - - - - - - - - - - - - - -')
print('Concatenating df: ')
print("----------------------------------")
print('dictionaries:')
d1 = {'a':[1,1,1,1,1], 'b':[1,1,1,1,1], 'c':[1,1,1,1,1], 'd':[1,1,1,1,1], 'e':[1,1,1,1,1]}
print(d1)
d2 = {'e':[2,2,2,2,2], 'f':[2,2,2,2,2], 'g':[2,2,2,2,2], 'h':[2,2,2,2,2], 'i':[2,2,2,2,2]}
print(d2)
d3 = {'a':[3,3,3,3,3], 'b':[3,3,3,3,3], 'c':[3,3,3,3,3], 'd':[3,3,3,3,3], 'e':[3,3,3,3,3]}
print(d3)
df1 = pd.DataFrame(d1, index = [1,2,3,4,5])
df2 = pd.DataFrame(d2, index = [1,2,3,4,5])
df3 = pd.DataFrame(d3, index = [5,6,7,8,9])
print()
print('converted to dataframes:')
print(df1)
print()
print(df2)
print()
print(df3)
print('- - - - - - - - - - - - - - - - -')
concatDs = pd.concat([df1, df2, df3])
concatDs1 = pd.concat([df1,df2,df3], axis = 1)
print('dataframes concatenated:')
print(concatDs)
print()
print(concatDs1)
print()
a = pd.concat([df1, df2], axis = 1)
print(a)
print()
b = pd.concat([df1, df3], axis = 0)
print(b)
print('- - - - - - - - - - - - - - - - -')
print('Merging df: ')
print("----------------------------------")
df1 = pd.DataFrame({'key1':[1,2,3], 'a':[2,3,4], 'b':[5,6,7]})
df2 = pd.DataFrame({'key1':[1,2,3], 'c':[1,2,9], 'd':[5,8,9]})
print('dataframes:')
print(df1)
print()
print(df2)
print('- - - - - - - - - - - - - - - - -')
mergedDFs = pd.merge(df1,df2)
print('and merged here: ')
print(mergedDFs)
print('- - - - - - - - - - - - - - - - -')
print('More Operations: ')
print("----------------------------------")
x = pd.DataFrame({'a':[1,2,3,4,5], 'b':[20,20,30,60,50]})
print('dataframe:')
print(x)
print()
print('- - - - - - - - - - - - - - - - -')
a = x.index
print('.index: ')
print(a)
print('- - - - - - - - - - - - - - - - -')
a = x.columns
print('.columns: ')
print(a)
print('- - - - - - - - - - - - - - - - -')
def inc(x):
	x = x + 100
	return x
a = x.apply(inc)
b = x['b'].apply(inc)
print('.apply(function): ')
print(a)
print()
print(b)
print('- - - - - - - - - - - - - - - - -')
a = x.sort_values('b')
print('.sort_values(columnName): ')
print(a)
print('- - - - - - - - - - - - - - - - -')
a = x['b'].unique()
print('.unique(): ')
print(a)
print('- - - - - - - - - - - - - - - - -')
a = x['b'].nunique()
print('.nunique() or number of unique ones: ')
print(a)
print('- - - - - - - - - - - - - - - - -')
a = x['b'].value_counts()
print('.value_counts() or number of times the value occurs: ')
print(a)
print('- - - - - - - - - - - - - - - - -')
a = x.isnull()
print('.isnull() or check if a value in the df is null: ')
print(a)
print('- - - - - - - - - - - - - - - - -')
print('Loading data using pandas: ')
print("----------------------------------")
print('json -> dictionarry in files')
print('csv -> dataframe in form of files')
print('html -> data in files')
print('excel -> data in files')
print('- - - - - - - - - - - - - - - - -')
print('csv file loaded: ')
print()
x = pd.read_csv('188.iris.csv')
print(x)
print('- - - - - - - - - - - - - - - - -')

print("----------------------------------")
