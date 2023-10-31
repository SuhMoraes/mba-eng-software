print('IMC\n')

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura:'))


imc = peso / altura ** 2 

# Arredondando o valor com round(), e 
# definindo quantas casas terá após a vírgula
imc = round(imc, 2)

print(f'\nO IMC é {imc}')