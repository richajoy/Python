def celsius(temp_cel):
    fahrenheit = float(temp_cel * 9/5 + 32)
    return fahrenheit

def fahrenheit(temp_fah):
    celsius = float((temp_fah - 32) * 5/9)
    return celsius


temp_cel = 40
temp_fah = 65

fah_re = celsius(temp_cel)
cel_se = fahrenheit(temp_fah)

print("{} degrees C = {} degrees F".format(temp_cel,fah_re))
print("{} degrees F = {} degrees C".format(temp_fah,cel_se))
