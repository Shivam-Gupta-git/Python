# Check if a password is "week", "medium", "strong". chracter: < 6char (week), < 8 char (medium), > 8 char (strong)

password = str(input("Please enter your password: ")) 

if len(password) < 6 :
  print("Your password is week ! please enter a strong password")
elif len(password) < 8 :
  print("Yoyr password is medium ! please try to enter a strong password")
else : 
  print("Your password is strong, Good")

