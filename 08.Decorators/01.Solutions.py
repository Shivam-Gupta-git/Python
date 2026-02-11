# Example of decorator 

def myDecorator(func):
  def wrapper():
    print("before function calling")
    func()
    print("after function calling")
  return wrapper

@myDecorator
def sayHello():
  print("Hello !")

sayHello()  