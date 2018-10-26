from ChargeDistribution import ChargeDistribution
from NumIntegrate import NumIntegrate
from Interpolate import Interpolate

import matplotlib.pyplot as pl
import numpy as np


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
            integrate.plot("Euler integration of Charge Distribution")


        def RK4Integrate(self):
            delta = 0.1
            xRange = [-2., 2.]
            y0 = 0.

            integrate = NumIntegrate()
            chargeDistr = ChargeDistribution()

            integrate.RK4(chargeDistr.evaluate, delta, xRange, y0)
            integrate.plot("RK4 integration of Charge Distribution")

        def differenceBetweenMethods(self):
            delta = 0.01
            xRange = [-2., 2.]
            y0 = 0.

            integrateEuler = NumIntegrate()
            integrateRK4 = NumIntegrate()
            chargeDistr = ChargeDistribution()

            integrateEuler.euler(chargeDistr.evaluate, delta, xRange, y0)
            integrateRK4.RK4(chargeDistr.evaluate, delta, xRange, y0)

            fig = pl.figure()
            ax1 = fig.add_subplot(111)

            eulerX = [item[0] for item in integrateEuler.vals]
            eulerY = [item[1] for item in integrateEuler.vals]
            RK4X = [item[0] for item in integrateRK4.vals]
            RK4Y = [item[1] for item in integrateRK4.vals]

            ax1.scatter(eulerX, eulerY, s=10, c='b', marker=".", label='Euler')
            ax1.scatter(RK4X, RK4Y, s=10, c='r', marker=".", label='RK4')
            pl.legend(loc='upper left')
            pl.show()

            self.difference(integrateEuler, integrateRK4)

        def difference(self, integral1, integral2):
            differenceData = []
            xVals = []

            for i in range(len(integral1.vals)):
                xVals.append(integral1.vals[i][0])
                difference = integral2.vals[i][1] - integral1.vals[i][1]
                differenceData.append(difference)

            pl.scatter( xVals, differenceData, marker='.', s=10)
            pl.title("Values of (RK4 - Euler) integratin methods")
            pl.show()

        def testInterpolate(self):
            data = [[0,1],[1,0],[2,1],[3,0],[4,1],[5,0]]
            inter = Interpolate(data)
            xVals = np.linspace(-3., 7., num=1000)
            yVals = []
            for x in xVals:
                yVals.append(inter.eval(x))

            pl.plot(xVals, yVals)
            pl.show()
