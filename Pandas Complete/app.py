import pandas as pd
from pandas import read_json

#read data from csv file into a dataframe
# df = pd.read_csv("sales_data_sample.csv",encoding="utf-8")
# df1 = pd.read_csv("sales_data_sample.csv",encoding="latin1")
# utf-8 and latin1 are two encoding methods
# print(df1)
# df2 = pd.read_excel("SampleSuperstore.xlsx",engine='openpyxl')
# print(df2)
df3 = pd,read_json("sample_Data.json",encoding="latin1")
print(df3)

#
