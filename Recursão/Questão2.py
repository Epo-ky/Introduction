#Eita como calculaaa
def calculo_mdc(a,b):
    if b == 0:
        return a
    return calculo_mdc(b, a % b)    
#Numeros e numerais
numero = int(input())
soma_mdc = 0
# laçozinho para repetição
for _ in range(numero):
    incursao = input().split()
    x = int(incursao[0].replace(" ", ""))
    y = int(incursao[1].replace(" ", ""))

    resultado_mdc = calculo_mdc(x,y)

    print(f"O MDC entre {x} e {y} é {resultado_mdc}")
# somatorio dos minimos divisores comuns :))
    if resultado_mdc != 0:
        soma_mdc += resultado_mdc

print(f"\nA senha final foi {soma_mdc}")

