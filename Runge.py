#Zach Pedersen, Rylan Casanova
#This is our work!
#Prof Citro
#2 October 2022

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
import math

#Our initial values
x0 = 1
y0 = 5
h = 0.02
r = 2000

#List that holds our x's and y's from rkf
xlist = [x0]
ylist = [y0]

#Our ODE
def dydx(y, x):
    return y/(math.e**x-1)

#Computes y's using Runge-Kutta
def rkf(y, x):
    k1 = dydx(y, x)
    k2 = dydx((y + h*k1/2), (x + h/2))
    k3 = dydx((y + h*k2/2), (x + h/2))
    k4 = dydx((y + h*k3), (x + h))
    return y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

#Sets variables that we will change when making our lists
x = x0
y = y0
#Records start time (Runge-Kutta)
start = time.time()
    
#Calculates 2000 x's and y's and adds them to lists
for i in range(r):
    x += h
    xlist.append(x)
    y = rkf(y, x)
    ylist.append(y)
    
#Calculates time for RKF
t = time.time() - start
print("Runge-Kutta operation took ", t, " seconds.")


#Plot results (Runge-Kutta)
plt.title('Runge-Kutta Method')
plt.plot(xlist,ylist)
plt.xlabel('x rkf')
plt.ylabel('y rkf')
plt.show()

#Records start time (Odeint)
start = time.time()
#Time points
xodeint = np.linspace(1, 41, 2000)

#Solve ODE
yodeint = odeint(dydx, y0, xodeint)
#Calculates time for odeint
t = time.time() - start
print("Odeint operation took ", t, " seconds.")

#Plot results (Odeint)
plt.title("Odeint Method")
plt.plot(xodeint, yodeint)
plt.xlabel('x odeint')
plt.ylabel('y odeint')
plt.show()

#Let's you search the lists for x's and y's (Runge-Kutta)
prompt = "Enter an integer 0 - {}\n".format(r)
while (1):
    index = input(prompt)
    print("x", index, " = ", xlist[int(index)], " y", index, " = ", ylist[int(index)])
