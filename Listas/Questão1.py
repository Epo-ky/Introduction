#Dor e solidão, dados da questão:
num_animais = int(input())
catalogo = []

#Laço da depressão, laço da questão:
while len(catalogo) < num_animais:
    comando = input()
    if comando == "REGISTRA":
        animal = input()
        if animal in catalogo:
            print(f"{animal} já foi registrado antes!")
        else:
            catalogo.append(animal)
            print(f"{animal} registrado com sucesso.")
        
    elif comando == "CORRIGE":
        if len(catalogo) >= 1:
            catalogo.pop()
            print("Último registro apagado com sucesso.")
        else:
            print("O catálogo ainda está vazio.")
    
    elif comando == "REINICIA":
        catalogo.clear()
        print("Catálogo redefinido com sucesso.")

#tapoxa todo mundo tem registro
print("Todos os animais foram registrados!\n")
print("Catálogo de animais:")
i = 0
for animal in range(len(catalogo)):
    i += 1
    print(f"{i}º: {catalogo[animal]}")
