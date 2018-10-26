'''
linearly interpolates data
'''

class Interpolate(object):

    def __init__(self, data):
        self.data = data
        self.xVals = [item[0] for item in data]
        self.yVals = [item[1] for item in data]
        self.xMax = max(self.xVals)
        self.xMin = min(self.xVals)

    def eval(self, x):
        if x > self.xMax:
            lastDiff = (self.yVals[-1]-self.yVals[-2]) / (self.xVals[-1]-self.xVals[-2])
            y = lastDiff * (x - self.xMax) + self.yVals[-1]
        elif x < self.xMin:
            firstDiff = (self.yVals[1]-self.yVals[0]) / (self.xVals[1]-self.xVals[0])
            y = firstDiff * (x - self.xMin) + self.yVals[0]
        else:
            index = self.findIndex(x)
            diff = (self.yVals[index+1]-self.yVals[index]) / (self.xVals[index+1]-self.xVals[index])
            y = diff*(x-self.xVals[index]) + self.yVals[index]

        return y

    #returns last index i where xVals[i] < x
    def findIndex(self, x):
        i = 0
        while self.xVals[i] < x:
            i += 1
        return i-1
