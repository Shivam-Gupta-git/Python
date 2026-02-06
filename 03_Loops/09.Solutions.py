# keep asking the user for input until they enter a number between 1 and 10

while True :
  number = int(input("Please enter your number between 1 to 10: "))
  if number < 1 or number > 10 :
    print("Invalid Number. try again")
  else :
    print("Thanks")
    break
