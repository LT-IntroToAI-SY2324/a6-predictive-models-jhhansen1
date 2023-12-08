# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data? The R-squared value I got was 0.86 this means that the data is mostly linear but the correlation is not that strong.

2. Is your model accurate? Why or why not? The model is fairly accurate, almost all of the predictions the model made was within a few thousand of the accurate price however the predictions are far frome perfect.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
the first car is worth 9186.52904028 while the second car is worth 2047.94514798
4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening? The model is only accurate within a certain boundry of value and age, once the values for age and mileage get large enough the graph no longer becomes accurate.