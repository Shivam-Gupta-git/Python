# Reverse a string using a loop

input_str = str(input("Plese enter your string: "))
reverse_str = ""
for char in input_str :
  reverse_str = char + reverse_str
print("Your reverse string is:",reverse_str)