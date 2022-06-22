import os
import time

def limpa_Tela():
    os.system("cls")

def dormir():
    time.sleep(2)

def registro():
    try:
        arquivo = open("Registro de Login.txt", "r")
        conteudo = arquivo.read()
        arquivo.close()
        return conteudo
    except:
        arquivo = open("Registro de Login.txt", "w")
        arquivo.close()
        return ""
