import pandas as pd
# df = pd.read_json("sample_Data.json")
data = {
    "Name" :['Ram','Shyam','Ghanshayam'],
    "Age"  :[10,20,30],
    "City" :['Nagpur','Mumbai','Dehli']
}
df = pd.DataFrame(data)
print("Displaying the info of data set ")
print(df.info())