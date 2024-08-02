#Evando cds o moral do CIN, compre 1 é tres, 2 é cinco, apenas hoje, DADOS DA QUESTÃO
def entrada_artistas():
    artista_1 = input()
    artista_2 = input()
    print(f"E os artistas de hoje são {artista_1} e {artista_2}!")
    return artista_1, artista_2

#Enquanto houver discos eu tocarei, não importa quem seja meu adverssario
def discoteca():
    repertorio = {}
    continuar = True
    while continuar:
        disco = input()
        if disco.lower() == "acabou" or disco.upper() == "FIM":
            continuar = False
        else:
            preco_valido = False
            while not preco_valido:
                preco_str = input()
                if preco_str.replace('.', '', 1).isdigit():
                    preco = float(preco_str)
                    preco_valido = True
                    repertorio[disco] = preco
                else:
                    print("Preço inválido. Tente novamente.")
    return repertorio

#repertorio novo no aralto minha gente: calculo das vendas
def simulacao(artista_1, repertorio_1, artista_2, repertorio_2):
    print("-----COMEÇO DO EXPEDIENTE!-----")
    disco_total = 0
    receita_total = 0
    vendas_artista1 = 0
    vendas_artista2 = 0
    receita_artista1 = 0
    receita_artista2 = 0
    continuar = True
    
    while continuar:
        disco_vendido = input()
        if disco_vendido.upper() == "FIM":
            continuar = False
        else:
            if disco_vendido in repertorio_1:
                vendas_artista1 += 1
                receita_artista1 += repertorio_1[disco_vendido]
                print(f"{disco_vendido} vendido")
            elif disco_vendido in repertorio_2:
                vendas_artista2 += 1
                receita_artista2 += repertorio_2[disco_vendido]
                print(f"{disco_vendido} vendido")
            else:
                print("Parece que não temos esse disco...")
            
            disco_total += 1
            diferenca_vendas = abs(vendas_artista1 - vendas_artista2)
            if diferenca_vendas % 3 == 0 and diferenca_vendas != 0:
                if vendas_artista1 > vendas_artista2:
                    for disco in repertorio_1:
                        repertorio_1[disco] += 4
                    for disco in repertorio_2:
                        repertorio_2[disco] -= 4
                    print(f"A diferença está ficando muito grande! AUMENTA R$4 DE {artista_1.upper()} E ABAIXA R$4 DE {artista_2.upper()}!")
                else:
                    for disco in repertorio_2:
                        repertorio_2[disco] += 4
                    for disco in repertorio_1:
                        repertorio_1[disco] -= 4
                    print(f"A diferença está ficando muito grande! AUMENTA R$4 DE {artista_2.upper()} E ABAIXA R$4 DE {artista_1.upper()}!")
    
    receita_total = receita_artista1 + receita_artista2
    print("-----FIM DO EXPEDIENTE!-----")
    
    # Exibindo a receita total de acordo com a condição especificada
    if receita_total == 0:
        print(f"O total de receita gerado foi de {int(receita_total)} e foram vendidos {disco_total} discos.")
    else:
        print(f"O total de receita gerado foi de {receita_total:.1f} e foram vendidos {disco_total} discos.")
    
    # Avaliando qual artista gerou mais receita
    if vendas_artista1 == vendas_artista2:
        if vendas_artista1 == 0:
            print("Que tristeza! Só artista péssimo...")
        else:
            print("Difícil de escolher o melhor!")
    else:
        if vendas_artista1 > vendas_artista2:
            ganhador = artista_1
            dinheiro_ganhador = receita_artista1
            discos_vendidos = vendas_artista1
        else:
            ganhador = artista_2
            dinheiro_ganhador = receita_artista2
            discos_vendidos = vendas_artista2
        
        print(f"O artista que mais gerou dinheiro para a loja foi {ganhador}, acumulando uma receita de {dinheiro_ganhador:.1f} e vendendo {discos_vendidos} discos.")

#Boas vindas as funções, amém.
print("Bem-vindo(a) à 'Sergio Bieber's Disco Shop'!")

# Chamada das funções principais
artista_1, artista_2 = entrada_artistas()

repertorio_1 = discoteca()
repertorio_2 = discoteca()

simulacao(artista_1, repertorio_1, artista_2, repertorio_2)
