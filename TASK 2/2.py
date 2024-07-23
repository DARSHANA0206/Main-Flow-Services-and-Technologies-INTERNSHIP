import pandas as p

data = p.read_csv("01.Data Cleaning and Preprocessing.csv")

print("\nDUPLICATE\n")
data1 = data.drop_duplicates()
print(data1)

print("\nNULL\n")
data2 = data.isnull()
print(data2)

print("\nNULL.SUM\n")
data3 = data.isnull().sum()
print(data3)

print("\nNOTNULL\n")
data4 = data.notnull()
print(data4)

print("\nNULL.SUM.SUM\n")
data5 = data.isnull().sum().sum()
print(data5)

print("\nHANDLING METHOD 1\n")
data6 = data.fillna(value = 0)
print(data6)

print("\nHANDLING METHOD 2\n")
data7 = data.fillna(method = "pad")
print(data7)

print("\nHANDLING METHOD 3\n")
data8 = data.fillna(method = "bfill")
print(data8)
