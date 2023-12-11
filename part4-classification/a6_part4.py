import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
print(x)
print("_____")
print(y)
# Step 2: Standardize the data using StandardScaler, 
scale=StandardScaler().fit(x)
# Step 3: Transform the data
x=scale.transform(x)
# Step 4: Split the data into training and testing data
xtrain, xtest, ytrain, ytest= train_test_split(x, y, test_size=.2)
# Step 5: Fit the data

# Step 6: Create a LogsiticRegression object and fit the data
log_reg=linear_model.LogisticRegression()
log_reg.fit(xtrain,ytrain)
# Step 7: Print the score to see the accuracy of the model
print(log_reg.score(xtest,ytest))
# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data
print("real Y values:")
print(ytest)
print("predicted Y values:")
print(log_reg.predict(xtest))

