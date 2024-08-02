#Meu heroi não usa capa, ele escuta Taylor, DADOS DA QUESTÃO:
num_rodadas = int(input())
competicao_rolando = True
desordem = False
musica = ""
desordem_kanye = 0
desordem_taylor = 0
artista_perdedor1 = ""
artista_perdedor2 = ""
avaliacoes = int
vitoria_taylor = 0 
vitoria_kanye = 0
artista1 = "Kanye West"
artista2 = "Taylor Swift"
num_de_rodada = 0
#Eita como laça
while competicao_rolando and not desordem and num_de_rodada < num_rodadas:
    print(f"{num_de_rodada + 1}° RODADA:")
    pontuacao_kanye = 0
    nome_musica = input()
    avaliacoes = 3
    for musica in range(avaliacoes):
         avaliacao = input()
         if desordem_kanye >= 5:
            avaliacoes = 0
            avaliacao = ""
         if avaliacao == "boa":
            pontuacao_kanye += 2
         elif avaliacao == "média":
            pontuacao_kanye += 1
         elif avaliacao == "ruim":
            pontuacao_kanye -= 3
         elif avaliacao == "péssima":
             comando = input()
             while comando != "ORDEM":
                if comando != "ORDEM":
                    desordem_kanye += 1 
                comando = input()
#possivel barraco             
    if desordem_kanye >= 5:
         print(f"Os fãs do(a) {artista1} causaram tanta desordem que ele(a) perdeu o prêmio!")
         desordem = True 
    else:
        pontuacao_taylor = 0
        nome_musica = input()
        for musica in range(avaliacoes):
            avaliacao = input()
            if desordem_taylor >= 5:
                avaliacoes = 0
                avaliacao = ""
            if avaliacao == "boa":
                pontuacao_taylor += 2
            elif avaliacao == "média":
                pontuacao_taylor += 1
            elif avaliacao == "ruim":
                pontuacao_taylor -= 3
            elif avaliacao == "péssima":
                comando = input()
                while comando != "ORDEM":
                    if comando != "ORDEM":
                        desordem_taylor += 1 
                    comando = input()
    if desordem_taylor >= 5:
            print(f"Os fãs do(a) {artista2} causaram tanta desordem que ele(a) perdeu o prêmio!")
            desordem = True
  
#BADERNAAAAA DESORDEM, CHUTA A CARA DELEEEEEEEE 
    if competicao_rolando == True:
        if desordem_kanye >= 5:
            competicao_rolando = False
            print(f"O(a) vencedor(a) do Cin Awards é {artista2}, parabéns!")
        elif desordem_taylor >= 5:
            competicao_rolando = False
            print(f"O(a) vencedor(a) do Cin Awards é {artista1}, parabéns!")
#Fino Señores, classe apenas votação
    if not desordem and competicao_rolando == True:
        if pontuacao_kanye > pontuacao_taylor:
            print(f"O(a) vencedor(a) da {num_de_rodada+1}° rodada foi {artista1}")
            vitoria_kanye += 1
        elif pontuacao_taylor > pontuacao_kanye:
            print(f"O(a) vencedor(a) da {num_de_rodada+1}° rodada foi {artista2}")
            vitoria_taylor += 1
        else:
            print(f"Não houve vencedor na {num_de_rodada+1}° rodada")

#panpanpanpan e o vencedor é:
    if competicao_rolando:
        if vitoria_kanye == 3:
            competicao_rolando = False
        elif vitoria_taylor == 3:
            competicao_rolando = False

        

    num_de_rodada += 1
#ACABOUUUU, GIGANTE, ACABOU, GIGANTE, UMA DAS MAIORES VIRADAS DA HISTÓRIA
if not desordem:
    if vitoria_kanye > vitoria_taylor:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {vitoria_kanye} vitórias, é {artista1}, parabéns!")
    elif vitoria_taylor > vitoria_kanye:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {vitoria_taylor} vitórias, é {artista2}, parabéns!")
    else:
        print("Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!")
