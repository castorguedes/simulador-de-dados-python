import random

print('Seja bem-vindo(a) ao Simulador de Dados.')
print('Assim como um dado de verdade, essa aplicação desenvolvida em Python apresentará um número aleatório entre 1 e 6.')
dado = (random.randrange(1, 7))

i = input('Deseja rolar o dado? Digite apenas s para sim ou n para não: ')
while i != 's' and i != 'n':
    print()
    i = input('Valores inválidos. Digite APENAS s para sim ou n para não: ')
while i == 's':
    if i == 's':
        print('O número rolado foi ',dado)
        print()
        i = input('Deseja rolar novamente? Digite apenas s para sim ou n para não: ')
        while i != 's' and i != 'n':
            print()
            i = input('Valores inválidos. Digite APENAS s para sim ou n para não: ')
if i == 'n':
    print('Entendido. Finalizando a aplicação.')