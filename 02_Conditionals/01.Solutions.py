# Classify a person age group : child (< 13), teenager (13 - 19), adult(20 - 59), senior(60+).

userAge = int(input("Please enter your age: "))
if userAge < 13 :
  print("user is Child")
elif userAge < 20 :
  print("user is Teenaser")
elif userAge < 60 :
  print("user is Adult")
else :
  print("user is Senior")