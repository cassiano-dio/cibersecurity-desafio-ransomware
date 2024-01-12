import os
import pyaes
from tkinter import messagebox
from configparser import ConfigParser

def catch_Key():
    config = ConfigParser()
    config.read('config.ini')
    return config.get('configurações','chave_criptografia')

file_name = "teste.txt.ransomwaretroll"

try:
    with open(file_name, "rb") as file:
        file_data = file.read()

    Chave = catch_Key()
    aes = pyaes.AESModeOfOperationCTR()
    decrypt_data = aes.decrypt(file_data)

    os.remove(file_name)

    new_file_name = "teste.txt"
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

    messagebox.showinfo("Descriptografia concluída com sucesso!")

except Exception as e:
    messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
