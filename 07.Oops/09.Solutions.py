# Use a property decorator in the Car class to make the model attribute only.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.__model = model

  @property
  def model(self):
    return self.__model  

newCar1 = Car("Tata", "Safari") 
print(newCar1.model)
