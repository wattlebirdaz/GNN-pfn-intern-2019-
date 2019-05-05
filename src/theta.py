import numpy as np
import matplotlib.pyplot as plt

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

