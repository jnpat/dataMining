import numpy as np
import pandas as pd 
from random import shuffle
from sklearn.model_selection import train_test_split
  

# reading csv file  
read = pd.read_csv("drug_consumption.csv")
#get x (input from csv file)
x = read[['Age','Gender','Education','Country',
              'Ethnicity','Nscore','Escore','Oscore','Ascore',
              'Cscore','Impulsive','SS']]
#get y (output from s\csv file)
y = read[['AlClass/0','AlClass/1','AlClass/2','AlClass/3',
              'AlClass/4','AlClass/5','AlClass/6']]
#show x/y read from csv file
# print(x)
# print(y)
#random train/test set
xTrain , xTest , yTrain , yTest = train_test_split(x,y,train_size=0.7,test_size = 0.3,random_state = 40)
#get train/test input after random set
trainInput = np.array(xTrain)
testInput = np.array(xTest)
#get train/test output after random set
trainOutput = np.array(yTrain)
testOutput = np.array(yTest)

print(trainInput.shape)

class Neural_Network(object):
  def __init__(self):
  #parameters
    self.inputSize = 12
    self.outputSize = 7
    self.hiddenSize = 5
    self.learningRate = -0.9

  #weights
    self.W1 = 2 * np.random.randn(self.inputSize, self.hiddenSize) - 1# (12*8) weight matrix from input to hidden layer
    self.W2 = 2 * np.random.randn(self.hiddenSize, self.outputSize) - 1 # (8*7) weight matrix from hidden to output layer

  def forward(self, X):
    #forward propagation through our network
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 12*8 weights
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 8*7 weights
    o = self.sigmoid(self.z3) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    #derivative of sigmoid
    return (s) * (1 - (s))

  def backward(self, X, y, o):
    # backward propagate through the network
    self.o_error = y - o # error in output
    self.o_gradient = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error
    self.o_delta = -self.learningRate * self.o_gradient

    self.h_error = self.o_gradient.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
    self.h_gradient = self.h_error * self.sigmoidPrime(self.z2)
    self.h_delta = -self.learningRate * self.h_gradient # applying derivative of sigmoid to z2 error

    self.W1 += X.T.dot(self.h_delta) # adjusting first set (input --> hidden) weights
    self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

  def train(self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

  def saveWeights(self):
    np.savetxt("w1.txt", self.W1, fmt="%s")
    np.savetxt("w2.txt", self.W2, fmt="%s")

  def predict(self):
    f = open("NN1.txt","w+")

    f.write ("Predicted data based on trained weights: ")
    f.write ("Input (scaled): \n" + str(testInput))
    f.write ("Output: \n" + str(self.forward(testInput)))

    f.close()

NN = Neural_Network()

# f = open("NN.txt","w+")

# for i in range(1000): # trains the NN 1,000 times
#   f.write ("# " + str(i) + "\n")
#   f.write ("Input (scaled): \n" + str(trainInput) + "\n")
#   f.write ("Output (scaled): \n" + str(trainOutput) + "\n")
#   f.write ("Actual Output: \n" + str(y) + "\n")
#   f.write ("Predicted Output: \n" + str(NN.forward(trainInput)) + "\n")
#   f.write ("\n")
#   NN.train(trainInput, trainOutput)

# f.close()

f = open("NN.txt","w+")

for i in range(1000): #trains the NN 1000 times
    NN.train(trainInput,trainOutput)

Y = testOutput
y = NN.forward(testInput) 
Loss = 0
for i in range(len(y)):
    Loss += ((Y[i]-y[i])**2)/len(y)
    f.write("Output \n" + str(Y[i]) + "\n" + "Predicted Output \n" + str(y[i]) + "\n")
    

f.write("Loss = " + str(Loss))

f.close()

NN.saveWeights()
NN.predict()

print(NN.W1)
