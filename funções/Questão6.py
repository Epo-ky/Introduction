#Matriz Pokemonsta
def criar_matriz(pokemons_armazenados):
    boxes = []
    num_matrizes = pokemons_armazenados // (5 * 6)
    elementos_restantes = pokemons_armazenados % (5 * 6)

    for _ in range(num_matrizes):
        boxes.append([[1] * 6 for _ in range(5)])

    if elementos_restantes > 0:
        box_parcial = [[0] * 6 for _ in range(5)]
        indice = 0
        for linha in range(5):
            for coluna in range(6):
                if indice < elementos_restantes:
                    box_parcial[linha][coluna] = 1
                    indice += 1

        boxes.append(box_parcial)

    if pokemons_armazenados == 0:
        boxes.append([[0] * 6 for _ in range(5)])  # Adiciona uma matriz vazia com zeros

    return boxes

# função de captura e registro
def capturar_pokemon(boxes, quantidade_pokemon):
    for box in boxes:
        for i in range(5):
            for j in range(6):
                if quantidade_pokemon > 0 and box[i][j] == 0:
                    box[i][j] = 1
                    quantidade_pokemon -= 1
    while quantidade_pokemon > 0:
        nova_box = [[0] * 6 for _ in range(5)]
        for i in range(5):
            for j in range(6):
                if quantidade_pokemon > 0:
                    nova_box[i][j] = 1
                    quantidade_pokemon -= 1
        boxes.append(nova_box)

# e o gengar, nada ainda? oia a transferencia
def transferir_pokemon(boxes, quantidade_pokemon):
    i = len(boxes) - 1
    while quantidade_pokemon > 0 and i >= 0:
        box = boxes[i]
        for linha in range(4, -1, -1):
            for coluna in range(5, -1, -1):
                if quantidade_pokemon > 0 and box[linha][coluna] == 1:
                    box[linha][coluna] = 0
                    quantidade_pokemon -= 1
        if sum(sum(i) for i in box) == 0 and len(boxes) > 1:
            boxes.pop(i)
        i -= 1

# amostra o box >:C
def imprimir_boxes(boxes):
    for numero_box, box in enumerate(boxes, start=1):
        print(f"BOX {numero_box}:")
        for linha in box:
            print(' '.join(str(num) for num in linha))
        print()
    if len(boxes) <= 0:
        print(f"BOX 1:")   
        matriz_vazia = [[0 for _ in range(6)] for _ in range(5)]
        for linha in matriz_vazia:
            print(' '.join(str(elemento) for elemento in linha))
        print()

# relatorio final ou seja chega fi cabo a graça.
def relatorio_final(boxes):
    print("RELATÓRIO FINAL:\n")
    print(f"BOXES: {len(boxes)}")
    quantidade_total_pokemon = sum(sum(sum(i) for i in matriz) for matriz in boxes)
    print(f"POKEMONS: {quantidade_total_pokemon}")

# Iniciando os Pokemons
pokemons_armazenados = int(input())
boxes = criar_matriz(pokemons_armazenados)

# Execução dos comandos
comando = input()
while comando != "Finalizar":
    if comando == "Capturar":
        quantidade_pokemon = int(input())
        capturar_pokemon(boxes, quantidade_pokemon)
        imprimir_boxes(boxes)
        
    elif comando == "Transferir":
        quantidade_pokemon = int(input())
        transferir_pokemon(boxes, quantidade_pokemon)
        imprimir_boxes(boxes)
    
    comando = input()

# Relatório final
relatorio_final(boxes)
