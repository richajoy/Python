user_input = int(input("Enter a positive integer: "))

for i in range(1, user_input + 1):
    factor = user_input % i
    if factor:
        continue
    else:
        print("{} is a divisor of {}".format(i,user_input))





