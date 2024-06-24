print(
    "this is a simple game called 'snake water gun' it is similar to rock paper scissors where you have to choose between snake, water and gun. The computer will also choose one of the three options and the winner will. The winner will be decided by the following rules: \n\n1. snake drinks water \n\n2. gun shoots snake \n\n3. water drowns gun\n \n"
)
print(
    "lets start the game the points will be counted and the winner will be decided after a player wins 5 rounds\n \n"
)
import random


a = "Y"
while a == "" or a == "Y":
  pp = 0
  cp = 0
  cmv = 0
  while (pp < 5 and cp < 5):
    cmv = random.randint(1, 3)
    pmv = int(input("choose between snake, water and gun:(1,2,3)\n"))
    if cmv == 1:
      print("computer chose snake")
    elif cmv == 2:
      print("computer chose water")
    else:
      print("computer chose gun")
    if pmv == cmv:
      print("its a tie \n")
    elif (pmv == 1 and cmv == 2) or (pmv == 2 and cmv == 3) or (pmv == 3 and cmv == 1):
      print("you won this round \n")
      pp = pp + 1
      print(f"your points are {pp} and computer points are {cp}")
    else:
      print("computer won this round \n")
      cp = cp + 1
      print(f"your points are {pp} and computer points are {cp}")
    if (cp == 5):
      print("you lost the game")
      break
    elif (pp == 5):
      print("you won the game")
      break

  a = input("do you want to play again?(y/n)").upper()
