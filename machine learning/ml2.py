import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

path = r"C:\Users\sriha\Downloads\house-prices.csv"
data = pd.read_csv(path)
print(data)

print(data.head())
print(data.shape)

x=data[['sqFt']]
y=data[["price"]]

print(x)
print(y)

