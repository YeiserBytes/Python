import random


def drop_dice():
    dice = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice, dice2

while True:
    response = input("¿Quieres lanzar los dados? (s/n) ")
    if response.lower() == 's':
        dice, dice2 = drop_dice()
        print('Dado 1:', dice)
        print('Dado 2:', dice2)
        print('Total:', dice + dice2)
    else:
        break