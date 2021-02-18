import math
from scipy import stats

# Defining Binomial Distribution
# Declare X to be a binomial random variable
X = stats.binom(6, 1/6) 

#Calculting respective probabilities

print("\n Probability of throwing at most 2 sixes in 6 throws of a single die is :",X.cdf(2))      # P(X <= 2)
