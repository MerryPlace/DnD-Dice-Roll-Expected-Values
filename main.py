import re

def norm_roll(num, sides):
  print("Expected Value of " + str(num) +"d"+ str(int(sides)) +" is: " + str(num * (sides/2.0 + .5)) + "\n")

def dis_roll(num, sides):
  denom = sides**2

  numer = (sides*2) - 1

  total = 0.0
  for side in range(1,sides + 1, 1): #from 1 to max side
    total += (side*(numer))/denom
    numer -= 2

  print("Expected Value of " + str(num) +"d"+ str(int(sides)) +" with disadvantage is: " + str(num*total) + "\n")

def adv_roll(num, sides):
  denom = sides**2
  numer = (sides*2) - 1

  total = 0.0
  for side in range(sides,0, -1): #from max side to 1
    total += (side*(numer))/denom
    numer -= 2

  print("Expected Value of " + str(num) +"d"+ str(int(sides)) +" with advantage is: " + str(num*total) + "\n")

def dice_parse(dice):
  for x in dice:
    halves = x.split("d")
    front = halves[0] #first half (becomes number of dice)
    faces = int(halves[1]) #number of faces on dice
    first = front[0] #first char, to check for adv/dis

    if(first== '-' or first== '+'):
      front = front.replace('-', '')
      front = front.replace('+', '')

    num = int(front) #number of dice

    if(num > 0 and faces > 0):
      if(first == '-'): #if disadvantage
        dis_roll(num, faces)
      elif(first == '+'): #if advantage
        adv_roll(num, faces)
      else:
        norm_roll(num, faces)
    else:
      print("Numbers must be positive. You can't roll negative sided dice!")



##PROGRAM START##
data = ""
while(data != 'q' and data != 'Q'):
  print("\nEnter the code of your desired selection:")
  data = input()

  if(data == "h"):
    print("HELP:\nFormat dice as 'ndx' where n is the number of dice and x is the number of sides. \n-Ex: \"2d6\" would be the mean value of 2 dice that are 6 sided" 
    + "\nTo roll with advantage put a '+' before the dice code. \n-Ex: \"+1d8\" would roll 2 d8 and take the higher value."
    + "\nTo roll with disadvantage put a '-' before the dice code. \n-Ex: \"-1d8\" would roll 2 d8 and take the lower value."
    + "\nYou can see the average of multiple types of rolls in one input by seperating several 'ndx' inputs with any other character such as a space. \n-Ex: \"4d6 6d4 -3d12\" would roll 4 d6's, 6 d4's, and 3 d12's with disadvantage."
    + "\n\nENTER 'q' IF YOU WOULD LIKE TO QUIT")
  else:
    dice = re.findall("[-+]?[0-9]+[dD][0-9]+", data)
    if(len(dice) == 0 and data != 'q'):
      print("Input formatted incorrectly. Please enter 'h' for help or 'q' to quit")
    else:
      dice_parse(dice)

print("\nThank you for testing your luck!")
