<!-- # shivamgupta@Shivams-MacBook-Air Python % ls
# 01_Basic
# shivamgupta@Shivams-MacBook-Air Python % cd 01_Basic
# shivamgupta@Shivams-MacBook-Air 01_Basic % python3
# Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.

# >>> import os
# >>> os.sys()

# Traceback (most recent call last):
#   File "<python-input-1>", line 1, in <module>
#     os.sys()
#     ~~~~~~^^
# TypeError: 'module' object is not callable
# >>> os.sys()
# Traceback (most recent call last):
#   File "<python-input-2>", line 1, in <module>
#     os.sys()
#     ~~~~~~^^
# TypeError: 'module' object is not callable

# >>> import sys
# >>> sys.platform
# 'darwin'

# >>> import hello_chai
# chai or code
# lemon tea
# >>> hello_chai.chai("mint chai")
# mint chai


# >>> from importlib import reload
# >>> reload(hello_chai)
# chai or code
# lemon tea
# <module 'hello_chai' from '/Users/shivamgupta/Desktop/Python/01_Basic/hello_chai.py'>
# >>> hello_chai.chai_one
# 'lemon tea'
# >>> hello_chai.chai_two
# 'green tea'
# >>> hello_chai.chai_three
# 'masala tea'
 -->


# Object Type / Data Type 

- Number : 1234, 3.2123, 3+4j, 0b111, Decimal(), Fraction()

- Srtings : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'

- List : [1, 2, 3], [1, 2, 3, ['a', 'b', 'c']], [1, 2, ['a', 'b'], list(range(10))];

- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple

- Dictionary : {'food' : 'spam', 'tasty' : 'yum',}, dict(hours = 10) 

