import re

def norm_roll(num, sides):
  return num * (sides/2.0 + .5)

def dis_roll(num, sides):
  if(num>1):
    result = (1/(num+1)) * sides + .5
  else:  
    result = norm_roll(num, sides)
  return result

def adv_roll(num, sides):
  result = norm_roll(num, sides)
  if(num>1):
    result = (num/(num+1)) * sides + .5
  else:  
    result = norm_roll(num, sides)
  return result

def dice_parse(dice):
    first = dice[0] #first char, to check for adv/dis
    if(first== '-' or first== '+'):
      dice = dice.replace('-', '')
      dice = dice.replace('+', '')
    if(dice[0] == 'd'):
      
      num = 1
      faces = int(dice.replace('d', ''))
    else:
      halves = dice.split("d")
      num = int(halves[0]) #number of dice
      faces = int(halves[1]) #number of faces on dice


    if(first == '-'): #if disadvantage
      print("Expected Value of a " +str(num) +"d"+ str(faces) + " (disadvantage roll): " + str(round(dis_roll(num, faces),3)) + "~")
    elif(first == '+'): #if advantage
      print("Expected Value of a " +str(num) +"d"+ str(faces) +  " (advantage roll): " + str(round(adv_roll(num, faces),3))+ "~")
    else:
      print("Expected Value of a " + str(num) +"d"+ str(faces) + ": " + str(round(norm_roll(num, faces),3)))

##PROGRAM START##
data = ""
while(data != 'q'):
  print("----------------------\nEnter your dice rolls.")
  data = input().lower().strip()
  data = re.sub(' +', ' ', data)
  if(data == "h" or data == "H"):
    print("HELP:\nFormat dice input as 'xdn' where x is the number of dice and n is the number of sides. \n-Ex: \"2d6\" would be the value of 2 dice that are 6 sided" 
    + "\nTo roll with advantage put a '+' before the dice code. \n-Ex: \"+2d8\" would roll 2 d8 and take the higher value."
    + "\nTo roll with disadvantage put a '-' before the dice code. \n-Ex: \"-2d8\" would roll 2 d8 and take the lower value."
    + "\nYou can see the average of multiple types of rolls in one input by seperating several 'ndx' inputs with any other character such as a space. \n-Ex: \"d6 6d4 -3d12\" would roll 1 d6, 6 d4's, and 3 d12's with disadvantage."
    + "\n\nENTER 'q' IF YOU WOULD LIKE TO QUIT")
  else:
    print("\n")
    entries = data.split(" ")
    for entry in entries:
      match = re.fullmatch("^([-+]?(?:[1-9][0-9]*)*[d][0-9]+)$", entry)

      if(match != None):
         dice_parse(entry)
      else:
        print(entry + ": Input formatted incorrectly. Please enter 'h' for help \n")


print("\nThank you for testing your luck!")
