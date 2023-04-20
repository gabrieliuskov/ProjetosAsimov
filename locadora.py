import os
import random

modelos = ['Fiat Uno','Fiat Mobi','Fiat Palio','Chevrolet Meriva','Ferrari Aventor','Buggati Sportline','Masseratti C320']
valores = [30, 40, 80, 150, 500, 1500, 3000]

carros = []

for i in range(len(modelos)):
    meu_dicionario = {'modelo': modelos[i], 'valor': valores[i], 'codigo':i, 'status': random.randint(0,1)}
    carros.append(meu_dicionario)

while True:
    os.system('cls')
    
    print('\nBem-vindo (a) à locadora\n')
    print('==='*40)
    print('\n\nMenu de opções:')
    print('\n0 - Mostrar portifolio     |   1 - Alugar um veículo   |   2 - Devolver um veículo')
    opt = int(input('\n\nDigite uma opção: '))

    if opt == 0:
        print('\nLista de carros: \n')
        for i in carros:
            if i['status'] == 1:
                status = 'Disponivel'
            else:
                status = 'Alugado'

            print(f'[{i["codigo"]}] {i["modelo"]} - R$ {i["valor"]:.2f} por dia - Status: {status}')
        
    elif opt == 1:
        print('\nLista de carros disponiveis: \n')
        for i in carros:
            if i['status'] == 1:
                print(f'[{i["codigo"]}] {i["modelo"]} - R$ {i["valor"]:.2f} por dia')

        opt2 = int(input('\nDigite o código do veículo desejado: '))
        qtd = int(input('\nQuantos dias deseja alugar: '))

        print(f'\nVocê escolheu {carros[opt2]["modelo"]} por {qtd} dias.')
        print(f'O valor totalizaria R$ {(qtd*carros[opt2]["valor"]):.2f}. Deseja alugar?')

        resp = int(input('\n0 - Sim | 1 - Não: '))

        if resp == 0:
            carros[opt2]["status"] = 0
            print(f'{carros[opt2]["modelo"]} alugado com sucesso!')
        else:
            print('Ok!')
            
    elif opt == 2:
        print('\nLista de carros alugados: \n')
        for i in carros:
            if i['status'] == 0:
                print(f'[{i["codigo"]}] {i["modelo"]} - R$ {i["valor"]:.2f} por dia') 

        opt2 = int(input('\nDigite o código do carro que deseja devolver: '))
        print(f'\nObrigado por devolver o carro {carros[opt2]["modelo"]}!')

        carros[opt2]["status"] = 1

    opt2 = int(input('\n0 - Continuar | 1 - Sair: '))

    if opt2 == 1:
        break   

print('\nObrigado!')


        
    
    


    
            

                   




