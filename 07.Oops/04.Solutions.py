# Create a ElectricCar Class that inherits from the Car class and has an additional attribute batterySize

class Car :
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def fullName(self):
    return f"{self.brand} {self.model}" 

newCar1 = Car("Toyota", "Corolla")
print(newCar1.brand)
print(newCar1.model)
print(newCar1.fullName())   