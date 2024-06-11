from arquivos_load import *

# Função para o menu do gerenciador
def menu_gerenciador(contas, usuario):

    while True:
        cont = 0
        clear()
        ler_arquivo('opcoes2')  # Texto do menu

        escolher_opcao = input('\nEscolha uma das opções acima: ')

        if escolher_opcao == '1':
            load('Redirecionando...')
            clear()

            # Iterar sobre as contas do usuário
            for i in contas[usuario]:
                # Ignora a primeira chave (senha)
                if cont == 0: 
                    cont+=1
                    continue
                print('-'*30)
                print(f'Site: {i}\n')
                # Iterar sobre os usuários e senhas do site
                for x in contas[usuario][i]:
                    # Descriptografa a senha antes de exibir
                    senha_decrypto = descriptografar(contas[usuario][i][x], chave_gerenc)
                    print(f'Usuario: {x}\nSenha: {senha_decrypto}')

            print('-'*30)
            print()
            os.system('pause')

        elif escolher_opcao == '2':
            load('Redirecionando...')
            site = input('Digite o nome do site: ')
            usuario_site = input('Digite o nome de usuário do site: ')
            senha_site = input('Digite a senha: ')
            senha_site = criptografar(senha_site, chave_gerenc)  # Criptografar a senha antes de armazenar
            dicionario = {site: {usuario_site: senha_site}}
            contas[usuario].update(dicionario)  # Adicionar site, usuário e senha ao dicionário de contas
            armazenar_dados('dados/dados.json', contas)  # Armazenar os dados atualizados no arquivo

            clear()
            print('Armazenando senha...')
            time.sleep(1.25)
            clear()
            print('Senha armazenada com sucesso!')  

        elif escolher_opcao == '3':
            load('Redirecionando...')
            clear()
            load('Saindo da conta e voltando ao menu principal...')
            break  # Sair do loop e retornar ao menu principal
        
        else:
            print('Valor inválido')
            time.sleep(1.25)