import pandas as pd
data = {
    "Name" :['Ram','Shyam','Ghanshyam','Dhanshaym','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(f"Display the dataframe\n {df}")
#selecting single column
print("Names (Single Column return series )")
name = df["Name"]
print(name)

#selecting multiple column
subset = df[["Name","Salary"]]
print("Name and salary (multiple column )")
print(subset)
