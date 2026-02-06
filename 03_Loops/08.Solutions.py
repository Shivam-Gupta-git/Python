number = int(input("Please enter your number: "))

if number < 1 :
  print("Please enter a valid number !")
  exit()

fact = 1

while number > 0 :
  fact *= number
  number -= 1

print("factorial of",number,"is:",fact) 