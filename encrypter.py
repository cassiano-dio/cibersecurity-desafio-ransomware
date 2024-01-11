import os
import pyaes

## Abrir o arquivo criptografado

file_name = "test.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Chave para descriptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remover o arquivo criptografado

os.remove(file_name)

## Criar o arquivo descriptografado

new_file = "test.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
