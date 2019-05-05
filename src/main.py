import matplotlib.pyplot as plt
import numpy as np
from theta import THETA
from hyperparameter import HP
from train import SGD

def tickfunction(ts, vr, bs, ep):
    newticklocation = np.arange(0, ts*(1-vr)*ep/bs, ts*(1-vr)/bs)
    newticklabels = [int(x/(ts*(1-vr)/bs)) for x in newticklocation]
    return newticklocation, newticklabels
            
if __name__ == '__main__':
    hp = HP(d=8, lr=0.0001, epoch=15, batchsize=100, sgdtype="normal sgd", modifygraph=0)
    theta = THETA(hp)
    sgd = SGD(theta)
    sgd.train()
    sgd.theta.hp.showparameters()

    newticklocation, newticklabels = tickfunction(hp.trainsize, hp.vr, hp.batchsize, hp.epoch)

    
    plt.subplot(2,1,1)
    plt.title("Average Loss of training and validation set ({})".format(sgd.theta.hp.sgdtype))
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.plot(sgd.trainloss, 'b-', label="training")
    plt.plot(sgd.validloss, 'r-', label="validation")
    plt.legend(loc='upper right')
    plt.xticks(newticklocation, newticklabels)


    plt.subplot(2,1,2)
    plt.title("Average accuracy of training and validation set ({})".format(sgd.theta.hp.sgdtype))
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.plot(sgd.trainacc, 'b-', label="training")
    plt.plot(sgd.validacc, 'r-', label="validation")
    plt.legend(loc='upper left')
    plt.xticks(newticklocation, newticklabels)

    plt.tight_layout()
    plt.show()

    # If you want to get the prediction for the test set
    sgd.gentestsetresult()



    
