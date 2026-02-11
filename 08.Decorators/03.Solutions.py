# Create a function to print the function name and the value of its argeument every time to function call

def debug(func):
  def wrapper(*args, **kwargs):
    argsValue = ', '.join(str(arg) for arg in args)
    kwargsValue = ', '.join(f"{k}={v}" for k, v in kwargs.items())

    print(f"calling name :{func.__name__} with args {argsValue} and kwargs {kwargsValue}")
    return func(*args, **kwargs)
  
  return wrapper



@debug
def greet(name, greeting="hello"):
  print(f"{greeting}, {name}")

greet("shivam", greeting="Welcome Back")  

  