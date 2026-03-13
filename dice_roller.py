## Packages to import
import math
import random

## Dice Rolling Function

def dice_roll(input):
    dice_num = int(input)
    if dice_num < 101 and dice_num > 6:
        return random.randint(1,dice_num)
    else:
        return 'Invalid Number. Try Again'
    
## Pretty Line Break Function

def pretty_line_break():
    return print("="*66)

## The main program

pretty_line_break()
print('\n')
dice_number = input('Enter the size of your dice: \n')

rolling = dice_roll(dice_number)

print('Your dice roll is: \n' + str(rolling))

print('\n')
pretty_line_break()
