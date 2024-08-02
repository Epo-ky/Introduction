# Venda dos melhores
art_semana1 = {
    "Priscila Senna": {"discos_vendidos": 40, "fortuna": 10000, "lucro": 800},
    "Eduarda": {"discos_vendidos": 60, "fortuna": 9990, "lucro": 1200},
    "Academia da Berlinda": {"discos_vendidos": 30, "fortuna": 9995, "lucro": 600},
    "Martins": {"discos_vendidos": 25, "fortuna": 9970, "lucro": 500},
    "Igor de Carvalho": {"discos_vendidos": 25, "fortuna": 9965, "lucro": 500},
}

# Calculo dos ricos
def calculo(discos_vendidos):
    if discos_vendidos == 1:
        return 20 * discos_vendidos
    elif 2 <= discos_vendidos <= 3:
        return 20 * discos_vendidos * 0.98
    elif 4 <= discos_vendidos <= 5:
        return 20 * discos_vendidos * 0.95
    elif discos_vendidos >= 6:
        return 20 * discos_vendidos * 0.93

# Entrada e saida de veiculos por favor estacione em outro lugar :))
N = int(input())

# eita como diciona ( palavra que inventei para ação de dicionario)
art_semana2 = {}
novos_artistas = {}
ordem_entrada = []

# Altas vendas hein 
for _ in range(N):
    entrada = input().split(" - ")
    artista = entrada[0]
    discos_vendidos = int(entrada[1])

    if artista in art_semana2:
        art_semana2[artista]["discos_vendidos"] += discos_vendidos
    else:
        art_semana2[artista] = {"discos_vendidos": discos_vendidos}

    if artista not in art_semana1:
        novos_artistas[artista] = discos_vendidos
    
    # Ordem, por que tava tudo bagunçado e aqui né varzea não, ou talvez seja :P
    ordem_entrada.append(artista)

# Calculo que espero que de certo, ja tem criança chorando aqui já, vulgo eu.
aumento_lucro = {}
houve_aumento = False
for artista, dados in art_semana1.items():
    if artista in art_semana2:
        discos_semana2 = art_semana2[artista]["discos_vendidos"]
        lucro_semana2 = calculo(discos_semana2)

        lucro_semana1 = dados["lucro"]
        aumento_porcentual = lucro_semana2 * 100 / 10000
        aumento_lucro[artista] = aumento_porcentual

        if aumento_porcentual > 0:
            houve_aumento = True

        nova_fortuna = dados["fortuna"] + lucro_semana2
        art_semana1[artista]["nova_fortuna"] = nova_fortuna
    else:
        art_semana1[artista]["nova_fortuna"] = dados["fortuna"]

# novos artistas do meu primo
for artista in novos_artistas:
    nova_fortuna = calculo(novos_artistas[artista])
    art_semana1[artista] = {"discos_vendidos": novos_artistas[artista], "fortuna": 0, "lucro": 0, "nova_fortuna": nova_fortuna}

# SAI TODO MUNDO, SAI TODO MUNDO, COMPRA INGRESSO DE NOVO VOLTAAAAAAAA.
if houve_aumento:
    print("Estes artistas obtiveram aumento do lucro em relação à primeira semana:")
    for artista in ordem_entrada:
        if artista in aumento_lucro:
            print(f"{artista} - Lucro em relação à primeira semana: {aumento_lucro[artista]:.2f}%")
else:
    print("Os artistas da primeira semana não tiveram aumento do lucro na segunda semana!")

print("\nEsta é a fortuna atual dos artistas considerados:")
for artista in art_semana1:
    print(f"{artista}: R$ {art_semana1[artista]['nova_fortuna']:.2f}")

if novos_artistas:
    print("\nNa semana 2 tivemos vendas de novos artistas no mercado:")
    for artista in novos_artistas:
        print(f"{artista} - Discos vendidos: {novos_artistas[artista]}")
else:
    print("\nNa semana 2 não tivemos vendas de novos artistas no mercado!")
