import time
from arquivos_load import armazenarDados, lerArquivo, clear, carregarDados

# Função para o menu do gerenciador
def menu_gerenciador(contas):
    while True:
        clear()
        while True:
            clear()
            lerArquivo('opcoes2')
            escolher_opcao = input('\nEscolha uma das opções acima: ')

            if not escolher_opcao.isnumeric():
                print('Valor inválido.')
                time.sleep(1)
                continue

            if int(escolher_opcao) < 1 or int(escolher_opcao) > 4:
                print('Valor inválido, apenas números dentre as opções.')
                time.sleep(1)
                continue

            if escolher_opcao == '4':
                clear()
                print('Saindo da conta e voltando ao menu principal...')
                time.sleep(1.25)
                break

            print('Redirecionando...')
            time.sleep(1.25)
            clear()
            if escolher_opcao == '1':
                if senhas == {}:
                    print('Você ainda não possui senhas registradas em sua conta.')
                    time.sleep(1.25)
                    continue
                else:
                    print('Suas senhas:')
                    time.sleep(0.5)

                    for i in contas['Senhas']:
                        print(f"{contas['Senhas']}: {contas['Senhas'][i]}")
                    time.sleep(3)
                    continue
            if escolher_opcao == '2':
                dispositivo = input('Título para a senha: ')
                senha = input('Digite a senha para armazená-la: ')
                senhas[dispositivo]= senha
                contas['Senhas'] = senhas

                clear()

                print('Armazenando senha...')
                time.sleep(1.25)

                clear()

                print('Senha armazenada com sucesso!')
                armazenarDados('dados/senhas.json', senhas)
                continue
            if escolher_opcao == '3':
                print('Advinha... Desenvolvimento!!')
                time.sleep(1.25)
                break
        print("Menu do Gerenciador")
        break

if __name__ == "__main__":
    from login import menu_login
    menu_login()