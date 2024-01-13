import os
import pyaes
from dotenv import load_dotenv


## carregar as variáveis de ambiente 
load_dotenv()


## abrir o arquivo a ser criptografado
file_name = "dados_importantes.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = os.getenv("key")
aes = pyaes.AESModeOfOperationCTR(key.encode())

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".cripto"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
