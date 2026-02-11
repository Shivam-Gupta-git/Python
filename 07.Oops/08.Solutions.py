class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def fullName(self):
    return f"{self.brand} {self.model}"
  
  def carType(self):
    return "Fuel + Deasel"

  @staticmethod
  def generalDescription():
    return "Cra are means of transport"

newCar1 = Car("Tata", "Safari")  

print(Car.generalDescription())
