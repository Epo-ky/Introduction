#dados da questão
nota = int(input())

boa_pratica_n = 0
ma_pratica_n = 0

#eita como calcula coisa boa
if nota != 0:

    for b in range(nota): 
        pratica = input()
        if pratica == "Programar utilizando uma boa IDE":
            boa_pratica_n += 3
        elif pratica == "Códigos limpos e organizados":
            boa_pratica_n += 10
        elif pratica == "Nomenclatura objetiva e de fácil identificação de variáveis":
            boa_pratica_n += 7
        elif pratica == "Assistir às aulas do REDU":
            boa_pratica_n += 10
        elif pratica == "Comentários significativos":
            boa_pratica_n += 5
        elif pratica == "Evitar repetições desnecessárias de códigos":
            boa_pratica_n += 5
        elif pratica == "Tirar dúvidas com os monitores e professores":
            boa_pratica_n += 10
  #eita o homem que calculava erros  
        if pratica == "Programar sem utilizar IDE":
            ma_pratica_n += -5
        elif pratica == "Código bagunçado e mal estruturado":
            ma_pratica_n += -6
        elif pratica == "Nomenclatura confusa e difícil de identificar variáveis":
            ma_pratica_n += -5
        elif pratica == "Não tirar dúvidas com professores e monitores":
            ma_pratica_n += -10

if nota == 0:
    media = 0
else:media = (boa_pratica_n + ma_pratica_n) / nota

#passamos por media?!
if media < 3:
    print ("É melhor voltar a cantar mesmo!")
elif media >= 3 and media < 7:
    print ("Vai precisar se esforçar um pouco mais, meu cantor!")
elif media == 7:
    print ("Na conta certa!")
elif media > 7 and media <9:
    print ("Nasceu para programar!")
elif media > 9:
    print ("Já pode ser chamado de Kanye, the dev, West!")
elif media < 0:
    media = 0
elif media > 10:
    media = 10



