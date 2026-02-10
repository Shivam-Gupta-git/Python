# Example of Enclosing Scope.......
x = 20

def myfun1() :
  # x = 30
  def myfun2(y) :
    sum = x + y
    return sum
  result = myfun2(30)
  print(result)

myfun1()  
