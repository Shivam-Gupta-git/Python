# Write a decorator that measure the time a function take to execute.

import time

def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__} ran in {end-start} time")
    return result
  
  return wrapper

@timer
def exampleFunction(n):
  time.sleep(n)

exampleFunction(2)  
