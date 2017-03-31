from math import *
from sys import path
path.append("C:\Users\Sal\Desktop\PythonPract")
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



def PoissFunct(ln,z):
    """ln is the number of input values minus one. z is the number of occurences. """
    x = range(ln)
    y = list()
    for i in x:
        y.append(PoissProb(i,z))
    plt.plot(x,y)
    plt.show()






