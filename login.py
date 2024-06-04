import time
from arquivos_load import clear
from menu import menu_gerenciador

# Função para o menu de login
def menu_login(contas):
    clear()
    print('Direcionando ao login...')
    time.sleep(1.25)
    
    while True:
        clear()
        usuario = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')
                    
        if usuario in contas and contas[usuario]['Senha'] == senha:
            print('Você está logado, redirecionando para o gerenciador...')
            time.sleep(1.25)
            clear()
            menu_gerenciador(contas, usuario)
            break
        else:
            print('E-mail ou senha incorretos.')
            time.sleep(1)
            clear()
            while True:
                opcao = input('Deseja tentar novamente? [s/n]')
                if opcao == 's':
                    break
                elif opcao == 'n':
                    print('Voltando ao menu principal...')
                    time.sleep(1.25)
                    break
                else:
                    print('Valor inválido.')
                    time.sleep(1.25)
                    clear()
            if opcao == 'n':
                break