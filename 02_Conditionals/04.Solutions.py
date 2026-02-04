# Determine it fruit is ripe, overrip, or unripe based on its color. (eg. Banana: Green - unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Please enter fruit name: ")
color = input("Please enter one of the following colors: yellow, green, or brown: ").lower()

if color not in ("yellow", "green", "brown"):
    print("Please choose a valid color")
    exit()

if color == "yellow":
    print("Your", fruit, "is ripe")
elif color == "green":
    print("Your", fruit, "is unripe")
elif color == "brown":
    print("Your", fruit, "is overripe")