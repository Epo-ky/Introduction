#quero mais não, quer dizer dados da questão:
nome_ouvinte = input()
quantidade_musicas = int(input())

musica_mais_tocada = ""
quantidade_musica_mais_tocada = 0

musica_menos_tocada = ""
quantidade_musica_menos_tocada = float("inf")

#playlist mais dificil da minha vida
for musica in range(quantidade_musicas):

    musica = input()
    quantidade_streams = int(input())

    if quantidade_streams > quantidade_musica_mais_tocada:
        musica_mais_tocada = musica
        quantidade_musica_mais_tocada = quantidade_streams
    if quantidade_streams < quantidade_musica_menos_tocada:
        musica_menos_tocada = musica
        quantidade_musica_menos_tocada = quantidade_streams

#ninguem ageunta mais kanye west
if quantidade_musicas == 0:
    print(f"{nome_ouvinte} é team Taylor e não ouviu Kanye West")
#uma ainda presta
elif quantidade_musicas == 1:
    print(f"A única música que {nome_ouvinte} ouviu foi {musica} com {quantidade_streams} streams")
#foi so ela tambem
elif quantidade_streams == quantidade_musica_mais_tocada and quantidade_streams == quantidade_musica_menos_tocada:
    print(f"A música que {nome_ouvinte} mais ouviu foi {musica_mais_tocada} com {quantidade_musica_mais_tocada} streams")
#ele gossssta
elif quantidade_musicas >= 2:
    print(f"A música que {nome_ouvinte} mais ouviu foi {musica_mais_tocada} com {quantidade_musica_mais_tocada} streams")
    print(f"A música que {nome_ouvinte} menos ouviu foi {musica_menos_tocada} com {quantidade_musica_menos_tocada} streams")










