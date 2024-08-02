#Lista e dados da questão:
evolutions = ["Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon", "Glaceon", "Leafeon", "Sylveon"]

#Só os famosos:
agua = ["Misty", "Gary", "Ivy", "Blanche"]
eletrico = ["Ash", "Ritchie", "Surge", "Spark"]
fogo = ["May", "Blaine", "Candela"]
psiquico = ["Agatha", "Sabrina", "Fantina"]
sombrio = ["Jessie", "James", "Giovanni"]
gelo = ["Lorelei", "Dawn"]
planta = ["Max", "Erika", "Tracey", "Mallow"]
fada = ["Whitney"]
#eita olha o alfabeto numeral:
def letra_por_numero(letra):
    return ord(letra) - ord("a") + 1

#nome e idade, ANTERDEGUEMON, 30 anos.
def calculo(nome_treinador, idade):
    soma_geral = 0
    for letra in nome_treinador:
        if "a" <= letra <= "z" or "A" <=letra <= "Z":
            soma_geral += letra_por_numero(letra)        
    resultado = soma_geral * idade
    indice_evolucao = resultado % 8
    return indice_evolucao
#Vamos transicionar os tipos pro nome éeeeeeeeee, Sylveon é o mais fofo e Umbreon o melhor.
def verificacao(nome):
    if nome in agua:
        return "Vaporeon"
    elif nome in eletrico:
        return "Jolteon"
    elif nome in fogo:
        return "Flareon"
    elif nome in psiquico:
        return "Espeon"
    elif nome in sombrio:
        return "Umbreon"
    elif nome in gelo:
        return "Glaceon"
    elif nome in planta:
        return "Leafeon"
    elif nome in fada:
        return "Sylveon"
   
#EVOLUÇÃOOOOOOOOOOOOOOOO
def evolucao():
    quantidade_evolution = int(input())
    
    for _ in range(quantidade_evolution):
        nome_treinador, idade = input().split(" - ")
        nome_treinador = nome_treinador.capitalize()
        idade = int(idade)

        evolucao_especie = verificacao(nome_treinador)
        if evolucao_especie is None:
            indice_evolucao = calculo(nome_treinador, idade)
            evolucao_especie = evolutions[indice_evolucao]

        nome_treinador = nome_treinador.capitalize()
#Parabéns ele vai destruir tudo com hydrobomb
        if evolucao_especie == "Vaporeon":
            print(f"A evolução do Eevee de {nome_treinador} é para Vaporeon, o mestre das águas!")
#Parabéns ele é uma bateria
        elif evolucao_especie == "Jolteon":
            print(f"O Eevee de {nome_treinador} evoluiu para Jolteon, cheio de energia elétrica!")
#Parabéns ele é botafogo campeão desde 1910:
        elif evolucao_especie == "Flareon":
            print(f"O Eevee de {nome_treinador} se transformou em Flareon, dominando o calor do fogo!")
#Parabéns ele é um ESPEÃO que espia a mente alheia:
        elif evolucao_especie == "Espeon":
            print(f"Espeon é a evolução do Eevee de {nome_treinador}, mostrando sua mente brilhante!")
#Parabéns ele é trevoso e a melhor evolução:
        elif evolucao_especie == "Umbreon":
            print(f"A evolução sombria do Eevee de {nome_treinador} é Umbreon, deslizando pelas sombras!")
#Parabéns ele da raio de gelo e insta kill no leafeon
        elif evolucao_especie == "Glaceon":
            print(f"Glaceon é o novo estágio do Eevee de {nome_treinador}, tão frio quanto o gelo!")
#Lamento, perde pra tudo, se duvidar até pra mim.
        elif evolucao_especie == "Leafeon":
            print(f"O Eevee de {nome_treinador} se transformou em Leafeon, um espírito da floresta!")
#Parabéns é o mais fofo <3. 
        elif evolucao_especie == "Sylveon":
            print(f"Sylveon é a evolução mágica do Eevee de {nome_treinador}, irradiando bondade e misticismo!")

evolucao()

