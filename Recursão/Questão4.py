# Soma da lista...
def somar_lista(l):
    if isinstance(l, list):
        return sum(somar_lista(sub) for sub in l)
    else:
        return l

# Guardando os resultados...
def processar_lista(l, resultado):
    soma = somar_lista(l)
    for item in l:
        if isinstance(item, list):
            processar_lista(item, resultado)
    resultado.append([soma, l])

# Soma principal...
def soma(lista):
    resultado = []
    processar_lista(lista, resultado)
    return resultado

# Deus que frustração... saida do resultado
def imprimir(resultado):
    for soma, l in resultado:
        print(f"{soma} -> {l}")

# Meu psicologo vai precisar de um psicologo agora, dados da questão:
acesso = input()
lista = eval(acesso)

# Processamento e impressão dos resultados
resultado_final = soma(lista)
imprimir(resultado_final)
