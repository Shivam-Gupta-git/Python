items = ["apple", "banana", "orange", "mango", "apple"]

unique_Item = set()

for item in items :
  if item in unique_Item :
    print("Duplicate item in list is:",item)
    break
  unique_Item.add(item)
print("Unique Item in list is:",unique_Item)  