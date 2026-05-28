import numpy as np
class Polynomial_Regression:
    def __init__(self , degree = 2, learning_rate = 0.01 , iteration = 1000):
        self.degree = degree
        self.lr = learning_rate
        self.iteration = iteration
        self.weight = None
        self.bias  = None


    def Polynomial_Feature (self , X):
        X_copy = X.copy()
        for i in range ( 2, self.degree + 1):
            X_copy = np.c_[X_copy , X ** i]

        return X_copy

    def fit (self, X , y ):
        X_polynomial = self.Polynomial_Feature(X)
        samples , features = X_polynomial.shape
        self.weight = np.zeros(features)
        self.bias  = 0
        for i  in range (self.iteration):
            y_predicted = np.dot(X_polynomial , self.weight) + self.bias
            dw = (1 / samples) * (np.dot(X_polynomial.T , (y_predicted -  y)))
            db = ( 1/samples) * (np.sum(y_predicted - y))

            self.weight = self.weight - self.lr * dw
            self.bias = self.bias  - self.lr * db


    def predict (self, X ):
        x_polynomial = self.Polynomial_Feature(X)
        y_predicted = np.dot(x_polynomial , self.weight) + self.bias
        return y_predicted
