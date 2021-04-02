#Importing Libraries

from itertools import product 
import matplotlib.pyplot as plt
import random
import numpy as np

# Setting us required probablities of the events considering two events A and B

P_A = 0.3
P_B = 0.6
sample = 10

#Function to count a particular element in a string

def count(list,a):
  count_val = 0
  for i in range(len(list)):
    if list[i]== a:
      count_val = count_val + 1
  return count_val

#Creating sample distribution

def sample_distribution(sample,probability):
  list = []
  for i in range(sample):
    if i < sample*probability:
     list.append(1)
    else :
     list.append(0)
  return list

# Making th list of first event such that P(A) = 0.3

Event_A = sample_distribution(sample,P_A)
Event_B = sample_distribution(sample,P_B)
np.random.shuffle(Event_A)
np.random.shuffle(Event_B)
Event = list(product(Event_A,Event_B))

# Main

# P(A and B)

iterations = 100000
count_occourance = []
for i in range(iterations):
  count_occourance.append(count(Event[np.random.randint(sample*sample)],1))
occourance = count(count_occourance,2)
probability_A_and_B =  occourance/ iterations
print(" P(A and B)")
print('\n')
print("Theoratically the probability of A and B ie P(A and B)  = P(A)*P(B) = 0.3*0.6 = 0.18", )
print("Practically the probability of A and B ie P(A and B) :", probability_A_and_B)
print('\n')

#P(A and not B)

occourance = 0
for i in range(iterations):
  if Event_A[np.random.randint(sample)] == 1:
    occourance +=1
probability_A_and_not_B =  (occourance/ iterations) -  probability_A_and_B
print(" P(A and not B)")
print('\n')
print("Theoratically the probability of A and not B ie P(A and not B)  = P(A)-P(A and B) = 0.3 - 0.18 = 0.12", )
print("Practically the probability of A and not B ie P(A and not B) :", round(probability_A_and_not_B,4))
print('\n')

#P(A or B)

probability_A_or_B = P_A + P_B - probability_A_and_B
print(" P(A or B)")
print('\n')
print("Theoratically the probability of A or B ie P(A or B)  = P(A) + P(B) - P(A and B) = 0.3 + 0.6 - 0.18 = 0.72", )
print("Practically the probability of A or B ie P(A or B) :", round(probability_A_or_B,4))
print('\n')

#P(neither A nor B)

probability_neither_A_nor_B = 1 - probability_A_or_B
print(" P(neither A nor B)")
print('\n')
print("Theoratically the probability of neither A nor B ie P(A neither A nor B)  = 1 - P(A or B) = 1 - 0.18 = 0.28", )
print("Practically the probability of neither A nor B ie P( neither A nor B) :", round(probability_neither_A_nor_B,4))
print('\n')


#Plotting Variations in theoratical and practical outcome 

labels = ['P(A and B)', 'P(A and not B)', 'P(A or B)', 'P(neither A nor B)']
Theoratical = [0.18, 0.12, 0.72, 0.28 ]
Calculated = [probability_A_and_B, probability_A_and_not_B, probability_A_or_B, probability_neither_A_nor_B ]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Theoratical, width, label='Theoratical')
rects2 = ax.bar(x + width/2, Calculated, width, label='Practical')

ax.set_ylabel('Probability')
ax.set_title('Probman 6.15 : \n GIven P(A) = 0.3 , P(B) =0.6 \n A and B being independent events')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
