# Create two battery classes and engine, and let the ElectricCar class inherit from both demonstrating multiple inheritance

class Battery:
  def batteryInfo(self):
    return "this is battery"

class Engine:
  def engineInfo(self):
    return "this is engine"

class ElectricCar(Battery, Engine):
  def __init__(self, brand, model):
    self.__brand = brand
    self.__model = model

  @property
  def brand(self):
    return self.__brand
  
  @property
  def model(self):
    return self.__model

newElectricCar1 = ElectricCar("Tesla", "Model")
print(newElectricCar1.batteryInfo())
print(newElectricCar1.engineInfo())
print(newElectricCar1.brand)
print(newElectricCar1.model)


