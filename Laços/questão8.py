# dados da questão 
candidato_1 = input().strip()
candidato_2 = input().strip()

# Verificar se Kanye West é um dos candidatos
if candidato_1 != "Kanye West" and candidato_2 != "Kanye West":
    print("Sem o Ye, sem eleição!")
else:
    delegado1 = 0
    delegado2 = 0
    voto_popular_Cand_1 = 0
    voto_popular_Cand_2 = 0
    votacao = 1

    while votacao == 1:
        entrada = input().strip()
        if entrada == "FIM":
            votacao = 0
        else:
            estado, num_delegados = entrada.split(", ")
            num_delegados = int(num_delegados)

            votos_validos = 0
            while votos_validos == 0:
                votos_candidato1 = input().strip()
                if votos_candidato1 == "Taylor Swift roubou as urnas!":
                    print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
                else:
                    votos_candidato1 = int(votos_candidato1)
                    votos_candidato2 = input().strip()
                    if votos_candidato2 == "Taylor Swift roubou as urnas!":
                        print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
                    else:
                        votos_candidato2 = int(votos_candidato2)
                        votos_validos = 1

            total_votos = votos_candidato1 + votos_candidato2

            if votos_candidato1 > votos_candidato2:
                delegado1 += num_delegados
                voto_popular_Cand_1 += votos_candidato1
                vencedor_no_estado = candidato_1
                percentual_de_votos = (votos_candidato1 * 100) // total_votos
            else:
                delegado2 += num_delegados
                voto_popular_Cand_2 += votos_candidato2
                vencedor_no_estado = candidato_2
                percentual_de_votos = (votos_candidato2 * 100) // total_votos

            print(f"{vencedor_no_estado} obteve maioria no(a) {estado} com {percentual_de_votos}% dos votos.")

    if delegado1 > delegado2:
        vencedor = candidato_1
        total_delegados = delegado1
        total_votos = voto_popular_Cand_1
    else:
        vencedor = candidato_2
        total_delegados = delegado2
        total_votos = voto_popular_Cand_2

    print(f"Temos o resultado final! {vencedor} vence a disputa pela presidência, com o apoio de {total_delegados} delegados do colégio eleitoral e {total_votos} votos populares.")

    if vencedor == "Kanye West":
        print('\"Everybody wanted to know what I would do if I didn\'t win... I Guess We\'ll Never Know.\"')
    elif candidato_1 == "Kanye West" or candidato_2 == "Kanye West":
        print('\"Não tem problema, eu obtive o molho!\"')
