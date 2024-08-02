condicoes_meteorologicas = input()
if condicoes_meteorologicas == "chuvoso":
     pista_molhada = input() == "True"
temperatura_pista = input()
desempenho_treinos = input()
posicao_largada = float(input())


print ("Estratégia de prova de Max Verstappen!")

#relação pista e tempo
if condicoes_meteorologicas == "ensolarado" and temperatura_pista == "alta":
    print ("Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!")

elif condicoes_meteorologicas == "ensolarado" and temperatura_pista not in "alta":
    print ("Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.")

elif condicoes_meteorologicas == "nublado" and temperatura_pista == "alta":
    print ("Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!")

elif condicoes_meteorologicas == "nublado" and (temperatura_pista == "baixa" or temperatura_pista == "moderada"):
    print ("Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!")

elif condicoes_meteorologicas == "chuvoso" and pista_molhada:
    print ("Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.")
else:
        print ("Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!")

#Dentro de campo, dentro de treino:
if posicao_largada == 1 and desempenho_treinos == "bom":
    print ("Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.")
elif posicao_largada == 1 and desempenho_treinos == "ruim":
    print ("Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.")
elif posicao_largada > 1 and posicao_largada < 13:
    print ("Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.")
elif posicao_largada > 12:
     print ("Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.")
