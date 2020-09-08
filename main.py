import hangman
import guessing

def select_game():
    print('Jogos disponíveis:')
    print('1 - Adivinhação')
    print('2 - Forca')

    jogo = int(input('Digite o número correspondente ao que deseja jogar: '))

    if (jogo == 1):
        print('Jogando Adivinhação')
        guessing.play()
    elif (jogo == 2):
        print('Jogando Forca')
        hangman.play()

if(__name__ == '__main__'):
    select_game()