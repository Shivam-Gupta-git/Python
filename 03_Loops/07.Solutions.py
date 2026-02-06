# find the factorial of given number  
number = int(input("Please enter your number: "))

if number < 1 :
  print("Please enter a valid number")
  exit()

fact = 1
for i in range(1, number + 1): 
  fact *= i
print("factorial of",number,"is:",fact)   