# Demonstrate the use of Instance() to check if my_tesla is an instance of Car and ElectricCar

class Car:
  def __init__(self, brand, model):
    self.__brand = brand
    self.__model = model

  @property
  def brand(self):
    return self.__brand
  
  @property
  def model(self):
    return self.__model
  
  def fullName(self):
    return f"{self.brand} {self.model}"
  
  
class ElectricCar(Car):
  def __init__(self, brand, model, batteryType):
    super().__init__(brand, model)
    self.__batteryType = batteryType 

  @property   
  def batteryType(self):
    return self.__batteryType

newCar1 = Car("Toyota", "Corolla")
print(newCar1.brand)
print(newCar1.model)
print(newCar1.fullName())

newElectricCar1 = ElectricCar("Tesla", "Model S", "Lithium-Ion")
print(newElectricCar1.fullName())
print(newElectricCar1.batteryType)   

print(isinstance(newElectricCar1, Car))
print(isinstance(newElectricCar1, ElectricCar))
  

