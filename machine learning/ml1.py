import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from matplotlib.animation import FuncAnimation
from sklearn.model_selection import train_test_split

url = r"C:\Users\sriha\Downloads\house-prices.csv"
data = pd.read_csv(url)
print(data)

'''data = data.dropna()

print(data)
'''
print(data.shape)
print(data.head())
print(data.describe())
print(data.info())
print(data.tail())

x = data[['SqFt']]
y = data[["Price"]]

print(x)
print(y)
# Split the data (80% for training, 20% for testing)

'''print(data.info())
print(data.describe())'''

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
# Train the model using the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Plot the training data points
plt.scatter(X_train, y_train, color='blue', label='Actual data')

# Plot the regression line using the test data points and the predicted values
plt.plot(X_test, y_pred, color='red', label='Regression line')

plt.xlabel('SqFt')
plt.ylabel('Price')
plt.title('Linear Regression')
plt.legend()
plt.show()