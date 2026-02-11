# Create a Login Check Decorator

def loginRequirment(fun):
  def wrapper(user):
    if user != "admin":
      print("access denied")
      return
    return fun(user)
  return wrapper  


@loginRequirment
def dashboard(user):
  print(f"Welcome to the Dashboard. {user}")

dashboard("user")  