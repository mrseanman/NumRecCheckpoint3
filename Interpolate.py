class Interpolate(object):

    def __init__(self, data):
        self.data = data
        self.xVals = [item[0] for item in data]
        self.yVals = [item[1] for item in data]
        self.xMax = max(self.Xvals)
        self.xMin = min(self.xVals)

    def eval(self, x):

    def findxIndex(self, x):
        if (x > self.xMax):
            last
