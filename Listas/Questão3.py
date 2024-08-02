itens_desejados = input().split(', ')
trecos_encontrados = input().split(', ')

itens_gerais = []

for item in trecos_encontrados:
    itens_gerais.apend(item)

encontrou_item = False
for item_desejado in itens_desejados:
    if item_desejado in itens_gerais:
        encontrou_item = True


if not encontrou_item:
    print(f"Parece que estou precisando fazer mais algumas colheitas! Não encontrei nenhum dos {itens_desejados} itens aqui na fazenda.")
else:
    print("Estes são os itens que já tenho na fazenda:")
    for i in range(len(itens_desejados)):
        for item in itens_gerais:
            if item == itens_desejados[i]:
                print(f"{i+1}º item: {itens_desejados[i]}")

encontrou_todos = True
for item_desejado in itens_desejados:
    if item_desejado not in itens_gerais:
        encontrou_todos = False

if encontrou_todos:
    print(f"Perfeito, encontrei todos os {len(itens_desejados)} itens aqui na fazenda!")
else:
    quantidade_itens_faltantes = 0
    for item_desejado in itens_desejados:
        if item_desejado not in itens_gerais:
            quantidade_itens_faltantes +1 
        print(f"Vou precisar adquirir {quantidade_itens_faltantes} itens antes do festival!")

print("Estou pronto para o festival de Stardew Valley! Que comece a diversão!")

