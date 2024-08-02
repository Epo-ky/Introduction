from decimal import Decimal, getcontext
getcontext().prec = 15
#Dados da questão, só jesus na causa
quantidade_veiculos = int(input())
acidente_info = input()
distancia_total = Decimal(input())
codigo_serializacao = input()

tempo_atraso = 0

#Eu que vou me acidentar jaja
if acidente_info == 'sim':
    tempo_atraso += 20
tempo_atraso += (Decimal(0.6) * quantidade_veiculos)

#Calculo gato a jato
opcao_A = "A"
velocidade_carro = 60
velocidade_jato = 1089

distancia_jato = distancia_total * Decimal(0.8)
distancia_carro = distancia_total * Decimal(0.2)
tempo_jato = distancia_jato / velocidade_jato
tempo_carro = distancia_carro / velocidade_carro
tempo_total_viagemA =  (tempo_carro + tempo_jato) * 60
tempo_total_A = tempo_total_viagemA  + tempo_atraso

#Calculo busão
opcao_B = "B"
velocidade_onibus = 40
tempo_onibus = distancia_total / velocidade_onibus
tempo_total_viagemB = tempo_onibus * 60

tempo_total_B = tempo_total_viagemB + tempo_atraso

#Calculo Eli O Copeteru
opcao_C = "C"
velocidade_helicoptero = 60

tempo_helicoptero = distancia_total / velocidade_helicoptero
tempo_total_C = tempo_helicoptero * 5 * 10


#Vamos para as opções:
print ("Análise das opções de transporte até o show!")
print (f"Opção {opcao_A} - Você chegará ao show em {tempo_total_A:.1f} minutos")
print (f"Opção {opcao_B} - Você chegará ao show em {tempo_total_B:.1f} minutos")
print (f"Opção {opcao_C} - Você chegará ao show em {tempo_total_C:.1f} minutos")
print ("---")
#Serialização sabado eu me mato, oba sabado eu me mato



ultimo_codigo = ""

for _ in codigo_serializacao:
    if int(_) % 2 == 0:
        ultimo_codigo += _ + "23"
    else:
        ultimo_codigo += _ + "78"

print (f"Senha de serialização transformada: {ultimo_codigo}, guarde com segurança!")


