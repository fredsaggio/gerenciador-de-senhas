import json
import os.path


def clear():
    os.system('cls')

def lerArquivo(arquivo):
    with open('arquivostexto/' + arquivo + '.txt', 'r', encoding='utf-8') as arquivooo:
        lerArquivo = arquivooo.read()
    return print(lerArquivo) 

def carregarDados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding='utf-8') as arquivoo:
            dados = json.load(arquivoo)
        return dados
    else:
        print("Arquivo não encontrado. Iniciando com um novo dicionário vazio.")
        return {}
    
def armazenarDados(arquivo, conteudo):
    with open(arquivo, 'w', encoding='utf-8') as arquivoo:
        json.dump(conteudo, arquivoo)