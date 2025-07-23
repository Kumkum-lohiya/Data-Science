
import pandas as pd
df_customers = pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":['Ramesh','Suresh','Kalpesh']
})

df_orders = pd.DataFrame({
    "CustomerID":[1,2,4],
    "OrderAmount":[250,450,350]
})

df_merged = pd.merge(df_customers,df_orders, on="CustomerID",how="inner")
print(df_merged)
df_merged1 = pd.merge(df_customers,df_orders, on="CustomerID",how="outer")
print(df_merged1)
df_merged2 = pd.merge(df_customers,df_orders, on="CustomerID",how="left")
print(df_merged2)
df_merged3 = pd.merge(df_customers,df_orders, on="CustomerID",how="right")
print(df_merged3)
# df_merged4 = pd.merge(df_customers,df_orders, on="CustomerID",how="cross")

# print(df_merged4)

df_concat = pd.concat([df_customers,df_orders],axis=1,ignore_index=True)
print(df_concat)