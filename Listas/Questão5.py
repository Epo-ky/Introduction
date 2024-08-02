#Meu deus que sonão, eita, dados da questão junto do laço de repetição
lista_de_peixes = ["Anchova", "Atum", "Bagre", "Baiacu", "Cioba", "Enguia", "Esturjão", "Linguado", "Pepino-do-mar", "Polvo", "Salmão", "Sardinha", "Tilápia", "Truta", "Robalo"]
lista_p_diferentes1 = []
nome_pescador1, conquista1 = input().split(": ")
lista_conquistas = conquista1.split(", ")
lista_peixes_1 = []
fim = False
while not fim:
    peixe = input()
    if peixe in lista_de_peixes:
        lista_peixes_1.append(peixe)
        if peixe not in lista_p_diferentes1:
                lista_p_diferentes1.append(peixe)
    if peixe not in lista_de_peixes:
        fim = True
lista_p_diferentes2 = []
nome_pescador2, conquista2 = input().split(": ")
lista_conquistas = conquista2.split(", ")
lista_peixes_2 = []
fim = False
while not fim:
    peixe = input()
    if peixe in lista_de_peixes:
        lista_peixes_2.append(peixe)
        if peixe not in lista_p_diferentes2:
                lista_p_diferentes2.append(peixe)
    if peixe not in lista_de_peixes:
        fim = True
lista_p_diferentes3 = []
nome_pescador3, conquista3 = input().split(": ")
lista_conquistas = conquista3.split(", ")
lista_peixes_3 = []
fim = False
while not fim:
    peixe = input()
    if peixe in lista_de_peixes:
        lista_peixes_3.append(peixe)
        if peixe not in lista_p_diferentes3:
                lista_p_diferentes3.append(peixe)
    if peixe not in lista_de_peixes:
          fim = True


verdadeiro_pescador1 = True
#laço for para definir a veracidade das conquistas
for conquistas in conquista1.split(", "):
    if conquistas == "Pescador" and len(lista_p_diferentes1) < 5:
            verdadeiro_pescador1 = False
    elif conquistas == "Velho Marinheiro" and len(lista_p_diferentes1) < 10:
            verdadeiro_pescador1 = False
    elif conquistas == "Velho Pescador" and sorted(lista_p_diferentes1) != sorted(lista_de_peixes):
            verdadeiro_pescador1 = False
    elif conquistas == "Deus Pescador" and len(lista_peixes_1) < 25:
            verdadeiro_pescador1 = False

verdadeiro_pescador2 = True 
#mesma coisa do laço for 1
for conquistas in conquista2.split(", "):
    if conquistas == "Pescador" and len(lista_p_diferentes2) < 5:
            verdadeiro_pescador2 = False
    elif conquistas == "Velho Marinheiro" and len(lista_p_diferentes2) < 10:
            verdadeiro_pescador2 = False
    elif conquistas == "Velho Pescador" and sorted(lista_p_diferentes2) != sorted(lista_de_peixes):
            verdadeiro_pescador2 = False
    elif conquistas == "Deus Pescador" and len(lista_peixes_2) < 25:
            verdadeiro_pescador2 = False

verdadeiro_pescador3 = True
#mesma coisa do laço for 2
for conquistas in conquista3.split(", "):
    if conquistas == "Pescador" and len(lista_p_diferentes3) < 5:
            verdadeiro_pescador3 = False
    elif conquistas == "Velho Marinheiro" and len(lista_p_diferentes3) < 10:
            verdadeiro_pescador3 = False
    elif conquistas == "Velho Pescador" and sorted(lista_p_diferentes3) != sorted(lista_de_peixes):
            verdadeiro_pescador3 = False
    elif conquistas == "Deus Pescador" and len(lista_peixes_3) < 25:
            verdadeiro_pescador3 = False

#Um homem integro
if verdadeiro_pescador1:
    print(f"{nome_pescador1} realmente estava falando a verdade!!!")
#mais ou menos:
else:
    print(f"{nome_pescador1} é um mentiroso, ele não tem todas essas conquistas!")
# um homem verdadeiro:    
if verdadeiro_pescador2:
    print(f"{nome_pescador2} realmente estava falando a verdade!!!")
#mais ou menos
else:
    print(f"{nome_pescador2} é um mentiroso, ele não tem todas essas conquistas!")
#gente boaaaaa
if verdadeiro_pescador3:
    print(f"{nome_pescador3} realmente estava falando a verdade!!!")
#talvez nem tão verdade
else:
    print(f"{nome_pescador3} é um mentiroso, ele não tem todas essas conquistas!")
    

