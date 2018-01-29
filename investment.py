def invest(amount,rate,time):
    print("Principal amount: ${}".format(amount))
    print("Annual rate of return: ", rate)
    for i in range(1,time+1):
        gains = amount * rate
        amount = amount + gains
        print("year {}: ${}".format(i, amount))


invest(100, .05, 8)