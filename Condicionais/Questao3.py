#Dados Da Questão
pontuacaocharles = float(input())
pontuacaomax = float(input())

#Classificação das Corridas
#Charles em dia ruim
if pontuacaocharles <1:
    print ("Oxe! E vai morrer por causa de 25 pontos?")
#Charles MVP
elif pontuacaocharles ==25:
    print ("O meu favorito venceu! Pode torar o aco Verstappen")
#Charles top3
elif pontuacaocharles >=15 and pontuacaocharles <25 and pontuacaocharles !=10 :
    print ("Esse Charles eh arretado mesmo")
#Charles o grande
elif pontuacaocharles <=12 and pontuacaocharles >=10:
    print ("Ele eh desenrolado demais")
#Charles sendo humilde
if abs(pontuacaocharles-pontuacaomax) <=4:
    print ("Ta com a molestia, vai perder para Max Verstappen eh")
#A LENDA CHARLES
elif pontuacaocharles > pontuacaomax:
    print ("Deu o sangue")

