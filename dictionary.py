def NumberList(ages):
    for i in ages:
        if i >= 1 and i <= 20:
            print(i)
        else:
            print("Number in the list {} is not between 1 and 20".format(i))


NumberList([2, 4, 8, 16, 32, 64])

