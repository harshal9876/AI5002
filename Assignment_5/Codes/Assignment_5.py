#Importing libraries
import random
import numpy as np
import matplotlib.pyplot as plt 

#defining function count to count the occourance of a particular value in a list 
def count(list,a):
  count_val = 0
  for i in range(len(list)):
    if list[i]== a:
      count_val = count_val + 1
  return count_val

#generating samples
six_occourance = []
for i in range(100000):
  Six_throw = []
  for j in range(6):
    Six_throw.append(random.randint(1,6))  
  six_occourance.append(count(Six_throw,6))

  
 #plotting samples 
plt.hist(six_occourance,bins = 12 ,align = 'left')
plt.xlabel("Number of sixes in 6 throws of a die ")
plt.ylabel("Number of sixes appear")
plt.title("Occourance of sixes in 1,000,000 consecutive times in 6 throws of a fair die")
plt.show()

#Result
probability = (count(histo,1) + count(histo,2) + count(histo,0))/100000

print("The probability for throwing at most two sixes in 6 throws of a single die is : ", probability)
