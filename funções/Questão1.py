#Função da questão: f(x) 
def cp_calculo(ataque, defesa, stamina, cp_multiplicador):
   return (ataque * (defesa**0.5) * (stamina**0.5) * (cp_multiplicador**2)) / 10
#Função do campeão O.O
def campeao(pokedex, cps, vencedor):
    maior_cp = -1
    pokemon_vencedor = ""

    for i in range(len(pokedex)):
        nome = pokedex[i]
        cp = cps[i]
        if cp > maior_cp:
            maior_cp = cp
            pokemon_vencedor = nome
        elif cp == maior_cp and len(nome) > len(pokemon_vencedor):
            pokemon_vencedor = nome
    

    vencedor[0] = pokemon_vencedor
    vencedor[1] = maior_cp
#Veremos se está na dex
pokedex = []
cps = []
def principal():
    finalizar = False

    while not finalizar:
        nome_pokemon = input()  
        if nome_pokemon == "Fim":
            finalizar = True
        elif nome_pokemon in pokedex:
            print("Opa, esse Pokémon já foi analisado.")
        else:
            pokedex.append(nome_pokemon)
            ataque = int(input())
            defesa = int(input())
            stamina = int(input())
            cp_multi = float(input())

            cp_maximo = cp_calculo(ataque, defesa, stamina, cp_multi)
            cps.append(cp_maximo)
            print("Pokémon computado com sucesso.")
            
principal()
#É notório o registro do vencedor
if len(pokedex) > 0:
    vencedor = ["", -1]
    campeao(pokedex, cps, vencedor)
    pokemon_vencedor, maior_cp = vencedor
    maior_cp_dado = f"{maior_cp:.2f}"
    #ENCONTRAMOS NOSSO MAIN <3
    if cps.count(maior_cp) > 1:
        print(f"Foi uma análise difícil, mas o Pokémon vencedor com maior CP é: {pokemon_vencedor}, com CP máximo de {maior_cp_dado}")
    #Encontramos um carinha show.
    else:
        print(f"O Pokémon com o maior CP na região de Kanto é: {pokemon_vencedor}, com CP máximo de {maior_cp_dado}")





