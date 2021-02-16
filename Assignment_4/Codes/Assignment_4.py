#Importing Libaries
from itertools import product
import numpy as np
import matplotlib.pyplot as plt

#Function to calculate mean of number of head 
def mean_heads(n):
  count=0
  mean_value = 0
  omega = set(product(['H','T'], repeat = n))
  for i in range(n+1):
    count = len({om for om in omega if om.count('H') == i })
    mean_value = mean_value + (count/len(omega))*i
  return mean_value
  
  #Mean no of head for a fair coin thrice 
  
  print("The mean number of heads in three tosses for a fair coin is : ",mean_heads(3))
  
  #Extra : to plot average tosses for different number of tosses for a fair coin
  
coin_toss_set = []
mean_head_set = []
for i in range(1,11):
  mean_head_set.append(mean_heads(i))
  coin_toss_set.append(i)
  
 plt.plot(np.array(coin_toss_set),np.array(mean_head_set),'o:b')
plt.title("Mean number of heads in coin toss")
plt.xlabel("Number of coin toss")
plt.ylabel("Mean number of heads")
plt.grid()
plt.show()
