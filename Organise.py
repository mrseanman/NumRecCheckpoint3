from ChargeDistribution import ChargeDistribution
from NumIntegrate import NumIntegrate
import matplotlib.pyplot as pl

class Organise(object):

        def quickPlot(self):
            ChargeDistr = ChargeDistribution()
            ChargeDiss.show()

        def eulerIntegrate(self):
            delta = 0.1
            xRange = [-2., 2.]
            y0 = 0.

            integrate = NumIntegrate()
            chargeDistr = ChargeDistribution()

            integrate.euler(chargeDistr.evaluate, delta, xRange, y0)

            xVals = [item[0] for item in integrate.vals]
            yVals = [item[1] for item in integrate.vals]

            self.plot(xVals, yVals)

        def RK4Integrate(self):
            delta = 0.1
            xRange = [-2., 2.]
            y0 = 0.

            integrate = NumIntegrate()
            chargeDistr = ChargeDistribution()

            integrate.RK4(chargeDistr.evaluate, delta, xRange, y0)

            xVals = [item[0] for item in integrate.vals]
            yVals = [item[1] for item in integrate.vals]

            self.plot(xVals, yVals)

        def plot(self, xVals, yVals):
            pl.plot(xVals, yVals)
            pl.show()
