#a ultima esperança
def calculo_dano(nivel, poder, defesa_inimigo, poder_ataque, efetividade):
    return int((((((2 * nivel) + 10) / 250) * (poder / defesa_inimigo * poder_ataque)) + 2) * efetividade)
#Foi super efetivo no meu coração MEU DEUS...
def calculo_efetividade(tipo_atacante, tipo_defensor):
    if tipo_atacante == tipo_defensor or (tipo_atacante == "normal" or tipo_defensor == "normal"):
        return 1
    elif (tipo_atacante == "fogo" and tipo_defensor == "agua") or (tipo_atacante == "agua" and tipo_defensor == "grama") or (tipo_atacante == "grama" and tipo_defensor == "fogo"):
        return 0.5
    elif (tipo_atacante == "fogo" and tipo_defensor == "grama") or (tipo_atacante == "agua" and tipo_defensor == "fogo") or (tipo_atacante == "grama" and tipo_defensor == "agua"):
        return 2
    else:
        return 1
#DUELO, opa jogo errado hehe
def batalha(nome_pokemon, tipo_pokemon, nivel_pokemon, vida_pokemon, poder_pokemon, defesa_pokemon, velocidade_pokemon, nome_ataque, poder_ataque):
    print(f"escolho você {nome_pokemon}")

    combate_ativo = True
    while combate_ativo:
        mensagem = input()
        if mensagem == "um pokemon selvagem aparece!":
            print("vamo botar pra quebrar!\n")
        elif mensagem == "Equipe Rocket":
            print(f"{nome_pokemon}, bora acabar com a raça desses bandidos e salvar o professor!\n")
#dados do MY ENEMY, MY ENEMY,YOU ARE MY ENEMY
        dados_inimigo = input().split(", ")
        nome_inimigo = dados_inimigo[0]
        tipo_inimigo = dados_inimigo[1]
        nivel_inimigo = int(dados_inimigo[2])
        vida_inimigo = int(dados_inimigo[3])
        poder_inimigo = int(dados_inimigo[4])
        defesa_inimigo = int(dados_inimigo[5])
        velocidade_inimigo = int(dados_inimigo[6])
        nome_ataque_inimigo = dados_inimigo[7]
        poder_ataque_inimigo = int(dados_inimigo[8])

        vida_total_inimigo = vida_inimigo

        my_turn = velocidade_pokemon > velocidade_inimigo
        cnt = 0
        
        while vida_pokemon > 0 and vida_inimigo > 0:
    # Leitura da ação do jogador antes do turno dele
            acao = input().split()[0].lower()

            if acao == "correr":
                if mensagem == "Equipe Rocket":
                    print("Lascou, eles não largam do meu pé!")
                else:
                    print("Ufa, consegui meter o pé!")
          

            # Turno do jogador
            if my_turn and combate_ativo:
                if acao == "atacar":
                    efetividade = calculo_efetividade(tipo_pokemon, tipo_inimigo)
                    dano = calculo_dano(nivel_pokemon, poder_pokemon, defesa_inimigo, poder_ataque, efetividade)
                    print(f"{nome_pokemon} usou {nome_ataque}")
                    if efetividade == 2:
                        print("Foi super efetivo!")
                    elif efetividade == 0.5:
                        print("Não foi muito efetivo")
                    vida_inimigo -= dano
                    vida_inimigo = max(0, vida_inimigo)
                    my_turn = False  # Passa para o turno do inimigo

                    
                    

            # Turno do inimigo
            if not my_turn and combate_ativo:
                efetividade = calculo_efetividade(tipo_inimigo, tipo_pokemon)
                dano = calculo_dano(nivel_inimigo, poder_inimigo, defesa_pokemon, poder_ataque_inimigo, efetividade)
                print(f"{nome_inimigo} usou {nome_ataque_inimigo}")
                if efetividade == 2:
                    print("Foi super efetivo!")
                elif efetividade == 0.5:
                    print("Não foi muito efetivo")
                vida_pokemon -= dano
                vida_pokemon = max(0, vida_pokemon)
                my_turn = True  # Passa para o turno do jogador

                
              

            cnt += 1
                
            if vida_pokemon == 0 or vida_inimigo == 0 and cnt % 2 != 0:
                    print(f"HP: {int(vida_pokemon)}/{int(vida_total)} | HP inimigo: {int(vida_inimigo)}/{int(vida_total_inimigo)}")
                    
            

            if cnt % 2 == 0:
                print(f"HP: {int(vida_pokemon)}/{int(vida_total)} | HP inimigo: {int(vida_inimigo)}/{int(vida_total_inimigo)}")
        if vida_pokemon == 0:
            print(f"{nome_pokemon} derrotado!\n")
            print("Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.")
            combate_ativo = False
        elif vida_inimigo == 0:
            print(f"{nome_inimigo} derrotado!\n")
            if mensagem == "Equipe Rocket":
                print(f"Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {nome_pokemon}?")
                combate_ativo = False

# Informações dos melhores, vulgo meus pokemonsta:
dados_pokemon = input().split(", ")
nome_pokemon = dados_pokemon[0]
tipo_pokemon = dados_pokemon[1]
nivel_pokemon = int(dados_pokemon[2])
vida_pokemon = int(dados_pokemon[3])
poder_pokemon = int(dados_pokemon[4])
defesa_pokemon = int(dados_pokemon[5])
velocidade_pokemon = int(dados_pokemon[6])
nome_ataque = dados_pokemon[7]
poder_ataque = int(dados_pokemon[8])
vida_total = vida_pokemon
batalha(nome_pokemon, tipo_pokemon, nivel_pokemon, vida_pokemon, poder_pokemon, defesa_pokemon, velocidade_pokemon, nome_ataque, poder_ataque)
