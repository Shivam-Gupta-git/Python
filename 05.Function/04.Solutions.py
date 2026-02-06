# write a function multiply that multiples two number, but can also accept and multiply string.

firstInput = int(input("Please enter your first number: "))
secondInput = input("Please enter your second value: ")

def multiply(a, b) :
  return a * b
print("your multiplication of",firstInput,"*",secondInput,"=",multiply(firstInput, secondInput))