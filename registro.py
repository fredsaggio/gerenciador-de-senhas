import time
from arquivos_load import armazenarDados, clear

def atualizarDados(contas):
    while True:
        clear()
        registrar_usuario = input('Digite um nome de usuário para registro: ')

        if registrar_usuario in contas: 
            print('Este nome de usuário já existe.')
            time.sleep(1.25)
            continue

        if len(registrar_usuario) < 5:
            print('Seu nome de usuário deve conter no mínimo 5 caracteres.')
            time.sleep(1.25)
            continue

        registrar_senha = input('Digite uma senha para registro: ')

        if len(registrar_senha) < 5:
            print('Sua senha deve conter no mínimo 5 caracteres.')
            time.sleep(1.25)
            continue
        
        print('Criando conta...')
        dados = {registrar_usuario: {'Senha': registrar_senha}} 
        contas.update(dados)
        time.sleep(1.25)

        clear()
        print('Nome de usuário e senha salvos!')
        armazenarDados('dados/dados.json', contas)
        time.sleep(0.5)
        print('Voltando ao menu principal...')
        time.sleep(1.25)
        break



# Função para o menu de registro de usuário
def menu_registro(contas):
    atualizarDados(contas)

    # conta = {nome: {senha: 'senha', site: {nome: senha, nome2: senha2}}}