import os.path
import time
import json

# Função para limpar o console
def clear():
    if os.name == 'posix':  
        return os.system('clear')
    elif os.name == 'nt':   
        return os.system('cls')
    else:
        return None

# Função para ler um arquivo de texto
def lerArquivo(arquivo):
    with open('arquivostexto/' + arquivo + '.txt', 'r', encoding='utf-8') as arquivooo:
        lerArquivo = arquivooo.read()
    return print(lerArquivo)   
    
# Função para carregar os dados de um arquivo JSON
def carregarDados(arquivo):
    try:
        with open(arquivo, "r", encoding='utf-8') as arquivoo:
            dados = json.load(arquivoo)
        return dados
    except FileNotFoundError:
        print("Arquivo não encontrado. Iniciando com um novo dicionário vazio.")
        return {}
    
# Função para armazenar os dados após finalizar o programa
def armazenarDados(arquivo, conteudo):
    with open(arquivo, 'a', encoding='utf-8') as arquivoo:
        json.dump(conteudo, arquivoo)


def main():
    # Carrega os dados dos arquivos JSON
    contas = carregarDados('dados/dados.json')
    senhas = carregarDados('dados/senhas.json')
    
    while True:

        clear()
        lerArquivo('options')


        option = input('\nEscolha uma das opções acima: ')


        if not option.isnumeric() or int(option) not in range(1, 4):
            print('\nvalor inválido')
            time.sleep(1.5)
            continue

        # Login no sistema
        if option == '1':
            clear()
            print('Direcionando ao login...')
            time.sleep(1.25)
            while True:
                clear()
                # Solicita o nome de usuário e senha
                usuario = input('Digite seu nome de usuário: ')
                senha = input('Digite sua senha: ')
                    
                if usuario in contas and contas[usuario] == senha:
                    print('Você está logado, redirecionando para o gerenciador...')
                    time.sleep(1.25)
                    clear()

                    while True:
                        clear()
                        lerArquivo('options2')
                        escolher_opcao = input('\nEscolha uma das opções acima: ')

                        if not escolher_opcao.isnumeric():
                            print('Valor inválido.')
                            time.sleep(1)
                            continue

                        escolher_opcao_int = int(escolher_opcao)

                        if escolher_opcao_int < 1 or escolher_opcao_int > 4:
                            print('Valor inválido, apenas números dentre as opções.')
                            time.sleep(1)
                            continue

                        if escolher_opcao_int == 4:
                            clear()
                            print('Saindo da conta e voltando ao menu principal...')
                            time.sleep(1.25)
                            break

                        print('Redirecionando...')
                        time.sleep(1.25)
                        clear()
                        if escolher_opcao_int == 1:
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
                        if escolher_opcao_int == 2:
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
                        if escolher_opcao_int == 3:
                            print('Advinha... Desenvolvimento!!')
                            time.sleep(1.25)
                            break
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
                            continue
                    if opcao == 'n':
                        break
                    continue
        # Registrando no sistema
        elif option == '2':
            while True:
                clear()

                # Registra um novo usuário
                registrar_usuario = input('Digite um nome de usuário para registro: ')

                if registrar_usuario in contas: 
                    print('Este nome de usuário já existe.')
                    time.sleep(1.25)
                    continue

                if len(registrar_usuario) < 5:
                    print('Seu nome de usuário deve conter no mínimo 5 caracteres.')
                    time.sleep(1.25)
                    continue

                # Registra uma nova senha
                registrar_senha = input('Digite uma senha para registro: ')

                if len(registrar_senha) < 8:
                    print('Sua senha deve conter no mínimo 8 caracteres.')
                    time.sleep(1.25)
                    continue
                
                contas[registrar_usuario] = registrar_senha

                print('Criando conta...')
                armazenarDados('dados/dados.json', contas)
                time.sleep(1.25)

                clear()
                print('Nome de usuário e senha salvos!')
                time.sleep(0.5)
                print('Voltando ao menu principal...')
                time.sleep(1.25)
                break
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
                    continue
            if certeza == 's':
                break
                

main()

