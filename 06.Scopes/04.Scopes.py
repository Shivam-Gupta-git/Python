# Example of closer.......

def outerFun() :
  x = 30
  def innerFun(y) :
    sum = x + y
    return sum
  return innerFun

result = outerFun()
print(result(20))