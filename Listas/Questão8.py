#Vo ver e te aviso, dados da questão :))

recursos_da_primavera = ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"]
recursos_do_verao = ["uva", "cafe-de-jardim", "ervilha-de-cheiro"]
recurso_do_outono = ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"]
recurso_do_inverno = ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]

plantacoes_da_primavera = ["chirivia", "vagem", "couve-flor", "batata"]
plantacoes_do_verao = ["tomate", "mirtilo", "melao", "pimenta-quente"]
plantacoes_do_outono = ["milho", "beringela", "abobora", "inhame"]
artesao = ["mel", "geleia", "queijo", "tecido"]
#tipos de salinha
tipo_sala = ["artesanato", "copa", "caldeira", "aquário", "mural"]

sala = input()
conjuntos = input()
itens = input()
#as salas que ja tão cheia pow
salas_completas = ["caldeira", "aquário", "mural"]

#aqui não tem ninguem
if sala not in tipo_sala:
    print("Essa sala não está no centro comunitário")
elif sala in salas_completas:
    print(f"Eu já conclui {sala}, não precisa doar mais itens para essa sala")
else:
    if conjuntos == " " or itens == " ":
        print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
    else:
        conjuntos = conjuntos.split(", ")
        itens = itens.split(", ")
        

        conjuntos_principais = []
        for c in conjuntos:
            if c not in conjuntos_principais:
                conjuntos_principais.append(c)
        
        itens_principais = []
        for i in itens:
            if i not in itens_principais:
                itens_principais.append(i)


        duplicacoes = False
        if len(itens) != len(itens_principais) or len(conjuntos) != len(conjuntos_principais):
            duplicacoes = True

        conjuntos_validos = []
        #checando os recursos
        if sala == "copa":
            for conjunto in conjuntos_principais:
                if conjunto == "recursos da primavera":
                    conjuntos_validos.extend(recursos_da_primavera)
                elif conjunto == "recursos do verao":
                    conjuntos_validos.extend(recursos_do_verao)
                elif conjunto == "recursos do outono":
                    conjuntos_validos.extend(recurso_do_outono)
                elif conjunto == "recursos do inverno":
                    conjuntos_validos.extend(recurso_do_inverno)
            
        #eita como checa recursos
        elif sala == "artesanato":
            for conjunto in conjuntos_principais:
                if conjunto == "plantacoes da primavera":
                    conjuntos_validos.extend(plantacoes_da_primavera)
                elif conjunto == "plantacoes do verao":
                    conjuntos_validos.extend(plantacoes_do_verao)
                elif conjunto == "plantacoes do outono":
                    conjuntos_validos.extend(plantacoes_do_outono)
                elif conjunto == "artesao":
                    conjuntos_validos.extend(artesao)
            

        conjuntos_grupo = conjuntos[:]
        itens_grupo = itens[:]
        itens_conjunto = itens[:]
        #oxe ta entregue meu patrão
        for item in itens_principais:
            if item in conjuntos_validos:
                print(f"{item} vai ser entregue ao centro logo!")
            else:
                print(f"{item} pode ser analisado depois")
        #pow Sergio, ta perdido?
        if duplicacoes:
            print("Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…")
