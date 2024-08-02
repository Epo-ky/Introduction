#Dikastis por favor cai não, quer dizer, dados da questão:
locais = [
    ["Torre do Mago", 700, "06:00", "23:00"],
    ["Rancho da Marnie", 260, "09:00", "16:00"],
    ["Saloon", 1200, "12:00", "00:00"],
    ["Armazém do Pierre", 1100, "09:00", "17:00"],
    ["Casa do Prefeito", 1500, "08:30", "22:00"],
    ["Peixaria", 1900, "09:00", "17:00"],
    ["Museu", 1870, "08:00", "18:00"],
    ["Ferreiro", 1700, "09:00", "16:00"],
    ["Mercado Joja", 1800, "09:00", "23:00"],
    ["Carpintaria", 1500, "09:00", "17:00"],
    ["Minas", 1850, "00:00", "23:59"],
    ["Centro Comunitário", 1300, "00:00", "23:59"]
]
#Lista dos suspeitos
suspeitos = ["Artur", "João", "Luana", "Pedro Elias", "Thomaz", "Welton"]

alibis = []
#Laço dos alibis
for _ in range(len(suspeitos)):
    alibi = input()
    alibis.append(alibi.split(" - "))

locais_invalidos = []
nome_locais_invalidos = []
#local e horario dos meliantes
for i in range(len(alibis)):
    nome, horario, local = alibis[i]
    local_valido = False
    for j in range(len(locais)):
        if local == locais[j][0]:
            local_valido = True
    if not local_valido:
        locais_invalidos.append([nome, local])
        if (nome,local) not in locais_invalidos:
            nome_locais_invalidos.append(local)
#ordena familia
if len(locais_invalidos) > 0:
    nome_locais_invalidos.sort()
    if len(nome_locais_invalidos) == 1:
        print(f"Esse lugar {nome_locais_invalidos[0]} nem existe! {locais_invalidos[0][0]} foi quem roubou os melões!")
    else:
        nome_suspeitos_invalidos = [nome for nome, local in locais_invalidos]
        nome_suspeitos_invalidos.sort()
        print(f"{', '.join(nome_locais_invalidos)} nem existem! {', '.join(nome_suspeitos_invalidos)} roubaram os melões!")

else:

    horario_invalido = []
    nome_horario_invalido = []
#o for mais dificil da minha vida, até agora.
    for i in range(len(alibis)):
        nome, horario, local = alibis[i]
        for j in range(len(locais)):
            if local == locais[j][0]:
                abertura = locais[j][2]
                fechamento = locais[j][3]
                h_a, m_a = int(abertura.split(":")[0]), int(abertura.split(":")[1])
                h_f, m_f = int(fechamento.split(":")[0]), int(fechamento.split(":")[1])
                h_h, m_h = int(horario.split(":")[0]), int(horario.split(":")[1])
                horario_valido = False

                if (h_a < h_h or (h_a == h_h and m_a <= m_h)) and (h_h < h_f or (h_h == h_f and m_h <= m_f)):
                    horario_valido = True
                if fechamento == "00:00" and ((h_a < h_h or (h_a == h_h and m_a <= m_h)) or (h_h < h_f or (h_h == h_f and m_h <= m_f))):
                    horario_valido = True
                
                if not horario_valido:
                    horario_invalido.append([nome, local, fechamento])
                    if local not in nome_horario_invalido:
                        nome_horario_invalido.append(local)
#horarios
    if len(horario_invalido) > 0:
        nome_horario_invalido.sort()
        if len(nome_horario_invalido) == 1:
            print(f"{nome_horario_invalido[0]} nem estava aberto nessa hora, esse lugar foi fechado às {horario_invalido[0][2]}! {horario_invalido[0][0]} roubou os melões!")
        else:
            nomes_suspeitos_horarios_invalidos = [nome for nome, local, fechamento in horario_invalido]
            nomes_suspeitos_horarios_invalidos.sort()
            print(f"{', '.join(nome_horario_invalido)} nem estavam abertos nessa hora, esses lugares foram fechados beeem antes! {', '.join(nomes_suspeitos_horarios_invalidos)} se uniram e roubaram os melões!")
#distancias
    else:
        distancia = []
        for i in range(len(alibis)):
            nome, horario, local = alibis[i]
            for j in range(len(locais)):
                if local == locais[j][0]:
                    distancia.append([nome, locais[j][1]])
        
        menor_distancia = min([dist[1] for dist in distancia])
        suspeitos_mais_proximos = [nome for nome, distancia in distancia if distancia == menor_distancia]
        suspeitos_mais_proximos.sort()
#resultado da pericia
        if len(suspeitos_mais_proximos) == 1:
            print(f"{suspeitos_mais_proximos[0]} estava a {menor_distancia} metros da plantação! Agora é nosso suspeito número um. Fiquem de olho!")
        else:
            print(f"{', '.join(suspeitos_mais_proximos)} estavam a {menor_distancia} metros da plantação! Eles podiam estar cometendo o roubo juntos... Fiquem de olho!")






