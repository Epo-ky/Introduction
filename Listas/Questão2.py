#SUUUUUUSPEITO, dados da questão:
lista_de_sus = []
finalizacao = False
#voce filma e laça, vc é o bixão mesmo hein doido:
while not finalizacao:
    investigacao = input()
    if investigacao == "Já temos nossa lista de suspeitos":
        print("O resultado final ficou assim:")
        y = ", ".join(lista_de_sus)
        print(y)
        finalizacao = True
#o proprio perigo
    if investigacao == "Novo suspeito - altíssima periculosidade":
        nome_do_suspeito = input()
        lista_de_sus.insert (0,  nome_do_suspeito)
#machuca pouco
    elif investigacao == "Novo suspeito - pouco perigoso":
        nome_do_suspeito = input()
        lista_de_sus.append(nome_do_suspeito)
#inocente
    elif investigacao == "Livre de suspeita, pode remover":
        nome_do_suspeito = input()
        lista_de_sus.remove(nome_do_suspeito)
#criminoso, pode mandar prender
    elif investigacao == "Sujeito mais perigoso do que pensávamos":
        indice_atual = int(input())
        indice_atualizado = int(input())
        lista_de_sus[indice_atual], lista_de_sus[indice_atualizado] = lista_de_sus[indice_atualizado], lista_de_sus[indice_atual]
# ora  ora oque temos aqui?!
    elif investigacao == "Que estranho, esses dois meliantes… troque-os de lugar":
        nome_do_suspeito = input()
        nome_do_suspeito2 = input()
        indice_1 = lista_de_sus.index(nome_do_suspeito)
        indice_2 = lista_de_sus.index(nome_do_suspeito2)
        lista_de_sus[indice_1], lista_de_sus[indice_2] = lista_de_sus[indice_2], lista_de_sus[indice_1]
# ele nem é tudo isso
    elif investigacao == "Essa posição não esta de acordo, ele não e tão perigoso assim":
        nome_do_suspeito = input()
        lista_de_sus.remove(nome_do_suspeito)
        lista_de_sus.append(nome_do_suspeito)
# ta boa a lista?
    elif investigacao == "Como a lista esta ficando?":
        y = ", ".join(lista_de_sus)
        print(y)
