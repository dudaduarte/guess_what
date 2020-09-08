import random

def play():
    show_opening_message()
    secret_word = get_secret_word('fruits.txt')
    right_words = ['_' for c in secret_word]
    hanged = False
    won = False
    mistakes = 0
    total_of_tries = 7

    print(' '.join(right_words))

    while not hanged and not won:
        guess = input('Digite uma letra: ').strip().upper()

        if guess in secret_word:
          handle_right_guess(guess, secret_word, right_words)
        else:
            mistakes += 1
            draw_forca(mistakes)
            print(f'Errado! Você ainda tem {total_of_tries - mistakes} tentativas.')

        hanged = mistakes == total_of_tries
        won = '_' not in right_words

        print(' '.join(right_words))

    show_final_message(won, secret_word)


def handle_right_guess(guess, secret_word, right_words):
  index = 0

  for caractere in secret_word:
      if caractere == guess:
          right_words[index] = caractere
      index += 1

def get_secret_word(file):
    file = open(file, 'r')
    words = []

    for line in file:
        words.append(line.strip())

    file.close()

    random_index = random.randrange(0, len(words))
    return words[random_index].upper()

def show_opening_message():
    print('*********************************')
    print('Bem vindo ao jogo da Forca!')
    print('*********************************')


def show_final_message(won, word):
    print('*********************************')
    if won:
        print('Parabéns! Você ganhou')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print('Você perdeu :(')
        print(f'A palavra secreta era {word}')
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    print('*********************************')

def draw_forca(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == '__main__':
    play()
