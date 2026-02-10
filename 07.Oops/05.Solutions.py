# modify the Car class to encapsulation the brand attribute, make it private and provide a getter method for it

class Car :
  def __init__(self, brand, model):
    self.__brand = brand
    self.model = model

  def getBrand(self):
    return self.__brand + " !" 
   
  def fullName(self):
    return f"{self.brand} {self.model}"
  
class ElectricCar(Car) :
  def __init__(self, brand, model, batterySize):
    super().__init__(brand, model)
    self.batterySize = batterySize


newElectricCar1 = ElectricCar("Tesla", "Model S", "85KWH")
# print(newElectricCar1.brand)
# print(newElectricCar1.model)
# print(newElectricCar1.batterySize)
# print(newElectricCar1.fullName())

print(newElectricCar1.getBrand())
