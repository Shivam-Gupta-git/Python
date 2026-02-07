# Create a function that accept any number of keyword arguments and print them in the format key:value

def numbers(**kwargs):
  print(kwargs)

print(numbers(name= 'Shivam', age= 22))  