# give a string, and find non-repeated character

input_str = str(input("Please enter your string: ")).lower()

nonRepeatedStr = ""

for char in input_str :
    if input_str.count(char) == 1 :
        nonRepeatedStr += char
print("your non-repeated character is: ",nonRepeatedStr)