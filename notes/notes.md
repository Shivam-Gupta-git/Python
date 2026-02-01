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

- Numbers in depth :
