import os

def nome_programa():
    print("""


    ███████╗░█████╗░████████╗██╗███████╗██╗░░░██╗
    ██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝╚██╗░██╔╝
    █████╗░░███████║░░░██║░░░██║█████╗░░░╚████╔╝░
    ██╔══╝░░██╔══██║░░░██║░░░██║██╔══╝░░░░╚██╔╝░░
    ███████╗██║░░██║░░░██║░░░██║██║░░░░░░░░██║░░░
    ╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░░░░░░░╚═╝░░░

    """)

def opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Aplicação Encerrada!\n')

def escolher_opcao():
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        cadastrar_restaurante = input('Digite o nome do restaurente: ')
    elif opcao == 2:
        print('Listar restaurantes: ')
    elif opcao == 3:
        print('Qual restaurante deseja ativar: ')
    else:
        finalizar_app()

def main():
    nome_programa()
    opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
