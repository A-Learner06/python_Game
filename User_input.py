from rock_game import ROCKPAPERSCISSER
from guess_game import Guessing_game

print("----- Hello Gamer -----")
print("***** Here The List Of Games For You .*****")
print("1. Rock Paper Scisors ")
print("2. Guessing Numbers ")

User_input = int(input("Enter Which Game u Want To Play (1-2) :"))

if User_input == 1 :
  print("_____Great Choice_____")
  print("Lets Play Rock Paper Scisors Game! ")
  ROCKPAPERSCISSER()
elif User_input == 2:
  print("_____Great Choice_____")
  print("Lets Play Guessing Numbers game!")
  Guessing_game()
else:
  print("Plese Choose Valid Options . ")