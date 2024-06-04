import time
from login import menu_login
from registro import menu_registro
from arquivos_load import carregarDados, clear, lerArquivo


contas = carregarDados('dados/dados.json')
def main(): 
    
    while True:
        clear()
        lerArquivo('opcoes')
        opcao = input('\nEscolha uma das opções acima: ')

        if not opcao.isnumeric() or int(opcao) not in range(1, 4):
            print('\nvalor inválido')
            time.sleep(1.5)

        # Login no sistema
        elif opcao == '1':
            menu_login(contas)
            
        # Registrando no sistema
        elif opcao == '2':
            menu_registro(contas)
            
        else:
            while True:
                clear()
                certeza = input('Tem certeza que deseja sair do programa? [s/n]: ')

                if certeza == 's':
                    print('Programa finalizado, até a próxima!')
                    time.sleep(1.25)
                    break
                elif certeza == 'n':
                    print('Voltando ao menu principal...')
                    time.sleep(1.25)
                    break
                else:
                    print('Valor inválido.')
                    time.sleep(1.25)
            if certeza == 's':
                break

main()