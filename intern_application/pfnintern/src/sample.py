import numpy as np
import matplotlib.pyplot as plt

class HP:        
    def __init__(self, step=None, d=None, lr=None, moment=None,moment2 = None, epsilon=None, epoch=None, trainsize=None, batchsize=None, validation_rate=None, testsize=None):
        self.step = step if step is not None else 2
        self.d = d if d is not None else 8
        self.lr = lr if lr is not None else 0.0001
        self.beta = moment if moment is not None else 0.9
        self.beta2 = moment2 if moment2 is not None else 0.99
        self.epsilon = epsilon if epsilon is not None else 0.001
        self.epoch = epoch if epoch is not None else 10
        self.trainsize = trainsize if trainsize is not None else 2000
        self.batchsize = batchsize if batchsize is not None else 100
        self.vr = validation_rate if validation_rate is not None else 0.2
        self.testsize = testsize if testsize is not None else 500

class THETA:
    def __init__(self, hp):
        self.hp = hp
        self.weight = 0.4*np.random.randn(hp.d,hp.d)
        self.A = 0.4*np.random.randn(hp.d)
        self.b = 0
        self.gradweight = np.zeros((hp.d,hp.d))
        self.gradA = np.zeros(hp.d)
        self.gradb = 0
        # For momentum SGD
        self.prevgradweight = np.zeros((hp.d, hp.d))
        self.prevgradA = np.zeros(hp.d)
        self.prevgradb = 0
        # For adam
        self.t = 0
        self.mweight = np.zeros((hp.d, hp.d))
        self.mA = np.zeros(hp.d)
        self.mb = 0
        self.vweight = np.zeros((hp.d, hp.d))
        self.vA = np.zeros(hp.d)
        self.vb = 0
        

    def update(self):
        self.weight = self.weight - self.hp.lr * self.gradweight /self.hp.batchsize
        self.A = self.A - self.hp.lr * self.gradA /self.hp.batchsize
        self.b = self.b - self.hp.lr * self.gradb /self.hp.batchsize
        self.gradweight = np.zeros((self.hp.d, self.hp.d))
        self.gradA = np.zeros(self.hp.d)
        self.gradb = 0


    def momupdate(self):
        self.weight = self.weight - self.hp.lr * self.gradweight /self.hp.batchsize + self.hp.beta * self.prevgradweight
        self.A = self.A - self.hp.lr * self.gradA /self.hp.batchsize + self.hp.beta * self.prevgradA
        self.b = self.b - self.hp.lr * self.gradb /self.hp.batchsize + self.hp.beta * self.prevgradb
        self.prevgradweight =  - self.hp.lr * self.gradweight /self.hp.batchsize + self.hp.beta * self.prevgradweight
        self.prevgradA = - self.hp.lr * self.gradA /self.hp.batchsize + self.hp.beta * self.prevgradA
        self.prevgradb = - self.hp.lr * self.gradb /self.hp.batchsize + self.hp.beta * self.prevgradb
        self.gradweight = np.zeros((self.hp.d, self.hp.d))
        self.gradA = np.zeros(self.hp.d)
        self.gradb = 0


    def adamupdate(self):
        self.t += 1
        self.mweight = self.hp.beta * self.mweight + (1-self.hp.beta) * self.gradweight / (1-self.hp.beta**self.t )
        self.mA = self.hp.beta * self.mA + (1-self.hp.beta) * self.gradA   / (1-self.hp.beta**self.t )
        self.mb = self.hp.beta * self.mb + (1-self.hp.beta) * self.gradb  / (1-self.hp.beta**self.t )
        self.vweight = self.hp.beta2 * self.vweight + (1-self.hp.beta2) * self.gradweight * self.gradweight   / (1-self.hp.beta2**self.t )
        self.vA = self.hp.beta2 * self.vA + (1-self.hp.beta2) * self.gradA * self.gradA / (1-self.hp.beta2**self.t )
        self.vb = self.hp.beta2 * self.vb + (1-self.hp.beta2) * self.gradb * self.gradb / (1-self.hp.beta2**self.t )
        self.weight = self.weight - self.hp.lr * self.mweight / np.sqrt(self.vweight + 1e-7)
        self.A = self.A - self.hp.lr * self.mA / np.sqrt(self.vA + 1e-7)
        self.b = self.b - self.hp.lr * self.mb / np.sqrt(self.vb + 1e-7)
        self.gradweight = np.zeros((self.hp.d, self.hp.d))
        self.gradA = np.zeros(self.hp.d)
        self.gradb = 0

        
        

class GRAPH:
    def __init__(self, n, adjacent, y):
        self.n = n
        self.adjacent = adjacent
        self.y = y

