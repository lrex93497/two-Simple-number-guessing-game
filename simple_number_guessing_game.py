import time
min = int(input("Choose a minimum int number:"))
max = int(input("Choose a maximum int number:"))


import random
tnum = random.randint(min, max)
gnum = int(input("Make a guess:"))
count = 1


while gnum != tnum:
  if gnum >tnum:
    print("Your guess is too big!")
  if gnum <tnum:
    print("Your guess is too small!")
  gnum = int(input("Make a guess:"))
  count +=1
  
  
print("Well done. You got it in {} tries!".format(count))
time.sleep(5)