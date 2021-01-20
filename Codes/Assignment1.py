# Importing Libraries
import numpy as np
import math 
from matplotlib import pyplot as plt

#Problem 6.2.1

#Taking input for random variables 

v = input(" Please input a value for V : ") 
v=float(v)
datax = np.linspace(-np.pi,np.pi,10000)
plot1 = plt.figure(1)
fx1 = np.sqrt(v)*np.sin(datax)
plt.plot(datax,fx1)
plt.grid()
plt.title('Variation if X1')
plt.xlabel('Range of x1')
plt.ylabel('$\sqrt{V}sin(x1)$')
plot2 = plt.figure(2)
fx1 = np.sqrt(v)*np.cos(datax)
plt.plot(datax,fx1)
plt.grid()
plt.title('Variation if X2')
plt.xlabel('Range of x2')
plt.ylabel('$\sqrt{V}cos(x2)$')
plot2 = plt.figure(2)

#Calculating Quantile function

datav=np.linspace(-np.sqrt(v),np.sqrt(v),1000)
plot3=plt.figure(3)
fx3=np.arcsin(datav/np.sqrt(v)) 
plt.plot(datav,fx3)
plt.title('Variation if a vs arcsin viz 2.1')
plt.xlabel('Range of a')
plt.ylabel('$arcsin\frac{a}{\sqrt{V}}$')
plt.grid()
plot4=plt.figure(4)
fx4=np.arccos(datav/np.sqrt(v))
plt.plot(datav,fx4)
plt.title('Variation if a vs arccos viz 2.2')
plt.xlabel('Range of a')
plt.ylabel('$arccos\frac{a}{\sqrt{V}}$')
plt.grid()

# Calculating PDF via Quantile function 

plot6=plt.figure(6)
fx1=(np.arcsin(datav)+math.pi/2)/math.pi
plt.plot(datav,fx1)
plt.title('Variation if CDF of F1(a) vs a')
plt.xlabel('Range of a')
plt.ylabel('F1(a)')
plt.grid()
plot5=plt.figure(5)
fx4=(-np.arccos(datav)+math.pi)/math.pi
plt.plot(datav,fx4)
plt.title('Variation if CDF of F2(a) vs a')
plt.xlabel('Range of a')
plt.ylabel('F2(a)')
plt.grid()

#Calculating Joint PDF

data=np.linspace(-1,1,1000)
plot7=plt.figure(7)
fx9=(1/(math.pi* np.sqrt(1-(data**2)/v))*(1/(math.pi* np.sqrt(1-(data**2))/v)))*(1/np.sqrt(v))
plt.plot(data,fx9)

plt.title('variation of joint PDF $p_{X1,X2}(x1,x2)$')
plt.xlabel('Range of variation of x1,x2')
plt.ylabel('$p_{X1,X2}(x1,x2)$')
plt.grid()

# Probman 6.2.2

# Taking inputs for V and theta

print("Finding the value of the jacobian at a point ")
v = input(" Give an input for V : ")
v=np.sqrt(float(v))
theta = input(' Give an input for theta')
s_theta = math.sin(float(theta))
c_theta = math.cos(float(theta))

#Calculating Jacobian Matrix

arr = np.array([[(c_theta/(2*v)), (s_theta/(2*v))], [-v*s_theta, v*c_theta]])
print("The Jacobian is ")
print(arr)
