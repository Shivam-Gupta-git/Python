# 1. Numeric Data Types.......................
# i. Int............
# numbers = 12
# print(numbers)

# ii. Float..........
# numbers = 12.7
# print(numbers)

# iii. complex.......
# numbers = 3 + 4j
# print(numbers)

# 2. Sequence Data Types...........................
# i. String...........
# name = "python"
# print(name)

# Slicing......
# text = "shivam"
# print(text[0:3])

# Methods of String.................
# language = "python"
# print(language.lower())

# print(language.upper())

# print(language.capitalize())

# print(language.title())

# language = "p y t h o n"
# print(language.strip())


# String Containing...................

# name = "Python is a programming language"

# # print("Python" in name) // True
# # print("Java" in name) // False

# ii. List ............
# numbers = [1, 2, 3, 4]
# print(numbers) 

# print(numbers[0])  // 1
# print(numbers[-1])  // 4
# print(numbers[2]) // 3

# List Slicing......
# numbers = [1, 5, 9, 2, 7]

# print(numbers[0 : 2])  // [1, 5]
# print(numbers[1:4]) // [5, 9, 2]

# iii. Ttuple............
# students = ('saurav', 'raman', 'ravi', 'mohit', 'pawan')
# print(students)

# tange ..........
# r = range(1, 5)
# print(list(r)) // [1, 2, 3, 4]

# 3. Mapping Data Type :.......................

# student = {
#   "name" : "shivam",
#   "age" : 22,
#   "cource" : "python"
# }
# print(student)
# print(student["name"])

# 4. Set Data Types...................
# numbers = [1, 3, 4, 2, 6, 3]
# print(frozenset(numbers))

# Difference between == and is.....................
# x = 20
# y = 30

# print( x is y)

# Example of for loop..................................
# with list......
# numbers = [1, 3, 2, 5, 4, 7]
# for num in numbers:
#   print(num) # 1 3 2 5 4 7

# with range.......
# for num in range(0, 5):
#   print(num)  # 0, 1, 2, 3, 4 

# with string
# name = "pythin"
# for words in name:
#   print(words) # p y t h o n

# Example of while loop...................
num = 1
while num <= 5 :
  num += 1
  print(num)  # 2 3 4 5 6
