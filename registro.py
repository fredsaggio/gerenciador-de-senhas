from arquivos_load import *

def menu_registro(contas):
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

        # Criptografando a senha do usuário
        registrar_senha = criptografar(registrar_senha, chave_login)
        
        print('Criando conta...')
        dados = {registrar_usuario: {'Senha': registrar_senha}} 
        contas.update(dados)
        time.sleep(1.25)

        clear()
        print('Nome de usuário e senha salvos!')
        armazenar_dados('dados/dados.json', contas)
        time.sleep(0.5)
        print('Voltando ao menu principal...')
        time.sleep(1.25)
        break

