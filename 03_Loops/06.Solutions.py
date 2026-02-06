# give a string, and find first non-repeated character

Input_str = str(input("Please Enter your string: ")).lower()

for char in Input_str :
  if Input_str.count(char) == 1 :
    print(char)
    break
