import pandas as pd
data = {
    "Name" :['Ram','Shyam','Ghanshyam','Dhanshaym','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
#square brackets df["Column Name"] = some data
print(df)
print()
df["Bonus"] = df["Salary"]*0.1
print(df)

#using insert method
#df.insert(loc,"column name",some data")
df.insert(0,"Employee id",[10,20,30,40,50,60,70,80])
print(df)