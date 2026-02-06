# Create a lamda function to compute the cube of a number
number = int(input("Please enter your number which you want to find cube:"))
cube = lambda num: num ** 3
print("Cube of", number,"is:",cube(number))