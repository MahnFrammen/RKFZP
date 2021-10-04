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
h=0.3 #Given values for ODE
x0=2
y0=1
xpoints=[x0] #array for storing X values
ypoints=[y0] #Array for storing Y values 

#State equations and define functions
def dy_dx(y,x):
    return -y + np.log(x) #Provided Equation
def RungeKuttaFehlberg(x,y):
    return -y + np.log(x)
#Calculates k1-k4, x and y solutions
def RKFAlg(x0,y0,h):
    k1 = RungeKuttaFehlberg(x0,y0)
    k2 = RungeKuttaFehlberg(x0+(h/2),y0+((h/2)*k1))
    k3 = RungeKuttaFehlberg(x0+(h/2),y0+((h/2)*k2))
    k4 = RungeKuttaFehlberg(x0+h,y0+(h*k3))
    y1 = y0+(h/6)*(k1+(2*k2)+(2*k3)+k4)
    x1 = x0+h
    x1 = round(x1,2)
    print("Point (x(n+1),y(n+1)) =",(x1,y1))
    return((x1,y1)) #Returns as ordered pair

#Define range for number of calculations
for i in range(2000):
    print(f"Y{i+1}".format(i)) #Solution value format
    x0,y0 = RKFAlg(x0,y0,h) #Calls RKF Function
    xpoints.append(x0) #Saves values into array
    ypoints.append(y0)
    y0 = 1
    ODEy1 = odeint(dy_dx,y0,xpoints)

#Runge-Kutta Graph
plt.plot(xpoints,ypoints,'b:',linewidth = 1) #command to plot lines using various colors and widths
plt.suptitle("RKF Graph")
plt.xlabel("x Points")
plt.ylabel("y Points")
plt.show()

#ODE graph
plt.plot(xpoints,ODEy1,'g-',linewidth=1)
plt.suptitle("ODE Graph")
plt.xlabel("x Points")
plt.ylabel("y Points")
plt.show()

#Function for plotting RKF and ODE graph
plt.plot(xpoints,ODEy1,'g-',linewidth=2,label="ODE")
plt.plot(xpoints,ypoints,'b:',linewidth=3,label="Runge-Kutta")
plt.suptitle("ODE and RKF Comparison")
plt.legend(bbox_to_anchor=(.8,1),loc=0,borderaxespad=0)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#Function for plotting the difference graph
diff = [] #array to store difference
for i in range(len(xpoints)):
    diff.append(ypoints[i]-ODEy1[i])
plt.plot(xpoints,diff)
plt.suptitle("Difference")
plt.xlabel("x Points")
plt.ylabel("RKF and ODE diff.")
plt.show()
