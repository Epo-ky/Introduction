#Dados da questão
velocidade_maxima = int(input())
tempo = (input())


#Resultados em Monaco
if (tempo == "ensolarado" or tempo == "chuvoso") and (velocidade_maxima > 250 and velocidade_maxima <=260):
    print ("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")
elif tempo == "neblina" and velocidade_maxima <250:
    print ("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")
#Resultados em Imola
elif (tempo =="ensolarado" or tempo == "chuvoso") and (velocidade_maxima > 261 and velocidade_maxima <=285):
    print ("Senna corria em Ímola, onde infelizmente fez sua última corrida.")
elif tempo == "neblina" and velocidade_maxima <260:
    print ("Senna corria em Ímola, onde infelizmente fez sua última corrida.")
#Resultados em Spa-Francorchamps
elif (tempo =="ensolarado" or tempo == "chuvoso") and (velocidade_maxima > 286 and velocidade_maxima <=310):
    print ("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")
elif tempo == "neblina" and velocidade_maxima <285:
    print ("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")

