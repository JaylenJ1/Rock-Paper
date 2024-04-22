import random


player_choice = input("What will you throw? R/P/S or Quit ")

while player_choice != 'Quit':

  
  options = ['rock', 'paper', 'scissors']

  if (player_choice == 'R' and options == 'rock') or (player_choice == 'P' and options == 'paper') or (player_choice == 'S' and options == 'scissors'):
    print(f'Its a Tie, you choose ${player_choice} and I choose S{options}')
  elif player_choice == 'R' and options == 'paper':
    print("You lose")
  elif player_choice == 'P' and options == 'rock':
    print("You Win")
  elif player_choice == 'R' and options == 'scissors':
    print("You win")
  elif player_choice == 'P' and options == 'scissors':
    print("You lose")
  elif player_choice == 'S' and options == 'paper':
    print("You win")
  elif player_choice == 'S' and options == 'rock':
    print("You lose")
  elif player_choice == 'Quit':
    break
  else: 
    print("That is not a valid choice")
    break




print(random.choice(options))


