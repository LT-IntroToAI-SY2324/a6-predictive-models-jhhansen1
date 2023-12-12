# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
the accuracy score of my model dropped from .85 to .65 after commenting out the standard scaler.   
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
I would say that 7/8 accuracy is accurate enough for what the goal of this model is since we are just predicting if someone is going to buy a car you are not always going to be correct.
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model was fairly accurate I counted that 10 values were predicted innacurately which means that 1/8 of the predicted answers were incorrect. I couldnt find any pattern to the values that were inaccurately predicted.
4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.She would most likely not buy the suv according to the model because when you input the data a 0 is returned meaning false

