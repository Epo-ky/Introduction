#depressão, quer dizer, dados da questão
quantidade_exercicio = int(input())
tipos_de_treino = input()
nome_musica = ""
nota_musica = 0
i = 0
#treino sendo aplicado
while tipos_de_treino != "Fim do Treino":
    contagem_musica_boa = 0
    contagem_musica_ruim = 0
    print (f"{tipos_de_treino}")
    for treino in range(quantidade_exercicio):
        nome_musica = input()
        nota_musica = int(input())
        i += 1
        print(f"{i}° música {nome_musica} tocando agora")
        if nota_musica >= 7:
            contagem_musica_boa += 1
            print ("O padre Marcelo está inspirado, conseguiu finalizar suas séries!")
        elif nota_musica < 7:
            contagem_musica_ruim += 1
            print ("O padre Marcelo está desanimado, não conseguiu finalizar suas séries")

#tapoxa só musica massa
    if contagem_musica_boa >= (quantidade_exercicio // 2 + quantidade_exercicio % 2):
        print("ME DEI BEM COM ESSA PLAYLIST, APROVADO")
#prefiro o meu: NÃO HÁ FERROLHOOOOO, NEM PORTAAAAAAA
    else:
        print("NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL")

    tipos_de_treino = input()
    i = 0 