# adjacent: adjacent matix (numpy.ndarray)
# d: dimention (int)
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

        
class SGD:
    # batch size should be a divisor of the trainsize
    def __init__(self, theta):
        self.theta = theta
        self.trainloss = []    # average training set loss
        self.validloss = []    # average validation set loss
        self.trainacc = []     # average training set accuracy
        self.validacc = []     # average validation set accuracy
        self.testresult = []   # test result
        

    def validationset(self):
        self.validationmask = np.random.choice(self.theta.hp.trainsize, int(self.theta.hp.trainsize*self.theta.hp.vr), replace = False, p = self.pweights/np.sum(self.pweights))
        self.pweights[self.validationmask] = 0
        self.trainingmask = np.where(self.pweights == 1)[0]
        self.traindatapweights = np.copy(self.pweights)
        
    def maskgen(self):          # batch mask generator
        self.batchmask = np.random.choice(self.theta.hp.trainsize, self.theta.hp.batchsize, replace=False, p = self.pweights/np.sum(self.pweights))
        self.pweights[self.batchmask] = 0 # selection probability weights


    def batchupdatetheta(self):
        # accumulated training set loss
        self.acctrainloss = 0
        # accumulated validation set loss
        self.accvalidloss = 0
        # accumlated training set accuracy
        self.acctrainacc = 0
        # accumlated validation set accuracy
        self.accvalidacc = 0
        
        for i in self.batchmask:
            self.adjacent = np.loadtxt(
                fname='datasets/train/{}_graph.txt'.format(i),
                skiprows=1
            )
            self.n = self.adjacent.shape[0]
            self.y = np.loadtxt('datasets/train/{}_label.txt'.format(i))
            graph = GRAPH(self.n, self.adjacent, self.y)
            gnn = GNN(graph, self.theta)
            # accumulate each gradient
            gnn.gradientdescent()
      
        #update theta
        #SGD: self.theta.update()
        #MOMSGD: self.theta.momupdate()
        #ADAMSGD: self.theta.adamupdate()
        self.theta.adamupdate()
        
        # training accuracy
        for i in self.trainingmask:
            self.adjacent = np.loadtxt(
                fname='datasets/train/{}_graph.txt'.format(i),
                skiprows=1
            )
            self.n = self.adjacent.shape[0]
            self.y = np.loadtxt('datasets/train/{}_label.txt'.format(i))
            graph = GRAPH(self.n, self.adjacent, self.y)
            gnn = GNN(graph, self.theta)
            gnn.steps()
            gnn.predict()
            gnn.crossentropyloss()
            self.acctrainloss = self.acctrainloss + gnn.l
            self.acctrainacc += 1 if self.y == gnn.predicty else 0
                                
#         print("training loss {}, training point {}".format(self.acctrainloss, self.acctrainacc))
        self.trainacc.append(self.acctrainacc/(int(self.theta.hp.trainsize*(1-self.theta.hp.vr))))
        self.trainloss.append(self.acctrainloss/(int(self.theta.hp.trainsize*(1-self.theta.hp.vr))))
       
            
        
        # validation set
#         print(self.validationmask)
        for i in self.validationmask:
            self.adjacent = np.loadtxt(
                fname='datasets/train/{}_graph.txt'.format(i),
                skiprows=1
            )
            self.n = self.adjacent.shape[0]
            self.y = np.loadtxt('datasets/train/{}_label.txt'.format(i))
            graph = GRAPH(self.n, self.adjacent, self.y)
            gnn = GNN(graph, self.theta)
            gnn.steps()
            gnn.predict()
            gnn.crossentropyloss()
#             print("graph: {}".format(i))
#             print("target: {}".format(self.y))
#             print("answer: {}".format(gnn.predicty))
            self.accvalidloss = self.accvalidloss + gnn.l
            self.accvalidacc += 1 if self.y == gnn.predicty else 0

#         print("validation loss {}, validation point {}".format(self.accvalidloss, self.accvalidacc))        
        self.validacc.append(self.accvalidacc/(int(self.theta.hp.trainsize*self.theta.hp.vr)))
        self.validloss.append(self.accvalidloss/(int(self.theta.hp.trainsize*self.theta.hp.vr)))

    def gooneepoch(self):
        self.pweights = np.copy(self.traindatapweights) # selection probability weights for choosing the batch
        print(int(self.theta.hp.trainsize*(1-self.theta.hp.vr)/self.theta.hp.batchsize))
        for i in range(int(self.theta.hp.trainsize*(1-self.theta.hp.vr)/self.theta.hp.batchsize)):
            self.maskgen()
            self.batchupdatetheta()
    
    def train(self):
        self.pweights = np.ones(self.theta.hp.trainsize) # selection probability weights for choosing the batch
        self.validationset()
        for i in range(self.theta.hp.epoch):
            self.gooneepoch()
            print("{} epoch done".format(i+1))

    def test(self):
        for i in range(self.theta.hp.testsize):
            self.adjacent = np.loadtxt('datasets/test/{}_graph.txt'.format(i), skiprows=1)
            self.n = adjacent.shape[0]
            self.y = -1
            graph = GRAPH(self.n, self.adjacent, self.y)
            gnn = GNN(graph, self.theta)
            gnn.steps()
            gnn.predict()
            self.testresult.append(gnn.predicty)
        np.savetxt("result.txt", self.testresult, delimiter="\n")

            


hp = HP(d=8, lr=0.0001, epoch=120, batchsize=100)

theta = THETA(hp)

sgd = SGD(theta)
sgd.train()

