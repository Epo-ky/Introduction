#CESAAAAAAAAAAR, dados da questão
def decifrar_nome(nome_codificado):
    nome_decifrado = ""
    i = 0
    
    while i < len(nome_codificado) and not nome_codificado[i].isalpha():
        i += 1
    
    while i < len(nome_codificado):
        letra = nome_codificado[i]
        if letra.isalpha():
            nova_letra = chr((ord(letra.lower()) - 97 - 3) % 26 + 97)
            if letra.isupper():
                nome_decifrado += nova_letra.upper()
            else:
                nome_decifrado += nova_letra
        else:
            nome_decifrado += letra
        
        i += 1
    
    nome_decifrado = nome_decifrado.rstrip()
    
    return nome_decifrado

# base de dados só as melhores
base_de_dados = {
    "sweetener": {
        "no tears left to cry": 0,
        "the light is coming": 0,
        "better off": 0,
        "everytime": 0
    },
    "thank u, next": {
        "NASA": 0,
        "thank u, next": 0,
        "break up with your girlfriend, i'm bored": 0,
        "bad idea": 0
    },
    "Positions": {
        "motive": 0,
        "safety net": 0,
        "nasty": 0,
        "pov": 0
    },
    "eternal sunshine": {
        "yes, and?": 0,
        "eternal sunshine": 0,
        "the boy is mine": 0,
        "we can't be friends": 0
    }
}

# ponto, ponto ponto
limite = int(input())
albuns_pontuacao = {album: 0 for album in base_de_dados}
# fé em deus que eu não aguento mais
nivel = False

try:
    entrada = input()
except EOFError:
    entrada = "FIM"

while entrada != "FIM" and not nivel:
    nome_codificado, nivel_yeahs = entrada.split(" - ")
    nivel_yeahs = int(nivel_yeahs)
    
    nome_decifrado = decifrar_nome(nome_codificado)
    
    encontrada = False
    for album, musicas in base_de_dados.items():
        if nome_decifrado in musicas:
            encontrada = True
            musicas[nome_decifrado] += nivel_yeahs
            albuns_pontuacao[album] += nivel_yeahs
            
            print(f"O nome da música decifrada é: {nome_decifrado}")
            print(f"Ótimo! A música está na discografia da nossa base de dados!")
            print(f"O album da música decifrada é {album}")
            
            if nivel_yeahs <= 5:
                print("A diva do pop não se empolgou nessa e decepcionou os arianators.")
            elif 5 < nivel_yeahs < 10:
                print("Ariana fez o dever de casa e entregou uma música na média para os seus fãs.")
            else:
                print("AVISA QUE ESSA JÁ É HIT NOS CHARTS!")
            if albuns_pontuacao[album] >= limite:
                print(f'Atenção! O limite de pontuação foi atingido pelo álbum {album}!')
                nivel = True
    
    if not encontrada:
        print(f"O nome da música decifrada é: {nome_decifrado}")
        print("Poxa, essa música não está na discografia da base do nosso estúdio!")
        
    
    try:
        entrada = input()
    except EOFError:
        entrada = "FIM"

print("Fim da análise!\n")

# checando a pontuação, se tiver mais pontos que o fluminense, tudo certo.
maior_pontuacao = 0
album_maior_pontuacao = ""
musica_melhor_pontuada = ""
pontos_melhor_musica = 0

for album, musicas in base_de_dados.items():
    total_pontos = sum(musicas.values())
    if total_pontos > maior_pontuacao:
        maior_pontuacao = total_pontos
        album_maior_pontuacao = album
        
        for musica, pontos in musicas.items():
            if pontos > pontos_melhor_musica:
                pontos_melhor_musica = pontos
                musica_melhor_pontuada = musica

print(f"O álbum da estrela Ariana Grande com a maior pontuação foi {album_maior_pontuacao}, com um total de {maior_pontuacao} pontos!")
print(f"Entre todas as faixas desse álbum, a melhor pontuada foi {musica_melhor_pontuada}, que obteve {pontos_melhor_musica} pontos")
