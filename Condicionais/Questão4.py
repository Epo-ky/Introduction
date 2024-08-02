#Dados Da Questão
pontuacaolewis = int(input()) 
colocacaolewis = int(input())
pontuacaomax = int(input())
colocacaomax = int(input())
pontuacaovaltteri = int(input())
colocacaovaltteri = int(input())

#Anuncio dos melhores

#Lewis pontos
if colocacaolewis <= 10:
    pontuacaolewis += 5 
#Max pontos 
if colocacaomax <= 10:
    pontuacaomax += 5
#valtteri pontos
if colocacaovaltteri <= 10:
    pontuacaovaltteri += 5
#resolução geral

#Mãe do Lewis MVP
if pontuacaolewis == pontuacaomax == pontuacaovaltteri:
    print(f"Lewis Hamilton ganhou a competição com {pontuacaolewis} pontos!")
#Grande mamãe do Lewis
if pontuacaolewis == pontuacaomax > pontuacaovaltteri:
    print (f"Lewis Hamilton ganhou a competição com {pontuacaolewis} pontos!")
#Pai do Max fez a boa
if pontuacaomax == pontuacaovaltteri > pontuacaolewis:
    print (f"Max Verstappen ganhou a competição com {pontuacaomax} pontos!")
#Lewis lendario
if pontuacaolewis > pontuacaomax and pontuacaolewis > pontuacaovaltteri:
    print(f"Lewis Hamilton ganhou a competição com {pontuacaolewis} pontos!")
#Max melhor do mundo, não tem como!
if pontuacaomax > pontuacaolewis and pontuacaomax  > pontuacaovaltteri:
    print (f"Max Verstappen ganhou a competição com {pontuacaomax} pontos!")
#Valter ganhou uma pra deus ver.
if pontuacaovaltteri > pontuacaolewis and pontuacaovaltteri > pontuacaomax:
    print (f"Valtteri Bottas ganhou a competição com {pontuacaovaltteri} pontos!")
