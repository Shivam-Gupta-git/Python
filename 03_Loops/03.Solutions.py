# print the multiplication table for a given number up to 10, but skip the 5th iteration. 

number = int(input("Please enter your number which you want to multiply it: "))

if number < 0 :
  print("Please enter a valid number !")
  exit()

multipliedNumber = 0

for i in range(1, 11) :
  if i == 5 :
    continue
  print(number, 'X', i, "=", i * number)  


