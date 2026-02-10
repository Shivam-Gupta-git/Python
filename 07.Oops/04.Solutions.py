# Create a ElectricCar Class that inherits from the Car class and has an additional attribute batterySize

class Car :
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def fullName(self):
    return f"{self.brand} {self.model}" 
  
class ElectricCar(Car) :
  def __init__(self, brand, model, batterySize):
    super().__init__(brand, model)
    self.batterySize = batterySize


# newCar1 = Car("Toyota", "Corolla")
# print(newCar1.brand)
# print(newCar1.model)
# print(newCar1.fullName())  

newElectricCar1 = ElectricCar("Tesla", "Model S", "85KWH")
print(newElectricCar1.batterySize)
print(newElectricCar1.brand)
print(newElectricCar1.model)
print(newElectricCar1.fullName())

