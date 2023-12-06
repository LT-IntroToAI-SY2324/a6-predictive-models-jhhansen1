import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest= train_test_split(x, y, test_size=.2)
#create linear regression model
model= LinearRegression().fit(xtrain, ytrain)
#Find and print the coefficients, intercept, and r squared values.
coef = np.round(model.coef_, 2)
intercept = np.round(float(model.intercept_), 2)
r_squared = np.round(model.score(x, y),2)
#Each should be rounded to two decimal places. 
prediction= model.predict(xtest)

#Loop through the data and print out the predicted prices and the 
#actual prices
for i in range(len(xtest)):
    print(ytest[i])
    print(prediction[i])
print("***************")
print("Testing Results")
print(model.prediction(np.array[[89000,10]]))