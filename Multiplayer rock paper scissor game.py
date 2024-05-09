from getpass import getpass as input
print("E P I C    🪨  📄 ✂️    B A T T L E")
print()
print("Wanna play rock,paper & scissors? Type R for rock, P for paper & S for scissors")
print()
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")
if player1 == 'R' and player2 == 'R':
  print("It's a tie!")
elif player1 == 'R' and player2 == 'P':
  print("Player 2 wins!")
elif player1 == 'R' and player2 == 'S' or player1 == 'P' and player2 == 'R':
  print("Player 1 wins!")
elif player1 == 'P' and player2 == 'P':
  print("It's a tie!")
elif player1 == 'P' and player2 == 'S' or player1 == 'S' and player2 == 'R':
  print("Player 2 wins!")
elif player1 == 'S' and player2 == 'P':
  print("Player 1 wins!")
elif player1 == 'S' and player2 == 'S':
  print("It's a tie!")
else:
  print("Invalid move!")
  