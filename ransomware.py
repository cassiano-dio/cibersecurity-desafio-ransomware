import pyaes
import io



def encrypt_file(alvo, key):
    # Use an in-memory buffer to store the content
    in_memory_buffer = io.BytesIO()

    # Write the content to the buffer
    in_memory_buffer.write(alvo)

    # Encrypt the content of the in-memory buffer
    in_memory_buffer.seek(0)
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(in_memory_buffer.read())

    new_file_name = "crypted.txt"
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)
        print(f"Encryption completed. New file '{new_file_name}' created.")

def decrypt_file(alvo, key):
    
    in_memory_buffer = io.BytesIO()

    in_memory_buffer.write(alvo)

    in_memory_buffer.seek(0)

    #with open(alvo, "rb") as file:
        #file_data = file.read(alvo)

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(in_memory_buffer.read())

    new_file_name = "decrypted_file.txt"
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)


    print(f"Arquivo descriptografado salvo como {new_file_name}")

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

def opcao_um(alvo,key):
    print("Voce escolheu Criptografar!")
    encrypt_file(alvo, key)

def opcao_dois(alvo,key):
    print("Voce escolheu a Descriptografar!")
    decrypt_file(alvo,key)

def menu(alvo,key):
    while True:
        print("Escolha uma opcao:")
        print("1. Criptografar")
        print("2. Descriptografar")

        escolha = input("Digite o numero da opcao desejada: ")

        if escolha == '1':
            opcao_um(alvo,key)
            break
        elif escolha == '2':
            opcao_dois(alvo,key)
            break
        else:
            print("Opcao invalida. Tente novamente.")

def receber_arquivo():
    while True:
        caminho_do_arquivo = input("Digite o caminho do arquivo: ")
        alvo = carregar_arquivo(caminho_do_arquivo)
        key = b"testeransomwares"

        if alvo is not None:
            print(f"Conteudo do arquivo carregado com sucesso:\n{alvo}")
            menu(alvo,key)
            break
        else:
            print("Falha ao carregar o arquivo.")
            continue

receber_arquivo()
