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

-> Depth in number data type ---------------------

- random method in python
- import random after that just call it 

random.random()
0.08514996672388664 // output

random.randint(1, 10)
1 // output

random.randint(1, 10)
8 // output

- random.choice() is used to return a random element from a given list (or any sequence). Each time you call it, it may return a different element from the array.

- Example :
l1 = ['lemon tea', 'masala tea', 'ginger tea', 'mint tea']

random.choice(l1)

'mint tea' // output 

random.choice(l1)

'lemon tea' //output

- random.shuffle() : It changes the order of elements in the same list every time it is called.

Example: 
l1 = ['lemon tea', 'masala tea', 'ginger tea', 'mint tea']

random.shuffle(l1) // call

l1 // call

['masala tea', 'ginger tea', 'lemon tea', 'mint tea'] // output

random.shuffle(l1) // call

l1 // call

['lemon tea', 'masala tea', 'ginger tea', 'mint tea']

- from decimal import Decimal : from decimal import Decimal is used to perform high-precision decimal arithmetic in Python. Floating-point numbers (float) can give inaccurate results due to binary representation.

Example (problem with float)

> print(0.1 + 0.2)

>0.30000000000000004 // output

- Using Decimal

from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')

print(a + b)

> 0.3 // output

-> Set Data Type ------------------------------

setone = {1, 2, 3, 4}

- setone & {1, 3} // find intersection 

> {1, 3} // output because both are common

- setone | {4, 5} // find union

> {1, 2, 3, 4, 5} // output

-> String in python ------------------------------
chai = 'Masala Chai'

- find firsh character of given string

first_char = chai[0]

> print(first_char) // output is M

-> Slicing :
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

=> Common String Methods :

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

- String Containing : string containing usually means checking whether a string contains a specific character or substring.

Example:  text = "Python programming"

> print("Python" in text)     # True

> print("Java" in text)       # False

-> List ...................................

- A list is a built-in data type in Python used to store multiple values in a single variable.

- decleration of list

students = ['shubham', 'mohan', 'sohan', 'saurav']

> print(students) // ['shubham', 'mohan', 'sohan', 'saurav']

=> List Slicing

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

=> Remove element into the give list

Example : students = ['shubham', 'Ravi', 'anish', 'mohan', 'sohan', 'saurav']

students[1:3] = []

> print(students) // ['shubham', 'mohan', 'sohan', 'saurav']












