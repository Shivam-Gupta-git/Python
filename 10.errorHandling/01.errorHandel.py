file = open('youtube.txt', 'w')

# this is a first way to handel file errors
try:
  file.write('start my coding jurney')
finally:
  file.close()

# this is a second way to handel file errors 
with open('youtube.txt', 'w') as file :
  file.write('start my python jurney')    

