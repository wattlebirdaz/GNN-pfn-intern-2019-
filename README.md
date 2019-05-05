# GNN
Implementation of Graph Neural Network for PFN internship assignment

## Usage
Put the `datasets/` and the `src/` in the same level of the directory.

Run it by
`python3 main.py`



## Parameters
You can set various parameters by modifying _line 13_ of the `src/main.py`.

() is the default value of the parameters

> step: step (2)
> d: dimention (8)
> lr: learning rate (0.0001)
> epsilon: epsilon ()
> epoch: number of epochs (10)
> trainsize: training set size including the validation set (2000)
> batchsize: batch size(100)
> testsize: test set size (500)
> validation_rate: validation rate (0.2)
> sgdtype: type of update. "normal sgd", "momentum", and "adam" are available. ("normal sgd")
> moment: momentum in momentum update, beta1 in adam update (0.9)
> moment2: beta2 in adam update (0.99)
> mg: modify graph. this is explained in the document. (0)
  

`hp = HP(d=8, lr=0.00015, epoch=2, batchsize=100, sgdtype="adam", modifygraph=0)`
This means that the dimention is 8, learning rate is 0.00015, number of epoch is 2, batch size is 100, update type is adam, and it does not allow graph modify option
