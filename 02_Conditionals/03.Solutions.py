# Assign a latter grade based on student's score: A(90-100), B(80-89), C(70-79), D(60-69), E(50-59), F(40-49)

studentScore = int(input("Please Enter Your Score: "))

if studentScore < 50 :
  grade = "F"
elif studentScore < 60  :
  grade = "E"
elif studentScore < 70 :
  grade = "D"
elif studentScore < 80 :
  grade = "C"
elif studentScore < 90 :
  grade = "B"
else :
  grade = "A"
print("You Have a Grade:",grade)
