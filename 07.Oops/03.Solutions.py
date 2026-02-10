# Add a method to a Car class that display the full name of the car.

class Car :
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def fullName(self) :
      return f"{self.brand} {self.model}"


myCar = Car("Toyota", "Corolla") 
print(myCar.brand)
print(myCar.model) 
print(myCar.fullName())  
