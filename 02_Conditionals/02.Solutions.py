# Movie tickets Prices are based on age: $12 for adult (18 and over), 8$ for children and everyone get a $2 discount on wednessday.

userAge = int(input("Please Enter your age: "))
day = "Wednesday"

price = 12 if userAge >= 18 else 8

if day == 'Wednesday' : price -= 2
print("Ticket price for you is $", price)