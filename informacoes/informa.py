# INFORMAÇÕES DA PALAVRA
# -*- coding: utf-8 -*-

def informacoes_palavra(pl):
    palavra = pl
    tamanho = len(palavra)
    if palavra == "RICARDO":
        return (f"É um nome proprio com {tamanho} letras.")
    elif palavra == "FERROVIARIA":
        return (f"É um time de futebol com {tamanho} letras.")
    elif palavra == "PERNAMBUCO":
        return (f"É um estado do Brasil com {tamanho} letras")
    elif palavra == "ARARAQUARA":
        return (f"É uma cidade brasileira com {tamanho} letras.")
    else:
        return (f"É um animal com {tamanho} letras")