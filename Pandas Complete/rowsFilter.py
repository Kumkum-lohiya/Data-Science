import pandas as pd
data = {
    "Name" :['Ram','Shyam','Ghanshyam','Dhanshaym','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(f"Display the dataframe\n {df}")
#single condition
high_salary = df[df["Salary"] > 50000]
print(f"Employees with salary >50000\n{high_salary}")

#multiple condition
filtered = df[(df["Age"]>30) & (df["Salary"]>50000)]
print(f"Employees with age >30 and salary >50000 \n{filtered}")