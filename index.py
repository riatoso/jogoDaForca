# MODULO PRINCIPAL
# -*- encoding: utf-8 -*-
# JOGO DA FORCA VERSAO 1.0

from gerador.palavra import gera
from informacoes.informa import informacoes_palavra
from jogo.inicia import confere, forca

# VARIAVEIS GLOBAL
if __name__ == "__main__":
    palavra_gerada = gera() # PALAVRA ESCOLHIDA
    lista_tracos = confere(palavra_gerada) # LISTA COM TRAÇOS
    print(informacoes_palavra(palavra_gerada)) # INFORMAÇÕES RELEVANTES A PALAVRA
    forca(palavra_gerada, lista_tracos)

