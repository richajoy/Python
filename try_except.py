'''Try and except option'''
try:
    number = int("This is a number.")
except ValueError:
    print("There is a ValueError identified. Please fix it.")

''' Try and except with Error name specifications'''

def divide(number1, number2):
    try:
        print(number1/number2)
    except (TypeError, ValueError, NameError, ZeroDivisionError):
        print("Encountered a problem!")

divide(1, 0)

'''Error handling using the error codes'''
try:
    number = int(input("Enter an non-zero integer:"))
    print("10/{} = {}".format(number, 10.0/number))
except ValueError:
    print("You did not enter an integer.")
except ZeroDivisionError:
    print("You cannot enter 0.")

''' ValueError example exercise '''

while True:
    try:
        user_input = int(input("Enter an integer: "))
        print("Thanks for entering integer", user_input)
        break
    except ValueError:
        print("Try again")



