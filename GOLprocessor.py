import numpy as np
from scipy.ndimage.filters import convolve
neighbourconvolver = np.array(((1,1,1), (1,0,1),(1,1,1)))

def makeAshoot(size):
    arr = np.zeros((size,size), dtype=bool)
    i = int(size/2)-1
    arr[i:i+3,i:i+3] = np.array(((1,1,1),(0,0,1),(0,1,0)), dtype=bool)
    return arr

def centeredsoup(size):
    return (np.exp(-5 * ((np.mgrid[:size, :size][0] / size - 0.5) ** 2 + (np.mgrid[:size, :size][1] / size - 0.5) ** 2)) * np.random.random((size,size))) > 0.7

class GameOfLife:
    def __init__(self, size = (100,100)):
        self.size  = np.array(size)
        self.value = np.zeros(size, dtype=bool)
        self.bornlastgen = np.zeros(size, dtype=bool)
        self.deadlastgen = np.zeros(size, dtype=bool)
        self.neighbours = np.zeros(size, dtype=bool)
    def setarr(self, arr):
        self.value = arr.astype(bool)
    def getarr(self):
        return self.value
    def getsize(self):
        return self.size
    def tick(self):
        self.neighbours = convolve(self.value.astype(int), neighbourconvolver, mode ='wrap')
        self.bornlastgen = np.logical_and(np.logical_not(self.value), (self.neighbours ==3))
        self.deadlastgen = np.logical_and(self.value, np.logical_or(self.neighbours <2, self.neighbours>3))
        self.value[self.bornlastgen] = True
        self.value[self.deadlastgen] = False
        return

    def symetrize(self):
        self.value = np.logical_or(self.value, self.value.T)
        