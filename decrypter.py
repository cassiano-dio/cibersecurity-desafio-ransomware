import os
import pyaes
from dotenv import load_dotenv


## carregar as variáveis de ambiente 
load_dotenv()

## abrir o arquivo criptografado
file_name = "dados_importantes.txt.cripto"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = os.getenv("key")
aes = pyaes.AESModeOfOperationCTR(key.encode())
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "dados_importantes.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
