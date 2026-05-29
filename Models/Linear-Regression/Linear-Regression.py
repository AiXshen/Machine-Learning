#LINEAR REGRESSION USING GRADIENT 

import numpy as np
class LinearRegression:
    def __init__ (self,learning_rate = 0.01,iterations = 1000):                            #Inititalisationi of Linear Regression Model
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None


    
    def fit(self,X_matrix,y_matrix):
        samples , features = X_matrix.shape                                                 # For m * n matrix there are m rows and n columns i.e.,
        self.weights = np.zeros(features)                                                   # Each row contributes to one sample -  therefore total m samples 
        self.bias = 0                                                                       # Each columns contributes  to one Type of feature - total n feature

        
        for i in range (self.iterations):
            y_predicted_matrix = np.dot(X_matrix, self.weights) + self.bias                 # np.dot (X_matrix , weight) is a simple multiplicaton
            
            dw = 1/samples * np.dot(X_matrix.T ,(y_predicted_matrix - y_matrix))            #dw and db are derivative of Costfunction/MeanSquareError (MSE)
            db = 1/samples * np.sum( y_predicted_matrix - y_matrix)                         #MSE = 1/total no. of samples *   (y predicted -y)**2 
            
            self.weights = self.weights - self.lr * dw     # Current weights are adjusted by a small amount (learning rate × gradient)
            self.bias = self.bias - self.lr * db           # Gradient indicates how to change parameters to reduce MSE
    

    def predict ( self , X_matrix) :
            y_predicted_matrix = np.dot(X_matrix, self.weights)  + self.bias
            return y_predicted_matrix;



