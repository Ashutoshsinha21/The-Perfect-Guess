import random
randNumber= random.randint(1,100)
guesses=0
userGuess= None

while(userGuess!=randNumber):
  userGuess=int(input("Enter the number\n"))
  guesses+=1
  if(userGuess==randNumber):
    print("You have guessed right.")
  else:
    if(userGuess>randNumber):
      print("You have guessed wrong! Please enter smaller number")
    else:
      print("You have guessed wrong! Please enter larger number")

print(f"You have guessed no in {guesses} guesses")
