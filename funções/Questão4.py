def cifra_de_cesar(texto, deslocamento):
    resultado = []
    for char in texto:
        if "a" <= char <= "z":
            novo_char = chr((ord(char) - ord("a") + deslocamento) % 26 + ord("a"))
            resultado.append(novo_char)
        elif "A" <= char <= "Z":
            novo_char = chr((ord(char) - ord("A") + deslocamento) % 26 + ord("a"))
            resultado.append(novo_char)
        else:
            resultado.append(char)
    return "".join(resultado)

def calcular_id(nome, deslocamento, tempo):
    nome_codificado = cifra_de_cesar(nome, deslocamento)
    soma_ascii = sum(ord(letra) for letra in nome_codificado)
    id_calculado = soma_ascii * tempo
    return id_calculado

def inteiro(string):
    # Verifica se a string não está vazia e contém apenas dígitos
    if not string:
        return False
    for char in string:
        if char < '0' or char > '9':
            return False
    return True

def processar_eventos(numero_participantes, entrada_apresentacao, eventos):
    nomes_participantes = []
    favoritos = []
    pokebolas = []

    # Criando uma lista de shinies para cada participante
    shinies = [[] for _ in range(numero_participantes)]
    
    # Processando a entrada de apresentação
    for apresentacao in entrada_apresentacao:
        apresentacao_tratada = apresentacao.split(", ")
        nome = apresentacao_tratada[1].split("é ")[1]
        favorito = apresentacao_tratada[2].split("é ")[1]
        qtd_pokebolas = apresentacao_tratada[2].split(" ")[7]
        favorito = favorito.replace(f" e tenho {qtd_pokebolas} pokébolas", "")
        nomes_participantes.append(nome)
        favoritos.append(favorito)
        pokebolas.append(int(qtd_pokebolas))
    
    contador_shiny = 0
    shiny_verdadeiro = False
    
    # Loop para processar os eventos
    while not shiny_verdadeiro:
        evento = input()
        eventos.append(evento)
        
        # Tratamento do evento
        eventos_tratados = evento.split("! ")
        pokemon = eventos_tratados[0].split("Um ")[1]
        pokemon = pokemon.replace(" selvagem apareceu", "")
        participante = eventos_tratados[1].split(" de ")[1]
        
        # Extrair o número de passos
        passos_str = eventos_tratados[1].split(" e ")[1].replace(" passos desde o último encontro de", "")
        passos_digitos = [char for char in passos_str if '0' <= char <= '9']
        passos = int(''.join(passos_digitos)) if passos_digitos else 0
        
        tempo_str = eventos_tratados[1].split("Foram ")[1].split(" segundos e ")[0]
        tempo = int(tempo_str)
        
        
        # Índice do participante atual no vetor de participantes
        indice_participante = nomes_participantes.index(participante)
        
        # Verifica se o Pokémon encontrado é shiny
        id_participante = calcular_id(participante, 3, 1)
        id_pokemon = calcular_id(pokemon, passos, tempo)
        
        # Informações do participante atual
        shiny_verdadeiro = str(id_participante)[-1] == str(id_pokemon)[-1]
        pokemon_favorito = favoritos[indice_participante]
        pokebolas_restantes = pokebolas[indice_participante]
        
        # Verifica se o participante tem pokébolas suficientes para continuar
        if pokebolas_restantes > 0:
            if shiny_verdadeiro:
                if pokemon not in shinies[indice_participante]:
                    shinies[indice_participante].append(pokemon)
                    pokebolas[indice_participante] -= 1
                    if pokemon == pokemon_favorito:
                        if pokebolas[indice_participante] == 0:
                            print(f"{participante}: Que sorte! Não apenas achei meu shiny favorito, como também o capturei em minha última pokébola!!!")
                            contador_shiny += 1
                        else:
                            print(f"{participante}: Consegui capturar um {pokemon_favorito} shiny!")
                            contador_shiny += 1
                    else:
                        print(f"{participante}: Mais um shiny para a coleção, mas ainda não é um {pokemon_favorito}")
                        shiny_verdadeiro = False
                elif pokemon in shinies[indice_participante]:
                    print(f"{participante}: Achei um {pokemon} shiny, mas não posso desperdiçar pokébolas em um shiny que já tenho...")
                    shiny_verdadeiro = False
            else:
                if pokemon == pokemon_favorito:
                    pokebolas[indice_participante] -= 1
                    print(f"{participante}: Uau, um {pokemon_favorito}! Pena que não é um shiny...")
                    shiny_verdadeiro = False
                else:
                    print(f"{participante}: Ainda não é um {pokemon_favorito} shiny, tenho que continuar procurando...")
                    shiny_verdadeiro = False
        else:
            if shiny_verdadeiro:
                if pokemon == pokemon_favorito:
                    print(f"{participante}: Só pode ser brincadeira, um {pokemon_favorito} shiny logo agora?!")
                    shiny_verdadeiro = False
                else:
                    print(f"{participante}: Péssimo momento, encontrei um {pokemon} shiny, mas não tenho mais pokébolas!")
                    shiny_verdadeiro = False
            else:
                if pokemon == pokemon_favorito:
                    print(f"{participante}: Desculpa, meu querido {pokemon_favorito}, mas não poderei lhe capturar hoje")
                else:
                    print(f"{participante}: Só um {pokemon} normal?Bom, não é como se eu tivesse pokébolas para capturar algo raro mesmo...")

        # Verifica se todos os participantes encontraram seu shiny favorito
        if contador_shiny >= numero_participantes:
            shiny_verdadeiro = True
    
    # Impressão final dos resultados
    print("\n---Vamos verificar o que todos encontraram!---")
    for idx in range(numero_participantes):
        nome_pessoa = nomes_participantes[idx]
        shinies_list = shinies[idx]  # Lista de shinies do participante atual
        if shinies_list:
            if len(shinies_list) == 1:
                print(f"{nome_pessoa} capturou os seguintes shinies: {shinies_list[0]}")
            else:
                print(f"{nome_pessoa} capturou os seguintes shinies: {', '.join(shinies_list)}")
        else:
            print(f"Coitado, {nome_pessoa} não conseguiu capturar um único shiny hoje")

# Leitura dos inputs
numero_participantes = int(input())
entrada_apresentacao = []
for participante in range(numero_participantes):
    entrada = input()
    entrada_apresentacao.append(entrada)

# Lista de eventos vazia
eventos = []
processar_eventos(numero_participantes, entrada_apresentacao, eventos)
