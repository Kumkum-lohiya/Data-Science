#sorting data
#sorting data 1 column sort_values()
# df.sort_values(by="Column Name",True/False,inplace=True)

import pandas as pd
data = {
    "Name ":['Arun','Varun','Karun'],
    "Age" :[28,34,22],
    "Salary":[10000,20000,30000]
}

df = pd.DataFrame(data)
print(df)
print()
df.sort_values(by="Age",ascending=True,inplace=True)
print(df)

df.sort_values(by="Salary",ascending=False,inplace=True)
print(df)