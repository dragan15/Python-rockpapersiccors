from random import randint #random generator
player = input('Choose one: rock(r), paper(p), scissors(s)') #Prints out choices

print(player,'vs', end=) #prints out what player chooses

compchoose= randint(1,3) #prints random number between 1-3

if compchoose == 1:
  computer = 'r';
elif compchoose == 2:
  computer = 'p';
else:
  computer = 's';
  
print(computer)

if player == compchoose:
  print('DRAW!')
elif player == 'r' and compchoose == 's':
  print('PLAYER WINS!')
else:
  print('COMPUTER WINS!!') 


