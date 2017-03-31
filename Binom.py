"""Creates a function that runs binomial probabilities, then graphs the output"""

from math import *
import matplotlib.pyplot as plt


def BinomExp(n,x,p=.5,q=.5):
    """Finds the probablity of some random variable given a number of trials.
           -n is the total number of trials.
           -x is the number of sucesses.
           -p is the probability of x successful trials.
           -q is the proability of n-x unsuccessful trials. """
    
    if p+q != 1:
        print "p and q must be complementary probabilities. Enter probabilities that add up to 1."

    else:
        C = factorial(n) / (factorial(x) * factorial(n-x))
        P = p ** x
        Q = q ** (n-x)
        Total = C * P * Q
        return Total


def PoissProb(l,x):
	ans = (l**x)*(e**-l)/factorial(x)
	return ans



#Plot the change in the highest prob value in the BinomDist as a function of
#the number of trials
input_ = range(4,501)
output_ = []

for numb_trials in input_:
    sucess_list = range(1,(numb_trials+1))
    sub_list = []
    for sucess in sucess_list:
        sub_list.append(BinomExp(numb_trials,sucess))
    maxim_prob = max(sub_list)
    output_.append(maxim_prob)

plt.plot(input_,output_)
plt.show()


        













