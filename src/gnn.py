import numpy as np

class GNN:
    def __init__(self, graph, theta):
        self.graph = graph
        self.theta = theta
        self.x = np.eye(self.graph.n, self.theta.hp.d)[np.arange(self.graph.n)%self.theta.hp.d]

    def relu(self, x):          # Relu function
        return np.maximum(0,x)

    def sigmoid(self, x):       # Sigmoid function
        return 1/(1+np.exp(-x))

    def steps(self):   # Step
        for i in range(self.theta.hp.step):
            x = self.x if i==0 else self.xx
            self.a = np.array([np.sum(x[self.graph.adjacent[i] == 1], axis=0) for i in range(self.graph.n)]) # Aggregation 1
            self.xx = self.relu(self.a.dot(self.theta.weight)) # Aggregation 2
        
    def predict(self):          
        self.h = np.sum(self.xx, axis=0) # Readout
        self.s = self.h.dot(self.theta.A) + self.theta.b
        self.p = self.sigmoid(self.s)
        self.predicty = 1 if self.p > 0.5 else 0 # Prediction

    def crossentropyloss(self): # Binary cross entropy loss
        delta = 1e-7
        self.l = -self.graph.y*np.log(self.p+delta)-(1-self.graph.y)*np.log(1-self.p+delta)

    def numericalgradient(self, unrolled_weight, A, b):
        for i in range(self.theta.hp.step):
            tempx = self.x if i == 0 else tempx
            tempa = np.array([np.sum(tempx[self.graph.adjacent[i] == 1], axis=0) for i in range(self.graph.n)])
            tempx = self.relu(tempa.dot(unrolled_weight.reshape(self.theta.hp.d, self.theta.hp.d)))
        temph = np.sum(tempx, axis=0)
        temps = temph.dot(A) + b
        tempp = self.sigmoid(temps)
        delta = 1e-7
        templ = -self.graph.y*np.log(tempp+delta)-(1-self.graph.y)*np.log(1-tempp+delta)
        return (templ-self.l)/self.theta.hp.epsilon

    def gradweight(self):        
        return np.array([self.numericalgradient(self.theta.weight.reshape(-1) + self.theta.hp.epsilon*np.eye(1, self.theta.weight.size, i), self.theta.A, self.theta.b) for i in range(self.theta.weight.size)]).reshape(self.theta.hp.d, self.theta.hp.d)

    def gradA(self):
        return np.array([self.numericalgradient(self.theta.weight.reshape(-1), self.theta.A + self.theta.hp.epsilon*np.squeeze(np.eye(1, self.theta.A.size, i)), self.theta.b) for i in range(self.theta.A.size)])

    def gradb(self):
        return self.numericalgradient(self.theta.weight.reshape(-1), self.theta.A, self.theta.b + self.theta.hp.epsilon)

    def gradtheta(self):
        self.theta.gradweight = self.theta.gradweight + self.gradweight()
        self.theta.gradA = self.theta.gradA + self.gradA()
        self.theta.gradb = self.theta.gradb + self.gradb()

    def gradientdescent(self):  
        self.steps()
        self.predict()
        self.crossentropyloss()
        self.gradtheta()        
