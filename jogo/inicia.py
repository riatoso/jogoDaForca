# MODULO DE FUNÇOES PRINCIPAIS
# -*- coding: utf-8 -*-

# CONFERE A PALAVRA
def confere(palavra):
    contraprova = []
    for num in range(len(palavra)):
        contraprova.append("-")
    return  contraprova

# FUNÇÃO PRINCIPAL
def forca(p_escolhida, l_tracos):
    lista_preenchida = l_tracos # LISTA QUE SAI
    palavra_escolhida = p_escolhida # PALAVRA ESCOLHIDA
    tentativas = 0
    secreta = ""
    tamanho = int(len(palavra_escolhida))
    while tentativas < 5:
        letra = input("Digite a letra da palavra: ").upper()
        if letra in palavra_escolhida and letra not in lista_preenchida:
            print("SIM EXISTE A LETRA")
            for num, letter in zip(range(tamanho), palavra_escolhida):
                if letter == letra:
                    lista_preenchida.pop(num)
                    lista_preenchida.insert(num, letter)
                    if lista_preenchida.count("-") == 0:
                        for i in lista_preenchida:
                            secreta = secreta + i
                        print(f"Voce achou a palavra: {secreta}")
                        tentativas = 5
                        break
            print(f"Sua palavra: {lista_preenchida}")
        elif letra in palavra_escolhida and letra in lista_preenchida:
            print("lETRA JA ESCOLHIDA.")
            continue
        else:
            print(f"Uma tentativa , e  não econtrou a letra {letra}")
            print(f"Faltam {4 - tentativas} tentativas.")
            tentativas += 1
            if tentativas == 5:
                print("INFELIZMENTE VOCE NÃO ACERTOU, SAINDO DO JOGO")