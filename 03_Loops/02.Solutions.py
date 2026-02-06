number = int(input("Please enter your number: "))

if number < 0 :
  print("Please enter a valid number")
  exit()
  
evenNum = 0

for i in range(1, number+1) :
  if i % 2 == 0 :
    evenNum += i
print(evenNum)