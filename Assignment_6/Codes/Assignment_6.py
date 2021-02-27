#Importing Libraries
from itertools import product 
import matplotlib.pyplot as plt
import random
import numpy as np

#geberating sample space
Cards = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
Decks = ['S','H','D','c']

Deck_of_cards = list(product(Cards,Decks))

#Function to count a particular element in a string
def count(list,a):
  count_val = 0
  for i in range(len(list)):
    if list[i]== a:
      count_val = count_val + 1
  return count_val

iter = 10000  #Number of iterations
occ_hist = []
for j in range(iter):
  Choosen_cards = []
  num = 0
  for i in range(2):
    Choosen_cards.append(Deck_of_cards[random.randint(0,55)])
    num =num+count(Choosen_cards[i],'A')
  occ_hist.append(num)

#Generating histogram
hist,bins = np.histogram(occ_hist,3)
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'r')
plt.hist(occ_hist, color = 'b',bins = 6 , align = 'left')
plt.legend(('CDF normalized','Histogram'), loc = 'upper right')
plt.xlabel("Number of aces")
plt.ylabel("Occourance of event")
plt.title("Plot of number of aces in two cards drawn from a deck")
plt.show()

#Calculating Expectation
expectation = 0
for i in range (3):
  expectation = expectation + (count(occ_hist,i)/iter)*i
print("The expectation of getting ace when two cards drawn at random is : ",expectation)
