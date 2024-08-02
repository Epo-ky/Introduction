#Dados da questão
voltas = int(input())
clima = input()
dificuldade = input()
tipo_pneu = input()

#Dias molhados
if tipo_pneu == "chuva" and clima == "sol":
    desgaste = (50 - voltas * 15)
#Pneu forte na chuva
elif tipo_pneu == "duro" and clima == "chuva":
    desgaste = (90 - voltas * 15)
#pneu razoavel na chuva
elif tipo_pneu == "médio" and clima == "chuva":
   desgaste = (70 - voltas * 15)
#pneu fofo na chuva
elif tipo_pneu == "macio" and clima == "chuva":
   desgaste = (50 - voltas * 15)
#Solzao facil ou nem tanto e com pneu fofo
if clima == "sol" and dificuldade == "baixa" or dificuldade == "média" and tipo_pneu == "macio":
    desgaste = (50 - voltas * 2)
#solzao, facil, ou nem tanto e pneu razoavel
elif clima == "sol" and dificuldade == "baixa" or dificuldade == "média" and tipo_pneu == "médio":
    desgaste = (70 - voltas * 2)
#grande sol dificil e com pneu fofo
if clima == "sol" and dificuldade == "alta" and tipo_pneu == "macio":
   desgaste = (50 - voltas * 3)
#grande sol dificil e o pneu mais forte
elif clima == "sol" and dificuldade == "alta" and tipo_pneu == "duro":
    desgaste = (90 - voltas)
#eita chuvinha mas ta facil e com pneu pra isso
if clima == "chuva" and dificuldade == "baixa" and tipo_pneu == "chuva":
   desgaste = (50 - voltas)
#eita chuvinha ta mediano mas ainda com pneu pra isso
elif clima == "chuva" and dificuldade == "média" and tipo_pneu == "chuva":
    desgaste = (50 - voltas * 2)
# eita chuvinha ta complicado mas ainda com pneu pra isso
elif clima == "chuva" and dificuldade == "alta" and tipo_pneu == "chuva":
   desgaste =  (50 - voltas * 3)


#SUCESSO
if desgaste >= 20:
    print (f"A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {desgaste}.")
#Falhamos
elif desgaste <= 20:
    print (f"Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {desgaste} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.")
