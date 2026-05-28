#LINEAR REGRESSION USING GRADIENT 

import numpy as np
class LinearRegression:
    def __init__ (self,learning_rate = 0.01,iterations = 1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def fit(self,X,y):
        samples , features = X.shape
        self.weights = np.zeros(features)
        self.bias = 0
        for i in range (self.iterations):
            y_predicted = np.dot(X, self.weights) + self.bias

            dw = 1/samples * np.dot(X.T ,(y_predicted - y))
            db = 1/samples * np.sum( y_predicted - y)

            self.weights = self.weights - self.lr *dw
            self.bias = self.bias - self.lr *db

    def predict ( self , X) :
            y_predicted = np.dot(X, self.weights)  + self.bias
            return y_predicted;



