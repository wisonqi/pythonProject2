import pandas as pd

# Define a dictionary 'x'
x = {'Name': ['Rose', 'John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4],
     'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
     'Salary': [100000, 80000, 50000, 60000]}
# casting the dictionary to a DataFrame
df = pd.DataFrame(x)
# display the result df
df
print(df)
x1 = df[['ID']]
# print(x1)
# iloc This method does not include the last element of the range passed in it.这个方法全用下标查找,row_index,column_index
df.iloc[0, 0]
df.iloc[0, 2]
# 这个方法用标签查找，参数为loc[row_label, column_label],因为如果没有row_lable的话，系统会用数字索引，用set_index可以把一列作为indexlabel
df.set_index(keys='ID', drop=True, append=False,inplace=True)
print(df.index)
# 切记把一列作为索引后，这一列就从列中独立出去了，列会少??? 此句存疑,这个会不会少取决于drop,drop为把索引列卸掉，和append参数，append为是否将列附加到现有索引，默认为False，
# inplace对原有数据生效，用iloc方法进行查找的时候注意不要出错
print(df.loc[1, 'Salary'])
print(df.loc[1, 'Name'])

print(df.iloc[1, 0])
