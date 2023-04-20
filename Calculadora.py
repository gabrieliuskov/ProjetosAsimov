import os

resposta = 0
os.system('cls')

while resposta != 5:
    print('Seja bem vindo (a)')
    print('='*50)
    print(' 0: Soma\n 1: Subtração\n 2: Multiplicação\n 3: Divisão\n 4: Exponenciação \n 5: Sair')
    resposta = int(input('\nDigite a sua opção: '))

    if resposta == 0:
        print('\n\nSoma escolhida\n')
        numero1 = float(input('Digite um número: '))
        numero2 = float(input('Digite outro número: '))
        print(f'\nA soma é: {numero1+numero2}')
    elif resposta == 1:
        print('\n\nSubtração escolhida\n')
        numero1 = float(input('Digite um número: '))
        numero2 = float(input('Digite outro número: '))
        print(f'\nA subtração é: {numero1-numero2}')
    elif resposta == 2:
        print('\n\nMultiplicação escolhida\n')
        numero1 = float(input('Digite um número: '))
        numero2 = float(input('Digite outro número: '))
        print(f'\nA multiplicação é: {numero1*numero2}')
    elif resposta == 3:
        print('\n\nDivisão escolhida\n')
        numero1 = float(input('Digite um número: '))
        numero2 = float(input('Digite outro número: '))
        if numero2 == 0:
            print('\nNão há divisão por zero!')
        else:
            print(f'\nA divisão é: {numero1/numero2}')
    elif resposta == 4:
        print('\n\nExponenciação escolhida\n')
        numero1 = float(input('Digite um número: '))
        numero2 = float(input('Digite outro número: '))
        print(f'\nA exponenciação é: {numero1**numero2}')
    elif resposta == 5:
        break
    else:
        print('\n\nEntrada inválida!')
    
    pergunta = str(input('\n\nDeseja continuar? '))[0]

    if pergunta == 'N' or pergunta == 'n':
        break
    os.system('cls')

print("\n\nObrigado!")