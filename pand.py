import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s)
print(s.index)
print(s[0])# print single value
print(s.iloc[1])
print(s[0:2])#print whole series
import pandas as pd
s = pd.Series([10, 20, 30], index=['a', 'b','c'])
print(s)
print(s.index)
print(s.loc['a'])
print("                              ")
p=pd.Series([100,200,300],index=[10,20,30])
print(p)
print(p.loc[10])
print(p.iloc[0])




# data={
#     "Name":["Pratik","Rohit","Ritik","Avi"],
#     "Age":[23,20,25,18],
#     "Department":["HR","Fiance","IT","HR"],
#     "Salary":[75000,50000,70000,40000]
# }

import numpy as np

data = {
    "Name": ["Alice kuntawar", "Bob kuntawar", "Charlie kuntawar", "David kuntawar", "Eve kuntawar", "Alice kuntawar"],
    "Age": [25.0, 30.0, 35.0, np.nan, 29.0, 25.0],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [55000.0, 65000.0, 75000.0, 67000.0, np.nan, 55000.0],
}

df=pd.DataFrame(data)
print(df)
print(df.head(3))#to print first 3 rows
print(df.tail(3))#to print last 3 rows
print(df.iloc[1:3])#to fetch row 1 and 2
print(df.loc[1:3,["Name","Age","Department"]])#to fetch row having index 1 and 2#in loc both starting and last index are included
print("                                   ")
print(df.drop("Age",axis=1))
print("                                   ")
print(df)

print(df.shape)# to get nonof rows and columns present in df
print(df.info())# to get details about dataframe
print(df.describe())# to get count,max value,min value,std deviation of each integer column

#broadcasting
df["Salary"]=df["Salary"]+5000
print(df)
df.rename(columns={"Department":"Dept"},inplace=True)
print(df)
print("                                ")
print(df["Dept"].unique())# to get uniques of a column
print(df["Dept"].value_counts())# koni value kitni baar aayi column mein yeh janne ke liye
df["Promoted Salary"]=df["Salary"]*10

print(df)
print("Null Values in each column")
print(df.isnull().sum())

#df.dropna(inplace=True)# whatever row contains null value,that row will be deleted from table
df.dropna(how='all',inplace=True)#if all column vales are null only then remove that row
print("                          ")
print(df)
#df.fillna(0,inplace=True)# here fillna means fill all null values with and if we pass parameter as 0,means fill all null values with 0
print("                              ")
print(df)
#print(df["Age"].fillna(df["Age"].mean()))
print(df["Age"].fillna(method="bfill"))
print(df["Salary"].fillna(df["Salary"].median()))
print(df)
df_dup=df[df.duplicated(keep="first")]
print(df_dup)
#print(df.drop_duplicates())# here duplicate records will be droped
df[["FirstName","LastName"]]=df["Name"].str.split(" ",expand=True)
df.drop(columns=["Name"], inplace=True)
df=df[["FirstName","LastName","Age","Dept","Salary","Promoted Salary"]]
print(df["Age"].apply(lambda x:x*2))
print(df)

department_info={
"Dept":["HR","IT","Finance"],
"Location":["New York","San Fransisco","Chicago"],
"Manager":["Laura","Steve","Nina"]
}
df2=pd.DataFrame(department_info)
print("Merging vertically")
print(pd.concat([df,df2]))
print("Merging Horizantally")
print(pd.concat([df,df2],axis=1))
print("Perform Merging")
print(pd.merge(df,df2, on="Dept"))#IT IS INNER JOIN BY DEFAULT




inner_join = pd.merge(df, df2, on="Dept", how="inner")

# LEFT JOIN
left_join = pd.merge(df, df2, on="Dept", how="left")

# RIGHT JOIN
right_join = pd.merge(df, df2, on="Dept", how="right")

# OUTER JOIN
outer_join = pd.merge(df, df2, on="Dept", how="outer")

print("----- INNER JOIN -----")
print(inner_join)
print("\n----- LEFT JOIN -----")
print(left_join)
print("\n----- RIGHT JOIN -----")
print(right_join)
print("\n----- OUTER JOIN -----")
print(outer_join)

print("Print cs file")
data=pd.read_csv("/Users/consultadd/Desktop/data.txt")
print(data)