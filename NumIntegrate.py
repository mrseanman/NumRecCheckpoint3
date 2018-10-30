'''
Class describes methods for numerically integrating
1st order ODEs including:
Euler Method & RK4
'''

import numpy as np
import matplotlib.pyplot as pl

class NumIntegrate(object):

    #fills vals with [x,y] values
    #of integral of func using euler method
    def euler(self, func, delta, xRange, y0):
        numIter = int(np.floor((xRange[1] - xRange[0]) / delta))

        params = [xRange[0], y0]

        currX = params[0]
        currY = params[1]

        self.vals = []
        for i in range(numIter):
            self.vals.append(params)
            diff = func(params)
            currY += diff * delta
            currX += delta
            params = [currX, currY]

    #fills vals with [x,y] values
    #of integral of func using RK4 method
    def RK4(self, func, delta, xRange, y0):
        numIter = int(np.floor((xRange[1] - xRange[0]) / delta))

        params = [xRange[0], y0]

        currX = params[0]
        currY = params[1]

        self.vals= []
        for i in range(numIter):
            self.vals.append(params)

            k1 = func(params)
            k2 = func([ (params[0] + delta/2.) , (params[1] + delta*k1/2.) ])
            k3 = func([ (params[0] + delta/2.) , (params[1] + delta*k2/2.) ])
            k4 = func([ (params[0] + delta   ) , (params[1] + delta*k3   ) ])

            currX += delta
            currY += delta*(k1/6. + k2/3. + k3/3. + k4/6.)
            params = [currX, currY]



    def plot(self, title, labels):
        xVals = [item[0] for item in self.vals]
        yVals = [item[1] for item in self.vals]
        pl.plot(xVals, yVals)
        pl.title(title)
        pl.xlabel(labels[0])
        pl.ylabel(labels[1])
        pl.show()
