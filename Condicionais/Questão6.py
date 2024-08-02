piloto_a = input ()
tempo_a = float (input())
piloto_b = input ()
tempo_b = float (input())
piloto_c = input ()
tempo_c = float (input())

print ("E o Pódio do GP de Mônaco é:")
if tempo_a < tempo_b and tempo_a < tempo_c:
    print (f"{piloto_a} está no lugar mais alto do pódio com tempo de {tempo_a} horas de corrida.")
elif tempo_b > tempo_a and tempo_b < tempo_c:
    print (f"{piloto_b} está no segundo lugar do pódio com tempo de {tempo_b} horas de corrida.")
elif tempo_c > tempo_a and tempo_c > tempo_b:
    print (f"{piloto_c} está no terceiro lugar do pódio com tempo de {tempo_c} horas de corrida.")
else:
    print (f"Galvão, temos um momento histórico da Fórmula 1, {piloto_a} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_a} horas de prova.")


if tempo_b < tempo_a and tempo_b < tempo_c:
    print (f"{piloto_b} está no lugar mais alto do pódio com tempo de {tempo_b} horas de corrida.")
elif tempo_a > tempo_b and tempo_a < tempo_c:
    print (f"{piloto_a}  está no segundo lugar do pódio com tempo de {tempo_a} horas de corrida.")
elif tempo_c > tempo_b and tempo_c > tempo_a:
    print (f"{piloto_c} está no terceiro lugar do pódio com tempo de {tempo_c} horas de corrida.")
else:
    print (f"Galvão, temos um momento histórico da Fórmula 1, {piloto_b} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_b} horas de prova")

if tempo_c < tempo_a and tempo_c < tempo_b:
    print (f"{piloto_c} está no lugar mais alto do pódio com tempo de {tempo_c} horas de corrida.")
elif tempo_a > tempo_c and tempo_a < tempo_c:
    print (f"{piloto_a} está no segundo lugar do pódio com tempo de {tempo_a} horas de corrida.")
elif tempo_b > tempo_c and tempo_b > tempo_a:
    print (f"{piloto_b} está no terceiro lugar do pódio com tempo de {tempo_b} horas de corrida.")
else:
    print (f"Galvão, temos um momento histórico da Fórmula 1, {piloto_c} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_c} horas de prova.")

if tempo_c < tempo_a and tempo_c < tempo_b:
    print (f"{piloto_c} está no lugar mais alto do pódio com tempo de {tempo_c} horas de corrida.")
elif tempo_b > tempo_c and tempo_b < tempo_a:
    print (f"{piloto_b} está no segundo lugar do pódio com tempo de {tempo_b} horas de corrida.")
elif tempo_a > tempo_b and tempo_a > tempo_c:
    print (f"{piloto_a} está no terceiro lugar do pódio com tempo de {tempo_a} horas de corrida.")
else:
    print (f"Galvão, temos um momento histórico da Fórmula 1, {piloto_c} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_c} horas de prova.")

if tempo_a < tempo_b and tempo_a < tempo_c:
    print (f"{piloto_a} está no lugar mais alto do pódio com tempo de {tempo_a} horas de corrida.")
elif tempo_c > tempo_a and tempo_c < tempo_b:
    print (f"{piloto_c} está no segundo lugar do pódio com tempo de {tempo_c} horas de corrida.")
elif tempo_b > tempo_a and tempo_b > tempo_c:
    print (f"{piloto_b} está no terceiro lugar do pódio com tempo de {tempo_b} horas de corrida.")
else:
     print (f"Galvão, temos um momento histórico da Fórmula 1, {piloto_a} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_a} horas de prova.")

if tempo_b < tempo_a or tempo_b < tempo_c:
    print (f"{piloto_b} está no lugar mais alto do pódio com tempo de {tempo_b} horas de corrida.")
elif tempo_c > tempo_b or tempo_c < tempo_a:
    print (f"{piloto_c} está no segundo lugar do pódio com tempo de {tempo_c} horas de corrida.")
elif tempo_a > tempo_b and tempo_a > tempo_c:
     print (f"{piloto_a} está no terceiro lugar do pódio com tempo de {tempo_a} horas de corrida.")
else:
    print (f"Galvão, temos um momento histórico da Fórmula 1, {piloto_b} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_b} horas de prova")
