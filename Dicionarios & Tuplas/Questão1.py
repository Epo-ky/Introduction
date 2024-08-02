#Repertorio novo no aralto gente...
albuns = [
    ("Abbey Road", "The Beatles", "1969", "Rock"),
    ("The Dark Side of the Moon", "Pink Floyd", "1973", "Rock"),
    ("Riot!", "Paramore", "2007", "Rock"),
    ("Fearless", "Taylor Swift", "2008", "Pop"),
    ("Da Lama ao Caos", "Chico Science e Nação Zumbi", "1994", "Manguebeat"),
    ("Gal Costa", "Gal Costa", "1969", "MPB"),
    ("Sim", "Vanessa da Mata", "2007", "MPB"),
    ("As 20 Melhores", "Luiz Gonzaga", "2004", "Forró"),
    ("O Melhor de Dominguinhos", "Dominguinhos", "2013", "Forró"),
    ("Alucinação", "Belchior", "1976", "MPB"),
    ("Samba Esquema Novo", "Jorge Ben Jor", "1963", "Samba")
]

mensagens_saida = []
#eu prometi não mais te procurar... mas hoje não é meu dia de sorte, achei os dados da questão no celular:
def adicionando_album(nome_album):
    nome_artista = input()
    ano_lancamento = int(input())
    genero_musical = input().capitalize()

    novo_album = (nome_album, nome_artista, ano_lancamento, genero_musical)
    albuns.append(novo_album)

    generos_existentes = {album[3].lower() for album in albuns[:-1]}
    novo_genero = genero_musical.lower() not in generos_existentes

    mensagem = f"Este foi o novo álbum adicionado:\n- {nome_album} do/da artista/banda {nome_artista} lançado em {ano_lancamento}"
    mensagens_saida.append(mensagem)
#não te esqueci me diz como é que pode, você me tirou do novo genero ( ou colocou)
    if novo_genero:
        mensagem = "Oba, você adicionou um novo estilo musical ao catálogo!"
        mensagens_saida.append(mensagem)
# e eu não te tirei da mente, a consulta por genero não apaga, a saudade da gente amor...
def consultar_por_genero(albuns, genero):
    genero_aux = genero.capitalize()
    encontrados = [album for album in albuns if album[3].capitalize() == genero_aux]
    if encontrados:
        mensagem = f"Nessa galeria há {len(encontrados)} albuns de {genero}. Os albuns encontrados foram:"
        mensagens_saida.append(mensagem)
        for album in encontrados:
            mensagem = f"- {album[0]} do/da artista/banda {album[1]} lançado em {album[2]}"
            mensagens_saida.append(mensagem)
    else:
        mensagem = "Você vai precisar adicionar um novo álbum ao catálogo! Não encontramos nenhum álbum desse estilo musical!"
        mensagens_saida.append(mensagem)

executando = True
#amor... ja que me ensinou a laçar, ja que me ensinou listar, me ensina por favor como essa questão passar.
while executando:
    comando = input()

    if comando == "CONSULTAR":
        genero = input()
        consultar_por_genero(albuns, genero)
    elif comando == "FIM":
        executando = False
    else:
        adicionando_album(comando)
    if mensagens_saida:
        for mensagem in mensagens_saida:
            print(mensagem)
        mensagens_saida.clear()

