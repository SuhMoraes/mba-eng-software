# escolha um numero aleatório
# entre 1 e 5
# receb um chute
# se for igual ao numero aletório => Acertou
# Senão, quase, o número secreto era {numero_secreto}
import random

print('Número aleatório\n')
numero_secreto = random.randint(1, 5)

print('Escolha um número entre 1 e 5')
chute = int(input('Digite um numero: '))

random.seed(5)

if chute == numero_secreto:
    print('Acertou!')
else: 
    print(f'Quase... O número secreto era {numero_secreto}')

