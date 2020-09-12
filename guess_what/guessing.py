import random
from guess_what import io

def play():
    print('*********************************')
    print('Bem vindo ao jogo de Adivinhação!')
    print('*********************************')

    print('Níveis:')
    io.print_enumerated_list(['Fácil', 'Médio', 'Difícil'])

    dificulty = int(input('Digite o número correspondente à dificuldade que deseja jogar: '))
    secret_number = random.randrange(1, 101)
    total_of_tries = 0
    points = 1000

    if(dificulty == 1):
        total_of_tries = 15
    elif(dificulty == 2):
        total_of_tries = 10
    else:
        total_of_tries = 5

    for round in range(1, total_of_tries + 1):
        print('Tentativa {} de {}'.format(round, total_of_tries))
        number = int(input('Digite um número entre 1 e 100: '))
        if(number < 1 or number > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue
        if(number == secret_number):
            print('Você acertou!')
            break
        else:
            points = points - abs(secret_number - number)
            if(number > secret_number):
                print('Você errou :( seu chute foi maior que o número secreto')
            elif(number < secret_number):
                print('Você errou :( seu chute foi menor que o número secreto')

    print('*********************************')
    print('Fim do jogo')
    print(f'O número secreto era {secret_number}')
    print(f'Vocẽ fez {points} pontos')
    print('*********************************')

if(__name__ == '__main__'):
    play()
