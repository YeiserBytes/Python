import random


secret_number = random.randint(1, 100)
riddle = int(input('Adivina el número secreto entre 1 y 100: '))
maxTrys = 5
trys = 1

while riddle != secret_number and trys < maxTrys:
    if riddle < secret_number:
        print('El número secreto es mayor que ese. Inténtalo de nuevo')
    else:
        print('El número secreto es menor que ese. Inténtalo de nuevo')
    trys += 1
    riddle = int(input('Adivina el número secreto entre 1 y 100: '))

if riddle == secret_number:
    print('Felicidades, has adivinado el número secreto!')
else:
    print('Lo siento, has fallado. El número secreto era', secret_number)
