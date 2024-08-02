#Dados da questão para vc não ser igual Elisa.
lico = input().split(" ")
linhas, colunas = int(lico[0]), int(lico[2])

quantidade_elementos = int(input())
#Eita matrizes, bom pelo menos não é log ;)
matriz = [[0] * colunas for _ in range(linhas)]
#Aplicação vindo forte
for _ in range(quantidade_elementos):
    elemento = input().split(" ")
    nivel_atratividade = int(elemento[0])
    posicao = elemento[1][1:-1].split(",")
    linha, coluna = int(posicao[0]), int(posicao[1])
    matriz[linha][coluna] = nivel_atratividade
#Base de operações
operation = input()
while operation != "Fim":
    if operation == "Permutar":
#Operando
        posicoes = input().split()
        pos1 = posicoes[0][1:-1].split(",")
        pos2 = posicoes[1][1:-1].split(",")
        linha1, coluna1 = int(pos1[0]), int(pos1[1])
        linha2, coluna2 = int(pos2[0]), int(pos2[1])
        matriz[linha1][coluna1], matriz[linha2][coluna2] = matriz[linha2][coluna2], matriz[linha1][coluna1]
#Transpondo
    elif operation == "Transposição":
        nova_matriz = [[matriz[j][i] for j in range(linhas)] for i in range(colunas)] 
        matriz = nova_matriz
        linhas, colunas = colunas, linhas
#Removeeeeeeeeeeeeeendo
    elif operation == "Remover":
        menor_atratividade = float("inf")
        menor_posicao = None
        for i in range(linhas):
            for j in range(colunas):
                if matriz[i][j] != 0 and matriz[i][j] < menor_atratividade:
                    menor_atratividade = matriz[i][j]
                    menor_posicao = (i,j)
        if menor_posicao:
            linha, coluna = menor_posicao
            matriz[linha][coluna] = 0

    operation = input()
#Mostre o arranjo pelo amor <3
print("Atual Arranjo:")
for linha in matriz:
    print(" ".join(str(elemento) for elemento in linha))

