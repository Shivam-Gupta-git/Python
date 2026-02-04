distance = int(input("Enter your distance: "))

if distance < 0 :
  print("Pleae enter valid distance")
  exit()

if distance < 3 :
  transport = "Walk"
elif distance <= 15 :
  transport = "Bike"
else :
  transport = "Car"  

print("AI recommands you the transport of:",transport)