import time
from arquivos_load import armazenarDados, lerArquivo, clear, carregarDados
import os.path

def load(texto):
    clear()
    print(texto)
    time.sleep(1.25)

# Função para o menu do gerenciador
def menu_gerenciador(contas, usuario):
    while True:
        cont = 0
        clear()
        lerArquivo('opcoes2')
        escolher_opcao = input('\nEscolha uma das opções acima: ')

        if escolher_opcao == '1':
            load('Redirecionando...')
            for i in contas[usuario]:
                if cont == 0:
                    cont+=1
                    continue
                print('-'*30)
                print(f'Site: {i}\n')
                for x in contas[usuario][i]:
                    print(f'Usuario: {x}\nSenha: {contas[usuario][i][x]}')
            print('-'*30)
            print()
            os.system('pause')

                            
        
        elif escolher_opcao == '2':
            load('Redirecionando...')
            site = input('Digite o nome do site: ')
            usuario_site = input('Digite o nome de usuário do site: ')
            senha_site = input('Digite a senha: ')
            dicionario = {site: {usuario_site: senha_site}}
            contas[usuario].update(dicionario)
            armazenarDados('dados/dados.json', contas)


            clear()

            print('Armazenando senha...')
            time.sleep(1.25)

            clear()

            print('Senha armazenada com sucesso!')  

        elif escolher_opcao == '3':
            load('Redirecionando...')
            clear()
            print('Saindo da conta e voltando ao menu principal...')
            time.sleep(1.25)
            break
        
        else:
            print('Valor inválido')
            time.sleep(1.25)


# print('Redirecionando...')
 #       time.sleep(1.25)
  #      clear()