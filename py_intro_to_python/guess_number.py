# -*- coding: utf-8 -*-
import random

print('Olá qual é o seu nome?')
name = input()

secretNumber = random.randint(1, 20)
print('Olá ' + name + ' pense num número entre 1 e 20')

# print('DEBUG: The secret number is: ', str(secretNumber))

for guessTaken in range(1, 6):
    print('Escolha outro número')
    guess = int(input())

    if guess < secretNumber:
        print('Sua escolha está baixa demais')
    elif guess > secretNumber:
        print('Sua escolha está alta demais')
    else:
        break

if guess == secretNumber:
    print('Boa escolha ' + name + ', acertou em apenas ' +
          str(guessTaken) + ' tentativas')
else:
    print('Você ultrapassaou o limite de tentativas: ' +
          '(' + str(guessTaken) + ')')
