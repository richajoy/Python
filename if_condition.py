want_cake = "yes"
have_cake = "no"

if want_cake == "yes":
    print("We want cake...")
    if have_cake == "no":
        print("But we don't have any cake")
    elif have_cake == "yes":
        print("And it's our lucky day")
else:
    print("The cake is a lie")