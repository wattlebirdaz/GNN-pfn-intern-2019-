import numpy as np
from graph import GRAPH
from gnn import GNN

class SGD:
    # batch size should be a divisor of the trainsize
    def __init__(self, theta):
        self.theta = theta
        self.trainloss = []    # average training set loss
        self.validloss = []    # average validation set loss
        self.trainacc = []     # average training set accuracy
        self.validacc = []     # average validation set accuracy
        self.testresult = []   # test result

    # validation set generator
    def validationset(self):
        self.pweights = np.ones(self.theta.hp.trainsize)
        self.validationmask = np.random.choice(self.theta.hp.trainsize, int(self.theta.hp.trainsize*self.theta.hp.vr), replace = False, p = self.pweights/np.sum(self.pweights))
        self.pweights[self.validationmask] = 0
        self.trainingmask = np.where(self.pweights == 1)[0]
        self.traindatapweights = np.copy(self.pweights) # Remember training set

    # batch mask generator
    def nextmaskgen(self):       
        self.batchmask = np.random.choice(self.theta.hp.trainsize, self.theta.hp.batchsize, replace=False, p = self.pweights/np.sum(self.pweights))
        self.pweights[self.batchmask] = 0 # selection probability weights


    def trainingsetstat(self):
        # training set
        # print(self.trainingmask)
        for i in self.trainingmask:
            self.adjacent = np.loadtxt(
                fname='datasets/train/{}_graph.txt'.format(i),
                skiprows=1
            )
            self.n = self.adjacent.shape[0]
            self.y = np.loadtxt('datasets/train/{}_label.txt'.format(i))
            
            graph = GRAPH(self.n, self.adjacent, self.y)
            if (self.theta.hp.mg == 1):
              graph.modifygraph()
              
            gnn = GNN(graph, self.theta)
            gnn.steps()
            gnn.predict()
            gnn.crossentropyloss()
            
            self.acctrainloss = self.acctrainloss + gnn.l
            self.acctrainacc += 1 if self.y == gnn.predicty else 0
                                
        self.trainacc.append(self.acctrainacc/(int(self.theta.hp.trainsize*(1-self.theta.hp.vr))))
        self.trainloss.append(self.acctrainloss/(int(self.theta.hp.trainsize*(1-self.theta.hp.vr))))

    def validationsetstat(self):
        # validation set
        # print(self.validationmask)
        for i in self.validationmask:
            self.adjacent = np.loadtxt(
                fname='datasets/train/{}_graph.txt'.format(i),
                skiprows=1
            )
            self.n = self.adjacent.shape[0]
            self.y = np.loadtxt('datasets/train/{}_label.txt'.format(i))
            
            graph = GRAPH(self.n, self.adjacent, self.y)
            if (self.theta.hp.mg == 1):
              graph.modifygraph()
              
            gnn = GNN(graph, self.theta)
            gnn.steps()
            gnn.predict()
            gnn.crossentropyloss()

            self.accvalidloss = self.accvalidloss + gnn.l
            self.accvalidacc += 1 if self.y == gnn.predicty else 0

        self.validacc.append(self.accvalidacc/(int(self.theta.hp.trainsize*self.theta.hp.vr)))
        self.validloss.append(self.accvalidloss/(int(self.theta.hp.trainsize*self.theta.hp.vr)))


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
            if (self.theta.hp.mg == 1):
              graph.modifygraph()
              
            gnn = GNN(graph, self.theta)
            gnn.gradientdescent()
      
        #update theta
        #SGD: self.theta.update()
        #MOMSGD: self.theta.momupdate()
        #ADAMSGD: self.theta.adamupdate()
        
        if (self.theta.hp.sgdtype == "normal sgd"):
            self.theta.update()
        elif (self.theta.hp.sgdtype == "momentum"):
            self.theta.momupdate()
        elif (self.theta.hp.sgdtype == "adam"):
            self.theta.adamupdate()
        
        self.trainingsetstat()
        self.validationsetstat()

    
    def train(self):
        # Create training & validation set
        self.validationset()

        # Loop the number of epochs
        for i in range(self.theta.hp.epoch):
            self.pweights = np.copy(self.traindatapweights) 

            # Loop the number of batch in one epoch
            for _ in range(int(self.theta.hp.trainsize*(1-self.theta.hp.vr)/self.theta.hp.batchsize)):
                # Create batch
                self.nextmaskgen()
                # Train the batch
                self.batchupdatetheta()
                
            print("{} epoch done".format(i+1))

    def gentestsetresult(self):
        for i in range(self.theta.hp.testsize):
            self.adjacent = np.loadtxt('datasets/test/{}_graph.txt'.format(i), skiprows=1)
            self.n = self.adjacent.shape[0]
            self.y = -1
            
            graph = GRAPH(self.n, self.adjacent, self.y)
            if (self.theta.hp.mg == 1):
                graph.modifygraph()
                
            gnn = GNN(graph, self.theta)
            gnn.steps()
            gnn.predict()
            
            self.testresult.append(gnn.predicty)
            
        np.savetxt("result.txt", self.testresult, delimiter="\n", fmt='%i')

