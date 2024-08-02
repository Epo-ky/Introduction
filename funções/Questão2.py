#Adição soma e soma
def adicao(status_pokemon, valor_item):
    resultado = status_pokemon + valor_item
    print(f"Ao dar esse item eu esperava uma operação de Adição e com isso o status do meu Pokemon de {int(status_pokemon)} foi para {int(resultado)}")
    return resultado
#Perde e subtrai, reduzindo.
def subtracao(status_pokemon, valor_item):
    resultado = status_pokemon - valor_item
    print(f"Ao dar esse item eu esperava uma operação de Subtração e com isso o status do meu Pokemon de {int(status_pokemon)} foi para {int(resultado)}")
    return resultado
#Multiplicaaaaaaaaaaaaaa
def multiplicacao(status_pokemon, valor_item):
    resultado = status_pokemon * valor_item
    print(f"Ao dar esse item eu esperava uma operação de Multiplicação e com isso o status do meu Pokemon de {int(status_pokemon)} foi para {int(resultado)}")
    return resultado
#dividi ai pow
def divisao(status_pokemon, valor_item):
    if valor_item != 0:
        resultado = status_pokemon / valor_item
        print(f"Ao dar esse item eu esperava uma operação de Divisão e com isso o status do meu Pokemon de {int(status_pokemon)} foi para {int(resultado)}")
        return resultado
    else:
        print("não existe divisão por 0")
        return status_pokemon
#MAIS POTENCIAAAAAAAAAAAA
def potencia(status_pokemon, valor_item):
    resultado = status_pokemon ** valor_item
    print(f"Ao dar esse item eu esperava uma operação de Potenciação e com isso o status do meu Pokemon de {int(status_pokemon)} foi para {int(resultado)}")
    return resultado
#Radiação kkkkkkkkkkkk
def radiciacao(status_pokemon, valor_item):
    resultado = status_pokemon ** (1/valor_item)
    print(f"Ao dar esse item eu esperava uma operação de Radiciação e com isso o status do meu Pokemon de {int(status_pokemon)} foi para {int(resultado)}")
    return resultado

def principal():
    quantidade_operacoes = int(input())

    if quantidade_operacoes == -1:
        print("Acho que vou desistir, confio no meu Pokemon sem nenhum item!")
        return
    
    for _ in range(quantidade_operacoes):
        acao = input()
        status_pokemon = int(input())
        valor_item = int(input())
    #O MAIS FORTEEEEEEEEEE
        if acao == "Quero deixar meu Pokemon mais forte!":
            status_pokemon = adicao(status_pokemon, valor_item)
    #Hm suspeito esses cogumelinho, uma vez eu vi um encanador fica gigante com isso.
        elif acao == "Deixa eu testar esse cogumelo estranho…":
            status_pokemon = subtracao(status_pokemon, valor_item)
    #É... será necessario evoluir.
        elif acao == "Vou evoluir meu Pokemon!":
            status_pokemon = multiplicacao(status_pokemon, valor_item)
    #comida ruim é assim:
        elif acao == "Não! Essa comida diminui o ataque…":
            status_pokemon = divisao(status_pokemon, valor_item)
    #Dalhe mega stone nele a menos que seja um flygon né xD
        elif acao == "E se eu colocar essa Mega Stone…":
            status_pokemon = potencia(status_pokemon, valor_item)
    #Megastone do flygon desenvolvida em vozes da cabeça de alguém
        elif acao == "Essa Mega Stone está estranha...":
            status_pokemon = radiciacao(status_pokemon, valor_item)
    #oque diabos vc ta tentando fazer?
        else:
            print("Ação não reconhecida.")
#VOU VENCER, grande Mulan
    print("Agora tenho confiança que vou vencer!")


principal()
