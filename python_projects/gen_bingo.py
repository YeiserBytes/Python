import random


letters = ['B', 'I', 'N', 'G', 'O']
numbers = list(range(1, 76))


def gen_card():
    card = []
    for letter in letters:
        column = []
        for i in range(5):
            if letter == 'N' and i == 2:
                column.append(" ")
            else:
                number = random.choice(numbers)
                numbers.remove(number)
                column.append(number)
        card.append(column)
    return card


def show_card(card):
    print('B I N G O')
    for i in range(5):
        row = []
        for j in range(5):
            row.append(str(card[j][i]).rjust(2))
        print(" ".join(row))

card = gen_card()
show_card(card)
