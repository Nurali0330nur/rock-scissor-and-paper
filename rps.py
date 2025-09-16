import random

things = ['paper', 'rock', 'scissor']
choise = input('Choose 1 thing: paper, rock, scissor -> ')
random_item = random.choice(things)

def game(choise, random_item):
    if choise == 'paper' and random_item == 'paper':
       print('draw')
    elif choise == 'paper' and random_item == 'rock':
       print('You win')
    elif choise == 'paper' and random_item == 'scissor':
       print('You lose')

    if choise == 'rock' and random_item == 'rock':
       print('draw')
    elif choise == 'rock' and random_item == 'scissor':
       print('You win')
    elif choise == 'rock' and random_item == 'paper':
       print('You lose')

    if choise == 'scissor' and random_item == 'scissor':
       print('draw')
    elif choise == 'scissor' and random_item == 'paper':
       print('You win')
    elif choise == 'scissor' and random_item == 'rock':
       print('You lose')

print('Computer chose:', random_item)
game(choise, random_item)




