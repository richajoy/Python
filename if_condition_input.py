string = input(" Enter a string: ")
length = len(string)

if length < 5:
    print("Length of the string is less that 5. ie, {}".format(length))
elif length == 5:
    print("Length of the string is equal to 5. ie, {}".format(length))
else:
    print("Length of the string is greater than 5. ie, {}".format(length))