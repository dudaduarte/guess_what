from guess_what import hangman
from guess_what import io
from guess_what import guessing

def select_game():
    print('Jogos disponíveis:')
    io.print_enumerated_list(['Adivinhação', 'Forca'])

    jogo = int(input('Digite o número correspondente ao que deseja jogar: '))

    if (jogo == 1):
        print('Jogando Adivinhação')
        guessing.play()
    elif (jogo == 2):
        print('Jogando Forca')
        hangman.play()

if(__name__ == '__main__'):
    select_game()
