# Demonstrate polymorphish by defining a method fuelType in both Car and ElectricCar classes but with diffrent behaviour.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def fullName(self):
    return f"{self.brand} {self.model}"

  def fuelType(self):
    return "Petrol or Diesel"

class ElectricCar(Car):
  def __init__(self, brand, model, batterySize):
    super().__init__(brand, model)
    self.batterySize = batterySize

  def fuelType(self):
    return "Electric Charge"


newCar1 = Car("Toyota", "Corolla")  
print(newCar1.fuelType())

newElectricCar1 = ElectricCar("Tesla", "Model S", "85KWH")
print(newElectricCar1.fuelType())

