#Zach Pedersen
#This is my work!
#CST-305
#Prof. Citro

#Import correct libraries and extensions
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import warnings
def fxn():
    warnings.warn("deprecated", DeprecationWarning)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

#Define conditions and store values
h = 0.3 #Given values for ODE
x0 = 2
y0 = 1
xpoints = [x0]
ypoints = [y0]

#State equations and define functions
def ODEmodel(y,x):
    return -y + np.log(x)
def RKmodel(x,y):
    return -y + np.log(x)
#Calculates k1-k4, x and y values
def RungeKuttaAlgorithm(x0,y0,h):
    k1 = RKmodel(x0,y0)
    k2 = RKmodel(x0+(h/2),y0+((h/2)*k1))
    k3 = RKmodel(x0+(h/2),y0+((h/2)*k2))
    k4 = RKmodel(x0+h,y0+(h*k3))
    y1 = y0+(h/6)*(k1+(2*k2)+(2*k3)+k4)
    x1 = x0+h
    x1 = round(x1,2)
    print("Point (x(n+1),y(n+1)) =",(x1,y1))
    return((x1,y1))

#Define range for number of calculations
for i in range(2000):
    print(f"Y{i+1}".format(i)) #Solution value format
    x0,y0 = RungeKuttaAlgorithm(x0,y0,h) #Calls RKF Function
    xpoints.append(x0)
    ypoints.append(y0)
    y0 = 1
    ODEy1 = odeint(ODEmodel,y0,xpoints)

#Function for plotting Runge-Kutta Graph
plt.plot(xpoints,ypoints,'r:',linewidth=1)
plt.suptitle("Runge-Kutta Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#Function for plotting ODE graph
plt.plot(xpoints,ODEy1,'g-',linewidth=1)
plt.suptitle("ODE Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#Function for plotting RKF and ODE graph
plt.plot(xpoints,ODEy1,'g-',linewidth=2,label="ODE")
plt.plot(xpoints,ypoints,'r:',linewidth=3,label="Runge-Kutta")
plt.suptitle("Comparing the two")
plt.legend(bbox_to_anchor=(.8,1),loc=0,borderaxespad=0)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#Function for plotting the difference graph
diff = []
for i in range(len(xpoints)):
    diff.append(ypoints[i]-ODEy1[i])
plt.plot(xpoints,diff)
plt.suptitle("Difference")
plt.xlabel("x Points")
plt.ylabel("RKF and ODE diff.")
plt.show()
