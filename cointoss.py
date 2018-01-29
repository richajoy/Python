from random import randint

flips = 0

trials = 10000
heads = 0
tails = 0

''' You will need to use a for loop for over the range of trials'''

for i in range(flips, trials):
    trials_out = randint(0, 1)
    print(trials_out)
    while trials_out == 0:
        trials_out = randint(0, 1)
        print(trials_out)
        i = i + 1




''' For each trial , check the outcome of the first flip'''
