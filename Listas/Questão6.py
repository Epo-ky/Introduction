# Parte da Anjolina Jollie
quantidade_de_galinheiros = int(input())

coelhos = 0
galinhas = 0
patos = 0

for _ in range(quantidade_de_galinheiros):
    galinheiro = input().split(", ")
    for animal in galinheiro:
        if animal == "Coelho":
            coelhos += 1
        elif animal == "Galinha":
            galinhas += 1
        elif animal == "Pato":
            patos += 1

if coelhos > 0:
    print(f"A fazenda tem {coelhos} coelhos!")
else:
    print("Poxa que pena, não temos coelhos.")
if galinhas > 0:
    print(f"A fazenda tem {galinhas} galinhas!")
else:
    print("Poxa que pena, não temos galinhas.")
if patos > 0:
    print(f"A fazenda tem {patos} patos!")
else:
    print("Poxa que pena, não temos patos.")

# Grande Ricardo :T
lista_de_compras = input().split(", ")
loja_pierre = input().split(", ")

if "Melão" in lista_de_compras:
    print("Eita parece que não estão vendendo melões, ouvi boatos que tem alguém roubando eles. Um tal de Pedro Elias...")

possivel_compra = []
for item in lista_de_compras:
    if item in loja_pierre:
        possivel_compra.append(item)

if len(possivel_compra) == len(lista_de_compras):
    print("Consegui comprar todas as frutas que queria!")
elif len(possivel_compra) == 0:
    print("Poxa, acho que ficaremos sem plantações.")
else:
    possivel_compra.sort()
    print("Consegui comprar as seguintes sementes:")
    print(", ".join(possivel_compra))

# Simbora Stefan
itens_mochila = input().split(", ")
quantidades = input().split(", ")

for i in range(len(quantidades)):
    quantidades[i] = int(quantidades[i])

barra_de_ferro = 0
quartzo_refinado = 0
asa_de_morcego = 0

for i in range(len(itens_mochila)):
    item = itens_mochila[i]
    quantidade = quantidades[i]
    if item == "Barra de ferro":
        barra_de_ferro = quantidade
    elif item == "Quartzo refinado":
        quartzo_refinado = quantidade
    elif item == "Asa de morcego":
        asa_de_morcego = quantidade

materia_para_raio = min(barra_de_ferro, quartzo_refinado, asa_de_morcego // 5)

print(f"Com os itens que tenho, consigo fazer {materia_para_raio} para-raios!")
