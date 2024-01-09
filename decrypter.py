import os
import pyaes

## abrir o arquivo criptografado

file_name = "teste.txt.textoperdido"
file = open(file_name, "rb") ##rb significa ler o arquivo (read)
file_data = file.read()
file.close()

## chave para descriptografia

key = b"segredossecretos"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado

os.remove(file_name)

## criar novo arquivo

new_file = "teste.txt"
new_file = open(f'{new_file}', "wb") ##wb significa escrever o arquivo (write)
new_file.write(decrypt_data)
new_file.close()
