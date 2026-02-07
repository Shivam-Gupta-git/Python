numbers = int(input("Please enter your number: "))

def findEven(num):
    for i in range(2, num + 1, 2):
        yield i

for even in findEven(numbers):
    print(even)