input_text = input("Enter some text: ")

for i in input_text:
    if i == 'a' :
        input_text = input_text.replace('a','4')
    elif i == 'b' :
        input_text = input_text.replace('b','8')
    elif i == 'e' :
        input_text = input_text.replace('e','3')
    elif i == 'l' :
        input_text = input_text.replace('l','1')
    elif i == 'o' :
        input_text = input_text.replace('o','0')
    elif i == 's':
        input_text = input_text.replace('s','5')
    elif i == 't':
        input_text = input_text.replace('t','7')
    else:
        pass

print(input_text)