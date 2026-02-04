weather = input("Please enter one of the following weather: Sunny, Rainy, or Snowy: ").lower()

if weather not in ("sunny", "rainy", "snowy") :
  print("Please choose a valid weather")
  exit()

if weather == 'sunny' :
  print("Go for a walk")
elif weather == 'rainy' :
  print("Read a book")
elif weather == 'snowy' :
  print("Build a snowman")

