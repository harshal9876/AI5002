#Prob 2.6

#Including Libraries 
import numpy as np
import random
import matplotlib.pyplot as plt

#Defining functions

#Function to generate random set of product values for A/B/C marked as Normal or Defective
def production_set(percentage,size,true_value,false_value):
  value=[]
  i=0
  for i in range(size):
    if(i<(percentage/100)*size):
      value.append(false_value)
    else:
      value.append(true_value)
  random.shuffle(value)
  return value

#Function to count a particular element in a set  
def count(string,found):
  count_value=0
  i=0
  for i in range(len(string)):
    if string[i]==found:
      count_value = count_value + 1
  return count_value

#Function to generate a set of time duration of work of each employee
def job_time(time_A,time_B,time_C,time):
  time_series = []
  if ((time_A+time_B+time_C)==100):
    print("All workers covered")
    time_A = (time_A/100)*time
    time_B = (time_B/100)*time
    time_C = (time_C/100)*time
    for i in range(time):
      if i< time_A:
        time_series.append('A')
      if (time_A<=i) &(i<(time_B+time_A)):
        time_series.append('B')
      if i>= (time_A + time_B ):
        time_series.append('C')
    return time_series
  else :
    print("Error imput : all workers not covered")
  
#Function to calculate probability
def probability(sub_space_length,sample_space_length):
  return sub_space_length/sample_space_length

#Generating sample set
work_distribution = job_time(50,30,20,1000)
defective_A = production_set(1,1000,'N','A')
defective_B = production_set(5,1000,'N','B')
defective_C = production_set(7,1000,'N','C')

#Plotting work distribution
plt.hist(work_distribution,bins = 3,edgecolor='black')
plt.xlabel('Machine Operator') 
plt.ylabel('Tme spend on machine by operators') 
  
plt.title('Time spend by each operator in machine operation\n\n', 
          fontweight ="bold") 
  
plt.show() 

#P(A)
P_A = probability(count(work_distribution,'A'),len(work_distribution))

#P(B)
P_B = probability(count(work_distribution,'B'),len(work_distribution))

#P(C)
P_C = probability(count(work_distribution,'C'),len(work_distribution))

#P(D|A)
P_D_given_A = probability(count(defective_A,'A'),len(defective_A))

#P(D|B)
P_D_given_B =  probability(count(defective_B,'B'),len(defective_B))

#P(D|C)
P_D_given_C =  probability(count(defective_C,'C'),len(defective_C))

#P(A|D)
P_A_given_D = (P_A*P_D_given_A)/(P_A*P_D_given_A + P_B*P_D_given_B + P_C*P_D_given_C)

print("Probability that a defective item is produced and it is produced by A is : {0:.3f}".format(P_A_given_D))
