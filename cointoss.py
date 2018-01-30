from random import randint

flips = 0

trials = 10

''' You will need to use a for loop for over the range of trials'''

for i in range(trials):
    first_flip = randint(0, 1)
    while randint(0, 1) == first_flip:
        flips += 1
print("flips done is {}".format(flips))
print(flips / trials + 2.0)


