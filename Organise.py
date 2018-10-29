from ChargeDistribution import ChargeDistribution
from NumIntegrate import NumIntegrate
from Interpolate import Interpolate

import matplotlib.pyplot as pl
import numpy as np
import copy

class Organise(object):

        #finds difference between integral2.vals[i][1] and
        #integral2.vals[i][1] for every i in integral2.vals
        def difference(self, integral1, integral2):
            interpolate1 = Interpolate(integral1.vals)
            differenceData = []

            for i in range(len(integral2.vals)):
                difference = integral2.vals[i][1] - interpolate1.eval(integral2.vals[i][0])
                differenceData.append([integral2.vals[i][0], difference])

            return differenceData

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


        def compare(self):
            delta = 0.2
            xRange = [-2., 2.]
            y0 = 0.

            chargeDistr = ChargeDistribution()

            integrateEuler = NumIntegrate()
            integrateRK4 = NumIntegrate()

            #evaluate E
            #-------------------------------------------------------------------
            integrateEuler.euler(chargeDistr.evaluate, delta, xRange, y0)
            integrateRK4.RK4(chargeDistr.evaluate, delta, xRange, y0)


            #plot both
            #-------------------------------------------------------------------
            eulerXVals = [item[0] for item in integrateEuler.vals]
            eulerYVals = [item[1] for item in integrateEuler.vals]

            RK4XVals = [item[0] for item in integrateRK4.vals]
            RK4YVals = [item[1] for item in integrateRK4.vals]

            fig = pl.figure()
            ax1 = fig.add_subplot(111)
            ax1.scatter(eulerXVals, eulerYVals, s=20, c='b', marker="+", label='Euler')
            ax1.scatter(RK4XVals, RK4YVals, s=20, c='r', marker="+", label='RK4')
            pl.legend(loc='upper left')
            pl.show()

            #plot difference
            #-------------------------------------------------------------------
            differenceData = self.difference(integrateEuler, integrateRK4)
            differenceXVals = [item[0] for item in differenceData]
            differenceYVals = [item[1] for item in differenceData]
            pl.scatter(differenceXVals, differenceYVals, s=20, marker="+")
            pl.title("Difference:   RK4 - Euler")
            pl.show()

            #find error
            #-------------------------------------------------------------------
            deltaRatio = 10000.

            integrateEulerTrueVals = NumIntegrate()
            integrateRK4TrueVals = NumIntegrate()
            integrateEulerTrueVals.euler(chargeDistr.evaluate, delta/deltaRatio, xRange, y0)
            integrateRK4TrueVals.RK4(chargeDistr.evaluate, delta/deltaRatio, xRange, y0)

            errEuler = self.difference(integrateEulerTrueVals, integrateEuler)
            errEulerXVals = [item[0] for item in errEuler]
            errEulerYVals = [item[1] for item in errEuler]

            errRK4 = self.difference(integrateRK4TrueVals, integrateRK4)
            errRK4XVals = [item[0] for item in errRK4]
            errRK4YVals = [item[1] for item in errRK4]

            #plot error
            #-------------------------------------------------------------------
            fig = pl.figure()
            ax1 = fig.add_subplot(111)
            ax1.scatter(errEulerXVals, errEulerYVals, s=20, c='b', marker="+", label='Euler Error')
            ax1.scatter(errRK4XVals, errRK4YVals, s=20, c='r', marker="+", label='RK4 Error')
            ax1.set_title("Difference between calculated values and 'true' values for Euler and RK4")
            pl.legend(loc='upper left')
            pl.show()

            #RK4 on separate axes
            #because error too small
            maxY = max(errRK4YVals)
            print("maximum rk4 error: " + str(maxY))
            margin = maxY/10.
            pl.title("RK4 Error")
            pl.ylim(-maxY - margin, maxY + margin)
            pl.scatter(errRK4XVals, errRK4YVals, marker='+')
            pl.show()

        def fieldThenVoltage(self):
            delta = 0.01
            xRange = [-2., 2.]
            y0Field = 0.
            y0Voltage = 0.

            integrateField = NumIntegrate()
            integrateVoltage = NumIntegrate()
            chargeDistr = ChargeDistribution()

            integrateField.RK4(chargeDistr.evaluate, delta, xRange, y0Field)
            integrateField.plot("Field")

            fieldData = copy.deepcopy(integrateField.vals)
            #putting in minus sign
            fieldX = [item[0] for item in fieldData]
            fieldY = [item[1] for item in fieldData]
            minusFieldY = [-item for item in fieldY]

            for i in range(len(fieldX)):
                fieldData.append( [fieldX[i], minusFieldY[i]] )

            #creates instance of interpolated field
            interpolatedField = Interpolate(fieldData)

            integrateVoltage.RK4(interpolatedField.eval, delta, xRange, y0Voltage)
            integrateVoltage.plot("Voltage")
