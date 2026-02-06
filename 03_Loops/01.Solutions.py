#  Given a list of an number, count how many are positives.  

numbers = [-2, -4, 5, 1, -7, 9]
positiveNum = []

for num in numbers :
  if num > 0 :
    positiveNum.append(num)
print("Positive Number is:",positiveNum, "and length is:",len(positiveNum))