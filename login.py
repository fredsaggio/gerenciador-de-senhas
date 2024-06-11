import time
from arquivos_load import *  
from menu import menu_gerenciador

# Menu do login
def menu_login(contas):
    clear() 
    print('Direcionando ao login...')
    time.sleep(1.25) 
    
    while True:  
        clear() 
        usuario = input('Digite seu nome de usuário: ')   
        senha = input('Digite sua senha: ')  

        if usuario in contas:
            # Descriptografar a senha para o login
            senha_decrypt = descriptografar(contas[usuario]['Senha'], chave_login)
        
        # Verifica se o usuário e a senha estão corretos
        if usuario in contas and senha_decrypt == senha:
            print('Você está logado, redirecionando para o gerenciador...')
            time.sleep(1.25)  
            clear()  
            menu_gerenciador(contas, usuario)  # Chama o menu do gerenciador de senhas
            break  
        else:
            print('E-mail ou senha incorretos.')
            time.sleep(1)  
            clear()  
            while True:
                opcao = input('Deseja tentar novamente? [s/n]').strip().lower()
                if opcao in ['s', 'sim', 'si', 'y', 'yes']:
                    break  
                elif opcao in ['n', 'não', 'no']:
                    print('Voltando ao menu principal...')
                    time.sleep(1.25)  
                    break  
                else:
                    print('Valor inválido.')    
                    time.sleep(1.25)  
                    clear() 
            if opcao == 'n':
                break 