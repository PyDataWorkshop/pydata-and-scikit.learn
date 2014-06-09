# Diabetes dataset
# - http://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html
# - The diabetes dataset consists of 10 physiological variables (age, sex, weight, blood pressure) 
# - measure on 442 patients, and an indication of disease progression after one year:
 
 diabetes = datasets.load_diabetes()
 diabetes_X_train = diabetes.data[:-20]
 diabetes_X_test  = diabetes.data[-20:]
 diabetes_y_train = diabetes.target[:-20]
 diabetes_y_test  = diabetes.target[-20:]

# The task at hand is to predict disease progression from physiological variables.
