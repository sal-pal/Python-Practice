"""
A simulation of the Monty Hall problem of probability. The first function
creates the simuulation, while MontyProb() iterates the simulation in order
to demonstrate how the probability of staying with the same door approaches
30% with N trials (Law of Large Numbers)
.
"""




from random import randrange


def MontyHall(choice1,choice2):
    """Enter 1, 2, or 3 for each parameter"""
    if type(choice1) and type(choice2) != type(1):
        return "Only ints can be used as arguments."
    else:
        pass
    prize = randrange(1,4)
    if choice1 and choice2 == prize:
        return 'Winner!'
    else:
        pass
    #elif choice2 == prize:     Uncomment this portion and delete else clause        
     #   return 'Winner!'       of line12 when wanting to use MontyHall without
    #else:                      MontyProb. If not uncommented, MontyProb returns 
     #   print 'Looser'         more than the desired number of output values.



def MontyProb(num_iter):
    one_if_win = []
    x = 0
    while x < num_iter:
        a = randrange(1,4)
        x += 1
        test = MontyHall(a,a)
        if test == 'Winner!':
            one_if_win.append(1)
            
        else:
            one_if_win.append(0)
    return "Probability of success when staying:", float(sum(one_if_win))/float(len(one_if_win))




