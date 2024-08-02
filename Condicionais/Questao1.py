piloto = input ()
piloto_01 = "Max Verstappen"
piloto_02 = "Sergio Perez"



distancia = float(input())
tempo = float(input())
velocidade = distancia / tempo
#melhor resultado
if  velocidade > 227:
    print (f"{piloto} se deu muito bem na prova de hoje!!")
#resultado medio
elif  velocidade == 227:
    print (f"{piloto} teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!")
#pior resultado
elif  velocidade <227:
    print (f"{piloto} não se deu tão bem. É preciso melhorar isso!")
    
