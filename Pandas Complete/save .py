import pandas as pd
# creation of dataframe
data = {
    "Name" :['Ram','Shyam','Ghanshayam'],
    "Age"  :[10,20,30],
    "City" :['Nagpur','Mumbai','Dehli']
}
df = pd.DataFrame(data)
print(df)
# df.to_csv("output.csv",index = False)
# df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)