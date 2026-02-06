# Check a number is prime or not

number = int(input("Please Enter your number: "))
isPrime = True

if number > 1 :
  for i in range(2, number) :
    if number % i == 0 :
      isPrime = False
      break

if isPrime == True  :
  print("your number",number,"is a prime number")
else:
  print("your number",number,"is not a prime number")   