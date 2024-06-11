import json
import os.path
import cryptocode
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ler_arquivo(arquivo):
    with open('arquivostexto/' + arquivo + '.txt', 'r', encoding='utf-8') as arquivooo:
        ler_arquivo = arquivooo.read()
    return print(ler_arquivo) 

def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding='utf-8') as arquivoo:
            dados = json.load(arquivoo)
        return dados
    else:
        return {}
    
def armazenar_dados(arquivo, conteudo):
    with open(arquivo, 'w', encoding='utf-8') as arquivoo:
        json.dump(conteudo, arquivoo)

def criptografar(senha, chave):
    return cryptocode.encrypt(senha, chave)

chave_login = '1234'
chave_gerenc = '4321'
def descriptografar(senha, chave):
    return cryptocode.decrypt(senha, chave)

def load(texto):
    clear()
    print(texto)
    time.sleep(1.25)