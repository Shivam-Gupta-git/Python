# Create a car class with attributes like brand and models. then create an instance of the class.

class Car :
  def __init__(self, brand, model) :
    self.brand = brand
    self.model = model
  

myCar = Car("Toyota", "Corolla")
print(myCar.brand)
print(myCar.model)

myCar2 = Car("Tata", "Safari")
print(myCar2.model)
print(myCar2.brand)

