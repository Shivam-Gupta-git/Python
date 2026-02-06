# Write a function that greets a user. if no name is provided, it should greet with a default name.

userName = input("Please enter your name: ")
def greet(name = "User"):
  return "Hello, " + name + " !"

print(greet(userName or "User"))
