#Importing Libraries

from itertools import product 
import matplotlib.pyplot as plt
import random
import numpy as np

#defining the imput list and sum number

A = [2,3,4,5]
B = [11,12,13,14,15]
sum_of_numbers = 16

#Printing the defination list and sum 

print("Set A : ",A)
print("Set B : ",B)
print("The sum of numbers to be equal to : ", sum_of_numbers)

#Creating a list of possible outcomes

numbers_choosen = list(product(A,B))

#Function to count a particular element in a string

def count(list,a):
  count_val = 0
  for i in range(len(list)):
    if list[i]== a:
      count_val = count_val + 1
  return count_val

#number of times the loop will follow
iterations = 100000

#Main

sum =[]
for i in range(iterations):
  sum.append(list(numbers_choosen[random.randint(0,len(numbers_choosen)-1)])[1] +list(numbers_choosen[random.randint(0,len(numbers_choosen)-1)])[0])

#Calculationg probability
probability = count(sum,sum_of_numbers)/iterations
print('\n The probability of having the sum of numbers to be equal to 16 is : ',round(probability,4))

#Plotting Variations in theoratical and practical outcome 

labels = ['Sum =16']
Theoratical = [0.2 ]
Calculated = [probability ]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Theoratical, width, label='Theoratical')
rects2 = ax.bar(x + width/2, Calculated, width, label='Practical')

ax.set_ylabel('Probability')
ax.set_title('GATE 7 : \n GIven A = [2,3,4,5] and B = [11,12,13,14,15] \n Result : Sum of two numbers choosen at random is equal to 16 ')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
