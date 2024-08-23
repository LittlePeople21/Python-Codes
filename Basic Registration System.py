from time import sleep

def title():
    print('-'*80)
    print('BANCO DEV'.center(80))
    print('-'*80)

def opc():
    opcc = int(input('Bem Vindo ao banco DEV, o que você gostaria hoje?\n1. Cadastrar\n2. Visualizar cadastros\n3. Excluir cadastros\n4. Criar arquivo de cadastros\n5. Encerrar programa\nR:'))
    if opcc == 1:
        cadastrar()
    if opcc == 2:
        visualizar()
    if opcc == 3:
        opcao = str(int('\nVocê tem certeza que quer excluir os cadastros? [Y/N]\nR: '))
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
        return 0

def cadastrar():
    opcqt = int(input('\nQuantas pessoas você deseja cadastrar?\nR: '))
    for qt in range(0, opcqt):
        x = str(input('Nome: '))
        y = str(input('Idade: '))
        with open('cadastros.txt', 'a') as arquivo:
            arquivo.write(x)
            arquivo.write(';')
            arquivo.write(y)
            arquivo.write(':')
        print('Cadastrado!\n')
    print(f'Feito! Obrigado pelos {opcqt} cadastro(s)!')
    opc()

def visualizar():
    with open('cadastros.txt', 'r') as arquivo:
        texto = arquivo.read()
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