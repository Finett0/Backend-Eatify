import os

restaurantes = []

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

def opcao_invalida():
    print('Opção Invalida!\n')
    input('Digite qualquer tecla para voltar ao menu')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('Castro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()


def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            print('Listar restaurantes: ')
        elif opcao == 3:
            print('Qual restaurante deseja ativar: ')
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    nome_programa()
    opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

    opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
