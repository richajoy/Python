for i in range(0, 4):
    if i == 2:
        break
    print(i)
print("Finished with i =", str(i))

for i in range(0, 5):
    if i == 2:
        continue
    print(i)
print("Finished with i =",str(i))

phrase = " There is no capital x in this word"

for letter in phrase:
    if letter == "X":
        print("There is X found in this phrase.")
        break
else:
    print("There is no X in this phrase.")

'''Code to enter the maximum password retries.'''

tries = 0

while tries < 3:
    password = input("Enter password: ")
    if password == "Jesusl0vea!!":
        break
    else:
        tries = tries + 1
else:
    print("Incorrect password, maximum tries exceeded.")


''' example for break operation '''


while True:
    input_word = input("Enter q or Q: ")
    if input_word == "q" or input_word == "Q":
        print("You entered correct alphabet.")
        break
    else:
        print("Enter the correct phrase!")
        continue

''' multiplies of 3 for numbers from 1 through 50'''

for number in range(1, 51):
    if number % 3:
        print(number)
        continue