- Set : set('abc'), set{'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'c:\ham.bin', 'wb')

- Boolean : True, False

- None : None

- Function, modules, classes

- Advance : Decorators, Generators, Iteratore, MetaProgarmming, Comprehensions, Context Managers

# Depth in number data type 
-
- random method in python
- import random after that just call it 

random.random()
> 0.08514996672388664 // output

random.randint(1, 10)
> 1 // output

random.randint(1, 10)
> 8 // output

- random.choice() is used to return a random element from a given list (or any sequence). Each time you call it, it may return a different element from the array.

- Example :
l1 = ['lemon tea', 'masala tea', 'ginger tea', 'mint tea']

random.choice(l1)

> 'mint tea' // output 

random.choice(l1)

> 'lemon tea' //output

- random.shuffle() : It changes the order of elements in the same list every time it is called.

Example: 
l1 = ['lemon tea', 'masala tea', 'ginger tea', 'mint tea']

> random.shuffle(l1) // call

l1 // call

> ['masala tea', 'ginger tea', 'lemon tea', 'mint tea'] // output

random.shuffle(l1) // call

l1 // call

> ['lemon tea', 'masala tea', 'ginger tea', 'mint tea']

- from decimal 

import Decimal : from decimal import Decimal is used to perform high-precision decimal arithmetic in Python. Floating-point numbers (float) can give inaccurate results due to binary representation.

Example (problem with float)

> print(0.1 + 0.2)

> 0.30000000000000004 // output

- Using Decimal

from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')

print(a + b)

> 0.3 // output

# Set Data Type
-

setone = {1, 2, 3, 4}

- setone & {1, 3} // find intersection 

> {1, 3} // output because both are common

- setone | {4, 5} // find union

> {1, 2, 3, 4, 5} // output

# String in python
-
chai = 'Masala Chai'

- find firsh character of given string

first_char = chai[0]

> print(first_char) // output is M

Slicing :
-
Slicing is used to extract a part of a sequence (string, list, tuple, etc.).

=> Syntax
sequence[start : end : step]
- start → starting index (inclusive)

- end → ending index (exclusive)

- step → gap between elements

=> Example : 
text = “Python"

> print(text[0:4])   // Pyth

> print(text[1:5])   // ytho

> print(text[:3])    // Pyt

> print(text[2:])    // thon

> print(text[0:6:2]) // Pto 

> print(text[::-1])  // nohtyP | and it is also usse to Reverse a String using Slicing 

Common String Methods :
-
Example : chai = 'lemon tea'

> print(chai.lower()) // lemon tea

> print(chai.upper()) // LEMON TEA

> print(chai.capitalize()) // Lemon tea

> print(chai.replace('lemon', 'ginger')) // ginger tea

> print(len(chai)) // 9

Example : chai1 = "lemon chai, masala chai, ment chai, ginger chai"

> print(chai1.split(", ")) // ['lemon chai', 'masala chai', 'ment chai', 'ginger chai']

> print(chai1.find('ment chai')) // 25

> print(chai1.count('chai')) // 4

=> note:  {} this is called placeholder and it is used to add variables inside.

Example : 
> chai_type = 'Masala'

> quantity = 2

> order = "I ordered {} cups of {} chai"

> print(order.format(quantity, chai_type)) // 
I ordered 2 cups of Masala chai

- join() : join() method is used to convert List into Sreing

Example: 

chai_type = ["masala chai", "ginger chai", "mint chai", "lemon chai", "green chai"]

> print(", ".join(chai_type)) // masala chai, ginger chai, mint chai, lemon chai, green chai

String Containing......
-
 string containing usually means checking whether a string contains a specific character or substring.

Example:  text = "Python programming"

> print("Python" in text)     # True

> print("Java" in text)       # False

# List 

- A list is a built-in data type in Python used to store multiple values in a single variable.

- decleration of list

students = ['shubham', 'mohan', 'sohan', 'saurav']

> print(students) // ['shubham', 'mohan', 'sohan', 'saurav']

List Slicing.......
-
students = ['shubham', 'mohan', 'sohan', 'saurav']

> print(students[:2]) // ['shubham', 'mohan']

> print(students[1:-1]) // ['mohan', 'sohan']

> print(students[1:4]) // ['mohan', 'sohan', 'saurav']

> print(students[::-1]) // ['saurav', 'sohan', 'mohan', 'shubham']

> print(students[-1]) // saurav

> print(students[::2]) // ['shubham', 'sohan']

=> List is Mutable 

Example: 
students = ['shubham', 'mohan', 'sohan', 'saurav']
> students[0] = 'Vikash' 
print(students) // ['Vikash', 'mohan', 'sohan', 'saurav']

=> Exchange Element into the give list

Example : students = ['shubham', 'mohan', 'sohan', 'saurav']

students[1:2] = ['nitin'] 

> print(students) // ['shubham', 'nitin', 'sohan', 'saurav']

students[1:3] = ['sonu', 'ravi']

> print(students) // ['shubham', 'sonu', 'ravi', 'saurav']

=> add element into to the given list

Example: students = ['shubham', 'mohan', 'sohan', 'saurav']

students[1:1]

students[1:1] = ['Ravi', 'anish']

> print(students) // ['shubham', 'Ravi', 'anish', 'mohan', 'sohan', 'saurav']

=> How to remove element into the give list

Example : students = ['shubham', 'Ravi', 'anish', 'mohan', 'sohan', 'saurav']

students[1:3] = []

> print(students) // ['shubham', 'mohan', 'sohan', 'saurav']

# Basic Loops in Python

students = ['anish', 'saurav', 'aryan', 'om']

for student in students:
> print(student) // anish saurav aryan om

for student in students:
> print(student, end'-') // anish-saurav-aryan-om-

if 'shubham' in students:
> print('shubham is all ready in list') // nothing

List Methods.........
-
students = ['anish', 'saurav', 'aryan', 'om']

- students.append('shubham')
> print(students) // ['anish', 'saurav', 'aryan', 'om', 'shubham']

- students.insert(2, 'rohan')
> print(students) // ['anish', 'saurav', 'rohan', 'aryan', 'om', 'shubham']

- numbers.remove(20)
> print(numbers) // [10, 13, 18, 15, 16, 22]

> - numbers.pop() // 20

- numbers.clear()
> - print(numbers) // []

> - numbers.index(1) // 2

> - numbers.count(5) // 1

> - range(10) // range(0, 10)

- square_num = [x ** 2 for x in range(10)]
> print(square_num) // [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

- cube_num = [y ** 3 for y in range(5)]
> print(cube_num) // [0, 1, 8, 27, 64]


# Dictionary in Python

=> Dictionary = A dictionary is a data type in Python used to store data in key–value pairs.

# methods in dictionary

- studentDetails = {"Name" : "Shivam Gupta", "age" : 22, "cource" : "Btech"}

> print(studentDetails) // {'Name': 'Shivam Gupta', 'age': 22, 'cource': 'Btech'}

> studentDetails["Name"] // 'Shivam Gupta'

> studentDetails.get('Name') // 'Shivam Gupta'

> studentDetails.get('address') // none (because data not present in to the dictionary)

> studentDetails.keys() // dict_keys(['Name', 'age', 'cource'])

> studentDetails.values() // dict_values(['Shivam Gupta', 23, 'Btech'])

> studentDetails.items() // dict_items([('Name', 'Shivam Gupta'), ('age', 23), ('cource', 'Btech')])

- studentDetails.update({'age': 25})
> print(studentDetails) // {'Name': 'Shivam Gupta', 'age': 25, 'cource': 'Btech'}

> studentDetails.pop('age') // {'Name': 'Shivam Gupta', 'cource': 'Btech'}

> studentDetails.popitem() // ('cource', 'Btech')

- studentDetails.clear()
> print(studentDetails) // {}

- newStudentDetails = studentDetails.copy()
>  print(newStudentDetails) // {'Name': 'Shivam Gupta', 'age': 22, 'cource': 'Btech'}

=> Looping Through Dictionary
-

for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)

