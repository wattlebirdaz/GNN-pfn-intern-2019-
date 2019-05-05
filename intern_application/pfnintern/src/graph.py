import numpy as np

class GRAPH:
    def __init__(self, n, adjacent, y):
        self.n = n
        self.adjacent = adjacent
        self.y = y

    def modifygraph(self):
        self.n = self.n + 1
        self.adjacent = np.insert(self.adjacent, 0, 1, axis=1)
        self.adjacent = np.insert(self.adjacent, 0, 1, axis=0)
        self.adjacent[0][0] = 0
