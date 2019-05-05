import numpy as np

class HP:        
    def __init__(self, step=None, d=None, lr=None, moment=None,moment2 = None, epsilon=None, epoch=None, trainsize=None, batchsize=None, validation_rate=None, testsize=None, sgdtype=None, modifygraph=None):
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
        
        self.sgdtype = sgdtype if sgdtype is not None else "normal sgd"
        self.mg = modifygraph if modifygraph is not None else 0

    def showparameters(self):
        print("Parameters:")
        print("	step: {}".format(self.step))
        print("	dimention: {}".format(self.d))
        print("	learning rate: {}".format(self.lr))
        print("	epsilon: {}".format(self.epsilon))
        print("	number of epochs {}". format(self.epoch))
        print("	training set size (including the validation set): {}".format(self.trainsize))
        print("	batch size: {}".format(self.batchsize))
        print("	test set size: {}".format(self.testsize))
        print("	validation rate: {}".format(self.vr))
        print("	sgd type: {}".format(self.sgdtype))
        if (self.sgdtype == "momentum"):
            print(" momentum: {}".format(self.beta))
        elif (self.sgdtype == "adam"):
            print(" beta1: {}".format(self.beta))
            print(" beta2: {}".format(self.beta2))
        print("	modify graph: {}".format(self.mg))

        
        

