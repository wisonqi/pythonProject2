import pandas as pd

df = pd.DataFrame({'USD':'1'},columns=('Currency','Rate'))
#print(df)

#dict.iloc[1]={'EUR':'0.97'} #iloc cannot enlarge its target object
new = pd.DataFrame({'Currency':'EUR','Rate':'0.98'},index=[1])
new2 = pd.DataFrame({'Currency':'GBP','Rate':'0.8'},index=[1])
df=df._append(new,ignore_index='true')
df=df._append(new2,ignore_index='true')
df = df.set_index('Currency').to_dict()['Rate']
print(df)
