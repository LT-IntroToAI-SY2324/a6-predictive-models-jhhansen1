import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values
plt.figure(figsize=(8,6)) 
plt.scatter(x,y)
plt.xlabel("Age (years)")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure by Age")
# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model
model = LinearRegression().fit(x, y)

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)
print(intercept)
# Print out the linear equation and r squared value
print(coef, intercept, r_squared)
# Predict the the blood pressure of someone who is 43 years old.
prediction= model.predict([[43]]) 
# Print out the prediction
print(prediction)
# Create the model in matplotlib and include the line of best fit
plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")
plt.show()