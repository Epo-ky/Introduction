# Só os melhores, por que o pior ta eu, dados da questão:
artistas_de_renome = {
    "João Gomes": "Parabéns, João Gomes, o novo fenômeno da música pernambucana!",
    "Zé Vaqueiro": "Zé Vaqueiro, o astro do forró, agora brilha como o rei da música pernambucana!",
    "Raphaela Santos": "Raphaela Santos, a voz marcante, agora é a rainha da música pernambucana!",
    "Alceu Valença": "Alceu Valença, o ícone da MPB, agora é o gigante da música pernambucana!",
    "Priscila Senna": "Priscila Senna, a rainha da sofrência, é a mais nova estrela da música pernambucana!",
}

# Entrada das cidades, faltou Moreno - Pernambuco
N = int(input())

# Cartão de memoria para guardar os dados
cidades = []
todas_visu = {"João Gomes":[], "Zé Vaqueiro":[], "Raphaela Santos":[], "Alceu Valença":[], "Priscila Senna":[]}
# Laço das cidades
for _ in range(N):
    cidade = {}
    
    
    nome_cidade = input()
    ano_fundada = int(input())
    
    cidade["nome"] = nome_cidade
    cidade["ano_fundada"] = ano_fundada
    
    # top 3
    top_artista = []
    for i in range(3):
        entrada_artista = input().split(" - ")
        nome_artista = entrada_artista[0]
        musica_artista = entrada_artista[1]
        visualizacao = int(entrada_artista[2])
        
        top_artista.append({
            nome_artista:
            {"musica": musica_artista,
            "visualizacoes": visualizacao}
        })
        todas_visu[nome_artista].append(visualizacao)
        
    
    cidade["top_artista"] = top_artista
    cidades.append(cidade)
    

# Informações das variaveis
artista_vencedor = ""
musica_vencedor = ""
numero_visualizacoes = 0
pontos_cantores = {"João Gomes":0, "Zé Vaqueiro":0, "Raphaela Santos":0, "Alceu Valença":0, "Priscila Senna":0}
# Laço da minha tristeza, das cidades*
for cidade in cidades:
    top = cidade["top_artista"]
    
    for i in range(len(top)):
        nome_artista = list(top[i].keys())[0]  # Obter o nome do artista
        visualizacao = top[i][nome_artista]["visualizacoes"]
        
        if i == 0:
            pontos_cantores[nome_artista] += cidade["ano_fundada"] + visualizacao

        elif i == 1:
            pontos_cantores[nome_artista] += cidade["ano_fundada"] // 2 + visualizacao
        elif i == 2:
            pontos_cantores[nome_artista] += cidade["ano_fundada"] // 3 + visualizacao
        else:
            pontuacao = 0
melhor_pontuacao = 0
for j in pontos_cantores: 
            if melhor_pontuacao < pontos_cantores[j]:
                    melhor_pontuacao = pontos_cantores[j]
                    for cidade in cidades:
                        top = cidade["top_artista"]
                        for art in top:
                            if j in art:
                                if art[j]["visualizacoes"] > numero_visualizacoes:
                                    artista_vencedor = j
                                    musica_vencedor = art[j]["musica"]
                                    numero_visualizacoes = art[j]["visualizacoes"]
            

# Se deus quiser sai certo agora:
for cidade in cidades:
    nome_cidade = cidade["nome"]
    if nome_cidade == "Recife":
        print("A veneza brasileira foi consultada nesta pesquisa!")
    elif nome_cidade == "Olinda":
        print("Uma honra ver que a primeira capital pernambucana foi consultada!")
    elif nome_cidade == "Petrolina":
        print("Ansioso para descobrir a opinião dos petrolinenses!")

# Deve funcionar
anuncio = ""
if artista_vencedor in artistas_de_renome:
    anuncio = artistas_de_renome[artista_vencedor]

# PAN PAN PAN PAN PAN, PLANTÃO
if anuncio:
    print(anuncio)

# Mensagem final :))
print(f"O fenômeno é {artista_vencedor}, que canta a música {musica_vencedor}, já contando com mais de {numero_visualizacoes} milhões de visualizações na internet.")
