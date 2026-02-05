size = input("Please enter one of the following weather: small, medium, large: ").lower()
extraSort = True

if size not in ("small", "medium", "large") :
  print("Please Select a valid size")
  exit()

if extraSort :
  coffee = size + "coffee with an extra sort"
else :
  coffee = size + " coffee"

print("Order",coffee)  
