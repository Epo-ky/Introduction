#o homem nasce bom, a lista o corrompe, DADOS DA QUESTÃO:
N = input()
votos = 0
votos_kaney = 0
#calculos durante os blocos de votos
while N != "FIM":
    N = int(N)

    if N % 7 == 0 and N % 2 != 0:
        votos_kaney += 20000000
    elif N % 2 == 0 and N % 7 != 0:
        votos_kaney += 10000000
    elif N % 2 != 0 and N % 7 != 0:
        votos += 14000000

    if (votos + votos_kaney) >= 300000000:
        N = "FIM"
    else:
        N = input()
#O homi para presidente
if votos_kaney > 170000000:
    print("O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")
    print(f"Kanye conseguiu ao final da campanha um total de {votos_kaney} votos.")
#Dessa vez não, faz o L
elif votos_kaney < 130000000:
    print("Caramba, não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")
    print(f"Kanye conseguiu ao final da campanha um total de {votos_kaney} votos.")
#Segundo turno é nosso
elif votos_kaney < 170000000 and votos_kaney > 130000000:
    print("A eleição está disputada, vamos ter um segundo turno!")
    print(f"Kanye conseguiu ao final da campanha um total de {votos_kaney} votos.")
    votos = 0
    votos_kaney = 0
    N = input()
    while N != "FIM":
        N = int(N)
        if N % 7 == 0 and N % 2 != 0:
            votos_kaney += 20000000
        elif N % 2 == 0 and N % 7 != 0:
            votos_kaney += 10000000
        elif N % 2 != 0 and N % 7 != 0:
            votos += 14000000

        if (votos + votos_kaney) >= 300000000:
            N = "FIM"
        else:
            N = input()
#falei pow, tudo nosso, kanye amassa demais
    if votos_kaney > 170000000:
        print("Depois de um pleito muito acirrado, O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")
        print(f"Kanye conseguiu ao final da campanha um total de {votos_kaney} votos.")
#Só não mais triste que eu fazendo essa questão
    elif votos_kaney < 170000000:
        print("Caramba, foi uma disputa muito acirrada, mas não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")
        print(f"Kanye conseguiu ao final da campanha um total de {votos_kaney} votos.")
