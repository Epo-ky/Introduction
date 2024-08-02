#... ja não existe animo pra piadas, apenas dor, dados da questão:
linha_antes = input()
linha_depois = input()
#os moveiszinhos zeradinhos
c_antes, p_antes, l_antes, t_antes, m_antes, tt_antes, b_antes = 0, 0, 0, 0, 0, 0, 0
c_depois, p_depois, l_depois, t_depois, m_depois, tt_depois, b_depois = 0, 0, 0, 0, 0, 0, 0
#tapoxa laçando e calculando
for i in range(0, 60, 10):
    for j in range(10):
        char = linha_antes[i + j]
        if char == "C":
            c_antes += 1
        elif char == "P":
            p_antes += 1
        elif char == "L" and j < 9 and linha_antes[i + j + 1] == "L":
            l_antes += 1
        elif char == "T" and j < 9 and linha_antes[i + j + 1] == "T" and i < 50 and linha_antes[i + 10 + j] and linha_antes[i + 10 + j + 1] == "T":
            t_antes += 1
        elif char == "M" and j < 9 and linha_antes[i + j + 1] == "M" and i < 50 and linha_antes[i + 10 + j] and linha_antes[i + 10 + j + 1] == "M":
            m_antes += 1
        elif char == "t" and j < 9 and linha_antes[i + j + 1] == "t" and i < 50 and linha_antes[i + 10 + j] and linha_antes[i + 10 + j + 1] == "t":
            tt_antes += 1
        elif char == "B" and j < 9 and linha_antes[i + j + 1] == "B" and i < 40 and linha_antes[i + 10 + j] and linha_antes[i + 10 + j + 1] == "B" and linha_antes[i + 20 + j] == "B" and linha_antes[i + 20 + j + 1] == "B":
            b_antes += 1
#antes, depois, antes, depois.
for i in range(0, 60, 10):
    for j in range(10):
        char = linha_depois[i + j]
        if char == "C":
            c_depois += 1
        elif char == "P":
            p_depois += 1
        elif char == "L" and j < 9 and linha_depois[i + j + 1] == "L":
            l_depois += 1
        elif char == "T" and j < 9 and linha_depois[i + j + 1] == "T" and i < 50 and linha_depois[i + 10 + j] and linha_depois[i + 10 + j + 1] == "T":
            t_depois += 1
        elif char == "M" and j < 9 and linha_depois[i + j + 1] == "M" and i < 50 and linha_depois[i + 10 + j] and linha_depois[i + 10 + j + 1] == "M":
            m_depois += 1
        elif char == "t" and j < 9 and linha_depois[i + j + 1] == "t" and i < 50 and linha_depois[i + 10 + j] and linha_depois[i + 10 + j + 1] == "t":
            tt_depois += 1
        elif char == "B" and j < 9 and linha_depois[i + j + 1] == "B" and i < 40 and linha_depois[i + 10 + j] and linha_depois[i + 10 + j + 1] == "B" and linha_depois[i + 20 + j] == "B" and linha_depois[i + 20 + j + 1] == "B":
            b_depois += 1
#Vamos descobrir oque acontece nos proximos capitulos dos moveis novos
moveis_novos = moveis_jogados_fora = moveis_fora_de_lugar = 0
#calculando registro de moveis que mudaram de lugar, moveis que o dono levou e as novidades novas.
if c_depois > c_antes:
    moveis_novos += 1
elif c_depois < c_antes:
    moveis_jogados_fora += 1

if p_depois > p_antes:
    moveis_novos += 1
elif p_depois < p_antes:
    moveis_jogados_fora += 1

if l_depois > l_antes:
    moveis_novos += 1
elif l_depois < l_antes:
    moveis_jogados_fora += 1

if t_depois > t_antes:
    moveis_novos += 1
elif t_depois < t_antes:
    moveis_jogados_fora += 1

if m_depois > m_antes:
    moveis_novos += 1
elif m_depois < m_antes:
    moveis_jogados_fora += 1

if tt_depois > tt_antes:
    moveis_novos += 1
elif tt_depois < tt_antes:
    moveis_jogados_fora += 1

if b_depois > b_antes:
    moveis_novos += 1
elif b_depois < b_antes:
    moveis_jogados_fora += 1

for i in range(len(linha_antes)):
    if linha_antes[i] != linha_depois[i]:
        moveis_fora_de_lugar += 1


#Thomaz o espalha lixo, grande vilão do pica-pau!
if moveis_novos >= 3:
    print("Thomaz bagunçou a casa. Ele sempre enche a casa de bugiganga!!.")
#QUE ZONA É ESSA NA MINHA CASA :((
elif moveis_novos > 0 and (c_antes != c_depois or p_antes != p_depois or l_antes != l_depois or t_antes != t_depois or m_antes != m_depois or tt_antes != tt_depois or b_antes != b_depois):
    print("Caramba, a casa tá uma bagunça! Não sei quem foi o responsável.")
#Pedrinho passando o rodo.
elif p_antes > p_depois:
    print("Poxa, Pedro Elias! Não basta vender toda a plantação de melões, ainda quer vender minha planta??")
#o dono levou, ou melhor, welton.
elif c_antes > 0 or p_antes > 0 or l_antes > 0 or t_antes > 0 or m_antes > 0 or tt_antes > 0 or b_antes > 0:
    if c_depois == 0 and p_depois == 0 and l_depois == 0 and t_depois == 0 and m_depois == 0 and tt_depois == 0 and b_depois == 1:
        print("CADÊ MEUS MÓVEIS?!?! SÓ FICOU A CAMA! Só pode ter sido Welton.")
#joão o bagunção
    elif moveis_fora_de_lugar >= 5:
        print("João bagunçou a casa. Não aguento mais tudo fora do lugar! Toda vez isso.")
#alguma coisa está diferente? OU SERÁ QUE NÃO!
    elif linha_antes != linha_depois:
        print("Hum, tem algo diferente aqui... Deve ter sido só impressão minha.")
    #Tudo certo, nada errado.
    else:
        print("Ufa! A casa tá do jeitinho que eu deixei.")
else:
        print("Ufa! A casa tá do jeitinho que eu deixei.")
        
