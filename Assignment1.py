#!/usr/bin/env python
# coding: utf-8

# # Probman 6.2.1
# Evaluate the joint PDF of X1, X2, given by
# _$$p_{X1,X2}(x1,x2)=p_{X1}(x1)p_{X2}(x2)$$_
# Given
# $$X1 = \sqrt{V}cos(x1)$$ 
# $$X2 = \sqrt{V}sin(x2)$$ 
# Probability Density Function, f(x), completely describes the probability that a Random Variable, X, assumes a value in a given range of possible values.
# Mathematically, the probability that random variable X, assumes a value that lies in the interval [a,b].
# $$p(a<x<b)=\int_{a}^bf(x)\,dx$$
# and CDF of a function is defined as 
# $$p(x<a)=F(a)=\int_{-\inf}^af(x)\,dx$$
# which is equal to the area under the PDF till a , converself it could be stated
# $$f(x)=\frac{d(F(a))}{dx}................(1)$$
# **For solving the problem we'll choose a particular value of V**

# In[1]:


import numpy as np
import math 
from matplotlib import pyplot as plt
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


# Both the random variable can attain the value in between [-1,1], thus 
# $$p( X1 \leq a ) = p( \sqrt{V}sin(x1) \leq a ) = p( x1 \leq arcsin(\frac{a}{\sqrt{V}}) ).....................(2.1)$$
# $$p( X2 \leq a ) = p( \sqrt{V}cos(x2) \leq a ) = p( x2 \leq arccos(\frac{a}{\sqrt{V}}) ).....................(2.2)$$
# $$where -\sqrt V \leq a \leq \sqrt V $$
# The plots of 2.1 and 2.2 comes out to be 

# In[2]:


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


# **Using the properties of CDF and Quantile function** 2.1 and 2.2 can be written as
# $$p(x1<a) = F1(a)=\frac{arcsin(\frac{a}{\sqrt{V}})+\pi/2}{\pi}...................( 3.1 )$$
# and 
# $$p(x2<a) = F2(a)=\frac{-arccos(\frac{a}{\sqrt{V}})+\pi}{\pi}....................( 3.2 )$$
# The respective CDF now would be 

# In[3]:


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


# Now as the Joint PDF is constrained under a limit of [0,1] following the properties of CDF 
# From (1) taking the derivative of the resulted CDF to calculate the PDF 3.1 and 3.2 becomes 
# $$p_{X1} = \frac{1}{\pi\sqrt{1-\frac{a^{2}}{V}}}*\frac{1}{\sqrt{V}}$$
# $$p_{X2} = \frac{1}{\pi\sqrt{1-\frac{a^{2}}{V}}}*\frac{1}{\sqrt{V}}$$
# The joint PDF would be 
# 

# In[4]:


data=np.linspace(-1,1,1000)
plot7=plt.figure(7)
fx9=(1/(math.pi* np.sqrt(1-(data**2)/v))*(1/(math.pi* np.sqrt(1-(data**2))/v)))*(1/np.sqrt(v))
plt.plot(data,fx9)

plt.title('variation of joint PDF $p_{X1,X2}(x1,x2)$')
plt.xlabel('Range of variation of x1,x2')
plt.ylabel('$p_{X1,X2}(x1,x2)$')
plt.grid()


# # Probman 6.2.2
# Let
# 
# $$X1 = \sqrt{V}cos\theta$$ 
# $$X2 = \sqrt{V}sin\theta$$ 
# 
# Evaluate the Jacobian 
#  $$J=\begin{vmatrix}
# \frac{\partial X1}{\partial V} & \frac{\partial X2}{\partial V} \\
# \frac{\partial X1}{\partial \theta} & \frac{\partial X2}{\partial \theta}
# \end{vmatrix}$$
# 
# Using partial derivitive
# 
# $$\frac{\partial X1}{\partial V} =\frac{1}{2\sqrt{V}}cos\theta$$
# $$\frac{\partial X2}{\partial V} =\frac{1}{2\sqrt{V}}sin\theta$$
# $$\frac{\partial X1}{\partial \theta}=-\sqrt{V}sin\theta$$
# $$\frac{\partial X2}{\partial \theta}=\sqrt{V}cos\theta$$
# 
# Substituting 
# $$J=\begin{vmatrix}
# \frac{1}{2\sqrt{V}}cos\theta & \frac{1}{2\sqrt{V}}sin\theta \\
# -\sqrt{V}sin\theta & \sqrt{V}cos\theta
# \end{vmatrix}$$

# In[5]:


print("Finding the value of the jacobian at a point ")
v = input(" Give an input for V : ")
v=np.sqrt(float(v))
theta = input(' Give an input for theta')
s_theta = math.sin(float(theta))
c_theta = math.cos(float(theta))
arr = np.array([[(c_theta/(2*v)), (s_theta/(2*v))], [-v*s_theta, v*c_theta]])
print("The Jacobian is ")
print(arr)


# In[ ]:




