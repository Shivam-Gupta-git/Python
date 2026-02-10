# Add a class variable to car that keeps track of the number of cars created

class Car:
  totalCar = 0
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    Car.totalCar += 1

  def fullName(self):
    return f"{self.brand} {self.model}"

  def carType(self):
    return "Petrol or Deasel"

newCar1 = Car("Tata", "Safari")
newCar2 = Car("Tata", "Nexon")

print(newCar1.fullName())
print(newCar2.fullName())
print(Car.totalCar)