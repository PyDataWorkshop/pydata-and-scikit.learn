Logistic regression

Logistic regression, despite its name, is a linear model for classification rather than regression. As such, it minimizes a “hit or miss” cost function rather than the sum of square residuals (as in ordinary regression). Logistic regression is also known in the literature as logit regression, maximum-entropy classification (MaxEnt) or the log-linear classifier.
The LogisticRegression class can be used to do L1 or L2 penalized logistic regression. L1 penalization yields sparse predicting weights. For L1 penalization sklearn.svm.l1_min_c allows to calculate the lower bound for C in order to get a non “null” (all feature weights to zero) model.