# nested dictionary

studentDetails = {
... 'student1' : {'name': 'shivam kumar', 'age': 21, 'cource': 'Btech'},
... 'student2' : {'name': 'saurav singh', 'age': 23, 'cource': 'bca'}
... }

> print(studentDetails) // {'student1': {'name': 'shivam kumar', 'age': 21, 'cource': 'Btech'}, 'student2': {'name': 'saurav singh', 'age': 23, 'cource': 'bca'}}

> print(studentDetails['student1']) // {'name': 'shivam kumar', 'age': 21, 'cource': 'Btech'}

> print(studentDetails['student1']['name']) // shivam kumar

# How to create square or cube number dictionary

squareNum = {x:x ** 2 for x in range(6)}
> print(squareNum) // {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

cubeNum = {y:y ** 3 for y in range(6)}
> print(cubeNum) // {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

-> fromkeys(iterable, value) method

key = ['masala tea', 'ginger tea', 'lemon tea']
defaultVal = 'delicious'

new_dict = dict.fromkeys(key, defaultVal)
> print(new_dict) // {'masala tea': 'delicious', 'ginger tea': 'delicious', 'lemon tea': 'delicious'}

# Tuples

A tuple is a built-in data type used to store multiple values in a single 

- students = ('saurav', 'raman', 'ravi', 'mohit', 'pawan')
> print(students) // ('saurav', 'raman', 'ravi', 'mohit', 'pawan')

=> Add two tupple 

student1 = ('saurav', 'raman', 'ravi', 'mohit', 'pawan')

student2 = ('avunash', 'prakash', 'abhishek')

totalStudent = student1 + student2
> print(totalStudent) // ('saurav', 'raman', 'ravi', 'mohit', 'pawan', 'avunash', 'prakash', 'abhishek')

# Questions On Conditionals
<details>
<summary>
1. Age Group Categorizations
</summary>
Classify a person age group : child (< 13), teenager (13 - 19), adult(20 - 59), senior(60+). 
</details>

<details>
<summary>
2. Movie Ticket Pricing
</summary>
Movie tickets Prices are based on age: $12 for adult (18 and over), 8$ for children and everyone get a $2 discount on wednessday. 
</details>

<details>
<summary>
3. Grade Calculator
</summary>
Assign a latter grade based on student's score: A(90-100), B(80-89), C(70-79), D(60-69), E(50-59), F(40-49)  
</details>

<details>
<summary>
4. Fruit Ripeness Cheaker
</summary>
Determine it fruit is ripe, overrip, or unripe based on its color. (eg. Banana: Green - unripe, Yellow - Ripe, Brown - Overripe)  
</details>

<details>
<summary>
5. Weather Activity Suggestions
</summary>
Suggest an activity based on weather (eg. sunny - go for a walk, rainy - read a book, snowy - build a snowman) 
</details>

<details>
<summary>
6. Transportation Mode Selection 
</summary>
choose a mode of transportation based on a distance (eg. < 3 Km: walk, 3-15 km: Bike, > 15 km: car )
</details>

<details>
<summary>
7. Coffee Customization
</summary>
Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
</details>




- Note =>  when we want to change string into number then we can use int(" ")










