import random


def select_word():
    words = ['python', 'javascript', 'java', 'ruby',
             'php', 'csharp', 'html', 'css', 'swift', 'kotlin']
    return random.choice(words)


def play_hangman(word):
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print('Vidas restantes:', lives)
        print('Letras utilizadas:', ' '.join(used_letters))
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print('Palabra actual: ', ' '.join(word_list))
        user_letter = input('Adivina una letra: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('La letra', user_letter, 'no está en la palabra.')
        elif user_letter in used_letters:
            print('Ya has usado esa letra. Inténtalo de nuevo.')
        else:
            print('Entrada inválida. Inténtalo de nuevo.')
    if lives == 0:
        print('Perdiste, la palabra era', word)
    else:
        print(f'¡Felicidades! ¡Adivinaste la palabra {word}!')


def main():
    print('¡Bienvenido al juego de Hangman!')
    word = select_word()
    play_hangman(word)


if __name__ == '__main__':
    main()
