import pandas as pd
df = pd.DataFrame({
    "days":[1,2,3,4,5,6],
    "eng":[10,12,14,15,16,12],
    "maths":[17,18,19,13,14,16],
    "Name":["a","b","c","d","e","f"]
})
print(df)
#reshape the data frame
print(pd.melt(df))
print(pd.melt(df,id_vars=["eng"],var_name="python",value_name="wscube"))


#pivot()
print(df.pivot(index="days",columns="Name",values="eng"))


print(df.pivot_table(index="Name",columns="days",aggfunc="sum",margins=True))