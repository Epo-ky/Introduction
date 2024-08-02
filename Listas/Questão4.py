#Meu irmão... quer dizer, dados da questão:
agricultura = []
criacao_de_animais = []
pesca = []
mineracao = []

#Agro é pop, criação de animais é massa, pesca é legal, minerar so em dia de sorte :))
agricultura = input().split(" - ")
criacao_de_animais = input().split(" - ")
pesca = input().split(" - ")
mineracao = input().split(" - ")
resposta = ""
finalizacao = False
print("Itens selecionados! Hora de iniciar a mesclagem... Simbora!")
while not finalizacao:
    a = int(input())
    c = int(input())
    p = int(input())
    m = int(input())
    
    print("Combinando Itens...")
    item_agro = agricultura[a]
    print(f"Item para agricultura: {item_agro}")
    item_cda = criacao_de_animais[c]
    print(f"Item para criação: {item_cda}")
    item_pesca = pesca[p]
    print(f"Item para pesca: {item_pesca}")
    item_mineracao = mineracao[m]
    print(f"Item para mineração: {item_mineracao}")
    
#Resposta, menos a minha :((
    resposta = input()
    if resposta == "Gostei de ver! Ir atrás desses itens vai me render boas horas de diversão...":
        finalizacao = True
        print("Meu dia tá garantido, obrigado pela ajuda Pega Móvel!")
    elif resposta == "Esses itens são bem paia, acho que não gostei muito :(":
        resposta = input()
        if resposta == "Essa máquina deve estar com defeito...":
            print("É... acho que já chega de Stardew por hoje...")
            finalizacao = True
        

#Terminamos :) :(
if not finalizacao:
    print("Meu dia tá garantido, obrigado pela ajuda Pega Móvel!")
