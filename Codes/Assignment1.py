# Importing Libraries and fixing plots 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
%matplotlib inline  
# Change inline to notebook for a 3D interactive view 
plt.rcParams['figure.figsize'] = (7,5)
plt.rcParams['figure.dpi']=150
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax = fig.add_subplot(111,projection ='3d')
ax.set_title('Setting up variables')
ax.set_xlabel('random variable $X_1$')
ax.set_ylabel('Random vriable $X_2$')
ax.set_zlabel('$p_{X1,X2}(x1,x2)$')


# Generating random points
mean = 0
sigma = 1
x_1 = (np.random.rand(1000,1)-0.5)*8
x_2 = (np.random.rand(1000,1)-0.5)*8


# Function for single variable Gaussian distribution for random variable 'x' , Mean 'mean' and Standard deviation 'sigma' 

def normal_distribution(x,mean, sigma):
  normal_value = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mean)/sigma)**2)
  return normal_value

# Function for bivariable Gaussian distribution for random variable 'x_1' and 'x_2'
# Having respective mean - 'mean_1' and 'mean_2'
# Having respective standard deviation 'sigma_1' and 'sigma_2'
# having a covariance of matrix 'cov'

def multivar_gaussian_distribution(x_1, x_2, mean_1, mean_2, sigma_1, sigma_2 ,cov):
    ro = cov[0,1]/(sigma_1*sigma_2)
    dev_1 = x_1 - mean_1
    dev_2 = x_2 - mean_2
    z = (dev_1/sigma_1)**2+(dev_2/sigma_2)**2-((2*ro*dev_1*dev_2)/(sigma_1*sigma_2))
    result = (1/(2*np.pi*sigma_1*sigma_2*np.sqrt(1-ro**2)))*np.exp((-1*z)/(2*(1-ro**2)))
    return result
  
  
#Calculating normal distribution for single random variable
x_1_Normal_distribution = normal_distribution(x_1,mean,sigma)
x_2_Normal_distribution = normal_distribution(x_2,mean,sigma)
plt.plot(x_1_Normal_distribution,'ro')
plt.plot(x_2_Normal_distribution,'bo')
plt.xlabel('Number of samples')
plt.ylabel('Gaussian distribution of samples ')
plt.title('Variation of samples in the gaussian plane ')
plt.legend(["$ X1 \sim \mathcal{N}(0,\,1) $", "$ X2 \sim \mathcal{N}(0,\,1) $"], loc ="upper right") 
plt.show()


#Calculation of joint distribution
result=[]
for x in x_1_Normal_distribution:
  for y in x_2_Normal_distribution:
    result.append(x*y)
result = np.asarray(result)


# calculating covariance for random variables
concat_random_variable = np.concatenate((x_1,x_2),axis=1)
covariance__random_variable = np.cov(np.transpose(concat_random_variable),bias=True)
mean_1 = mean_2 = 0
sigma_1 = sigma_2 = 1


#Creating joint random variable distribution 
dist=[]
for i in x_1:
    for j in x_2:
        dist.append(multivar_gaussian_distribution(i,j,mean_1,mean_2,sigma_1,sigma_2,covariance__random_variable))
             
dist=np.asarray(dist)



#Calculating Joint PDF
fig=plt.figure()
ax=fig.add_subplot(111, projection = '3d')
ax.scatter(x_1,x_2, dist[0:1000],c=np.linalg.norm([x_1,x_2,dist[0:1000]],axis=0))
ax.set_xlabel('Random variable $X_1$')
ax.set_ylabel('Random vriable $X_2$')
ax.set_zlabel('$p_{X1,X2}(x1,x2)$')
ax.set_title('Variation of Joint distribution ')

fig=plt.figure()
ax=fig.add_subplot(111, projection = '3d')
ax.scatter(x_1,x_2,result[0:1000],c=np.linalg.norm([x_1,x_2,result[0:1000]],axis=0))
ax.set_xlabel('Random variable $X_1$')
ax.set_ylabel('Random vriable $X_2$')
ax.set_zlabel('$p_{X1}(x1)*p_{X2}(x2)$')
ax.set_title('Variation of Joint distribution ')

