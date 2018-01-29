''' Find the average heads and tails with tails as 0 and heads as 1'''

from random import randint

heads = 0
tails = 0

for trails in range(0, 11):
    while randint(0, 1) == 0:
        tails = tails + 1
    heads = heads + 1

print("Total number of heads is {} and tails is {}".format(heads,tails))
print("heads/tails", heads/tails)

'''dice throw and random result'''

from random import randint

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

for throws in range(0, 10000):
    output = randint(1, 6)
    if output == 1:
        ones = ones + 1
    elif output == 2:
        twos = twos + 1
    elif output == 3:
        threes = threes + 1
    elif output == 4:
        fours = fours + 1
    elif output == 5:
        fives = fives + 1
    elif output == 6:
        sixes = sixes + 1

for avg in ones,twos,threes,fours,fives,sixes:
    print("average count for total {} is {}".format(avg, (avg/10000 * 100)))




