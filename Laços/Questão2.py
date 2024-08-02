#os entrevistados que lutem
numero_pessoas = int(input())
qtd_resposta1 = 0
qtd_resposta2 = 0
qtd_resposta3 = 0

#galera da enquete
for i in range(numero_pessoas):
    resposta = input()
    if resposta == "Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!":
        qtd_resposta1 += 1
    elif resposta == "Não gostei. Muito sem graça, onde já se viu nome com duas letras?":
        qtd_resposta2 += 1
    elif resposta == "Ainda estou me acostumando. Não tenho uma opinião formada sobre isso.":
        qtd_resposta3 += 1

print ("A pesquisa terminou e os resultados foram os seguintes:")

totais = qtd_resposta1 + qtd_resposta2 + qtd_resposta3
#continha de resposta da galera
taxa_de_aprovacao = (qtd_resposta1 / totais) * 100
taxa_de_rejeicao = (qtd_resposta2 / totais) * 100
taxa_de_abstencao = (qtd_resposta3 / totais) * 100

print (f"Taxa de aprovação: {taxa_de_aprovacao:.2f}")
print (f"Taxa de rejeição: {taxa_de_rejeicao:.2f}") 
print (f"Taxa de abstenção: {taxa_de_abstencao:.2f}") 

#É né, tem quem goste.
if taxa_de_aprovacao > taxa_de_rejeicao:
    print ("YES!!! Sabia que as pessoas gostariam!")
#Alguns nem tanto.
elif taxa_de_aprovacao < taxa_de_rejeicao:
    print ("Ops... Por essa eu não esperava.")
#Outros tão pouco.
elif taxa_de_aprovacao == taxa_de_rejeicao:
    print ("Bom... Vou olhar para o copo meio cheio!")
