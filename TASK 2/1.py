import pandas as p

data = p.read_csv("01.Data Cleaning and Preprocessing.csv")

print("\nTYPE\n")
print(type(data))

print("\nINFO\n")
print(data.info())

print("\nDESCRIBE\n")
print(data.describe())
