def square(number):
    sqr_num = int(number) ** 2
    return sqr_num

input_num = input("Please enter the base number: ")
output_num = square(input_num)

print("The square of {} is {}".format(input_num,output_num))