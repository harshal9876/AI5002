#Problem 1.8

#Importing Libraries
import math
from scipy import stats

#Defining Binomial Distribution
X = stats.binom(50, 0.01) # Declare X to be a binomial random variable

#Calculting respective probabilities
print("\n Probibility of at least once :",1-X.pmf(0))       # P(X >= 1)
print("\n Probibility of exactly equal to one :",X.pmf(1))  # P(X = 1)
print("\n Probibility of at least twice :",1-X.cdf(1))      # P(X >= 2)
