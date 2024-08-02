#Deus me ajuda nessa madrugada, amém, DADOS DA QUESTÃO:
quantidade_alunos = int(input())
votos_beyonce = 0
votos_taylor_swift = 0

contador = 0
x = 0
#Tapoxa votação
for contador in range(quantidade_alunos):
    voto = input()
    x += 1
    if voto == "beyonce":
        votos_beyonce += 1
        print(f"Aluno {x} votou na Beyoncé.")
    elif voto == "taylor swift":
        votos_taylor_swift += 1
        print(f"Aluno {x} votou na Taylor Swift.")
    contador += 1
print("Contagem de votos:")
print(f"Taylor Swift: {votos_taylor_swift} votos")
print(f"Beyoncé: {votos_beyonce} votos")
if votos_beyonce > votos_taylor_swift:
    print(f"Beyoncé venceu com {votos_beyonce} votos! Será que Kanye West estava certo?")
elif votos_taylor_swift > votos_beyonce:
    print(f"Taylor Swift venceu com {votos_taylor_swift} votos! Kanye West tá irritado com isso.")
# Se Houver empate

if votos_beyonce == votos_taylor_swift:
    print("Empate! Iniciando rodada de debate.")
    print("Alunos, agora é a sua chance de convencer os outros a mudar de voto!")

    x = 0
    contador = 0
    for contador in range(quantidade_alunos):
        x += 1
        mudar_voto = input()
        if mudar_voto == "sim":
            novo_voto = input()
            if novo_voto == "beyonce":
                votos_beyonce += 1
                print(f"Aluno {x} mudou seu voto para Beyoncé.")
            elif novo_voto == "taylor swift":
                votos_taylor_swift += 1
                print(f"Aluno {x} mudou seu voto para Taylor Swift.")
        else:
            print(f"Aluno {x} não mudou seu voto.")

    print("Nova contagem de votos após o debate:")
    print(f"Taylor Swift: {votos_taylor_swift} votos")
    print(f"Beyoncé: {votos_beyonce} votos")
#bora aldo desempata essa poxa:
    contador += 1
    if votos_beyonce == votos_taylor_swift:
        print("Aldo, como presidente do evento, tem o voto decisivo.")
        voto_decisivo = input()
        if voto_decisivo == "beyonce":
            votos_beyonce += 1
            print("Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?")
        elif voto_decisivo == "taylor swift":
            votos_taylor_swift += 1
            print("Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso.")

#todos sabiamos como ia terminar
    else:
        if votos_beyonce > votos_taylor_swift:
            print(f"Beyoncé venceu com {votos_beyonce} votos! Será que Kanye West estava certo?")
        else:
            print(f"Taylor Swift venceu com {votos_taylor_swift} votos! Kanye West tá irritado com isso.")




