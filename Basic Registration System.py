from time import sleep

def title():
    print('-'*80)
    print('BANCO DEV'.center(80))
    print('-'*80)

def opc():
    opcc = int(input('Bem Vindo ao banco DEV, o que você gostaria hoje?\n1. Cadastrar\n2. Visualizar cadastros\n3. Excluir cadastros\n4. Criar arquivo de cadastros\n5. Encerrar programa\nR: '))
    if opcc == 1:
        cadastrar()
    if opcc == 2:
        visualizar()
    if opcc == 3:
        opcao = str(input('\nVocê tem certeza que quer excluir os cadastros? [Y/N]\nR: '))
        if opcao in 'yY':
            with open('cadastros.txt', 'w+') as arquivo:
                arquivo.write('')
                arquivo.close()
            print('\nExcluido!\n')
            opc()
        if opcao in 'nN':
            print('\nOk!\n')
            opc()
    if opcc == 4:
        open('cadastros.txt', 'x')
        print('\nCriando "cadastros.txt"...\n')
        sleep(1)
        print('\nCriado!\n')
        opc()
    if opcc == 5:
        print('\nObrigado pela preferência! Volte sempre!')
        sleep(1)
        print('Encerrando...')
        sleep(1)
        return 0

def cadastrar():
    try:
        open('cadastros.txt', 'r')
    except:
        print('\n\033[0;33mPrimeiro crie um arquivo para cadastros!!!\033[0;m\n')
        opc()
    opcqt = int(input('\nQuantas pessoas você deseja cadastrar?\nR: '))
    for qt in range(0, opcqt):
        x = input('Nome: ')
        if not x.isalpha():
            while True:
                print('\n\033[0;33mDigite apenas letras para o nome.\033[0;m\n')
                x = input('Nome: ')
                if x.isalpha():
                    break
        y = str(input('Idade: '))
        if not y.isnumeric():
            while True:
                print('\n\033[0;33mDigite apenas números para idade.\033[0;m\n')
                y = input('Idade: ')
                if y.isnumeric():
                    break
        with open('cadastros.txt', 'a') as arquivo:
            arquivo.write(x)
            arquivo.write(';')
            arquivo.write(y)
            arquivo.write(':')
        print('\033[0;32mCadastrado!\033[0;m\n')
    print(f'Feito! Obrigado pelos {opcqt} cadastro(s)!\n')
    opc()

def visualizar():
    try:  
        with open('cadastros.txt', 'r') as arquivo:
            texto = arquivo.read()
    except:
        print('\n\033[0;33mPrimeiro crie um arquivo para cadastros!!!\033[0;m\n')
        opc()
    texto = texto.split(':')
    print('\nNome'.ljust(30), 'Idade'.rjust(30))
    print('-'*60)
    for palavra in texto:
        palavra = palavra.split(';')
        nome = palavra[0]
        idade = palavra[-1]
        print(nome.ljust(30), idade.rjust(29))
    print('-'*60)
    opc()

title()
opc()
