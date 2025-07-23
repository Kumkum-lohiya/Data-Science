import pandas as pd
data = {
    "Name ":['Arun','Varun','Karun'],
    "Age" :[28,34,22],
    "Salary":[10000,20000,30000]
}
df = pd.DataFrame(data)
print(df)

agv_Salary = df["Salary"].mean()
print(agv_Salary)