# import pandas as pd
# data={'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35]}
# df=pd.DataFrame(data)
# print(df)


# import pandas as pd
# s=pd.Series([10,20,30,40,50])
# print(s[2])
# print(s.dtype)

# import pandas as pd
# data={
#     'Name': ['David', 'Eva', 'Frank'],
#     'Age': [28, 22, 33]    
# }
# df=pd.DataFrame(data)
# print(df)
# print(df['Name'])
# print(df['Age'])

# import pandas as pd
# df=pd.DataFrame({
#     'A': [1,2,3],
#     'B': [4,5,6],
#     'C': [7,8,9]
# })
# print(df['A'])
# print(df.loc[1])
# print(df.iloc[0:1])
# print(df[df['B']>4])
# df['D']=df['A']=df['B']
# df['E']=df['C']+df['A']
# df['F']=df['E']*4
# print(df)
# df.loc[0,'A']=12
# print(df)
# df=df.drop('C',)
# print(df)
# df=df.rename(columns={'A':'Alpha'})
# print(df)
# print(df[df['A']>30])
# print(df[(df['A'] < 3) & (df['B'] > 4)])
# print(df.sort_values(by='C', ascending=False))

# import pandas as pd
# df=pd.DataFrame({
#        'Team': ['A', 'B', 'A', 'B'],
#          'Points': [10, 15, 20, 25]
# })
# df=df.groupby('Team').sum() 
# print(df)

# import pandas as pd
# df1=pd.DataFrame({'A':[1,2,3]},index=['x','y','z'])
# df2=pd.DataFrame({'B':[4,5,6]},index=['x','y','z'])

# print(df1.join(df2))

# import pandas as pd
# df1=pd.DataFrame({'A':[1,2,3]})
# df2=pd.DataFrame({'A':[4,5,6]})
# print(pd.concat([df1,df2]))
# print(pd.concat([df1,df2], axis=1))

import pandas as pd
df=pd.DataFrame({
    'Date': ['2025-01-01','2025-01-02','2025-01-03']
})
df['Date']=pd.to_datetime(df['Date'])
print(df['Date'].dt.month)
print(df['Date'].dt.day)

print(df[df['Date']>'2025-01-05'])