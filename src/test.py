import numpy as np
from theta import THETA
from hyperparameter import HP
from graph import GRAPH
from gnn import GNN

def test(hp, theta, graph, x, h):
    Graph = GRAPH(graph.shape[0], graph, -1)
    gnn = GNN(Graph, theta)
    gnn.x = x
    gnn.steps()
    gnn.predict()
    if (np.all(np.absolute(gnn.h - h) < 0.001)):
        return "success"
    else:
        return "fail"

if __name__ == '__main__':
    
    # (Fix dimention to 4, step to 2)
    # Test with three graphs with three x
    graph1 = np.array([[0,1,0,0], [1,0,1,1], [0,1,0,1], [0,1,1,0]])
    x1  = np.eye(4, 4)[np.arange(4)%4]
    graph2 = np.array([[0,1,1,1,1],[1,0,1,1,1], [1,1,0,1,1], [1,1,1,0,1], [1,1,1,1,0] ])
    x2 =  np.eye(5, 4)[np.arange(5)%4]
    graph3 = np.array([[0,1,0,0,0,1], [1,0,1,0,0,0], [0,1,0,1,1,0], [0,0,1,0,1,0], [0,0,1,1,0,1], [1,0,0,0,1,0]])
    x3 =  np.eye(6, 4)[np.arange(6)%4]

    # Fix parameter W
    weight = np.array([[0.1, -0.5, -0.6, 0.2], [0.3, 0.7, 0.4, 0.5], [0.4, -0.3, -0.2, -0.1], [0.1, 0.2, -0.3, -0.8]])

    # Expected values
    h1 = np.array([1.95, 0.77, 0.0, 1.37])
    h2 = np.array([2.2, 0.0, 0.0, 0.82])
    h3 = np.array([3.45, 1.38, 0.0, 1.94])

    hp = HP(d=4, step=2)
    theta = THETA(hp)
    theta.weight = weight

    # Three tests
    print("test1: {}".format(test(hp, theta, graph1, x1, h1)))
    print("test2: {}".format(test(hp, theta, graph2, x2, h2)))
    print("test3: {}".format(test(hp, theta, graph3, x3, h3)))
