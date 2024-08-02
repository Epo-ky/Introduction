#A partir daqui é so sofrimento
def palavra_contida(linha_orc, palavra):

    if not palavra:
        return True
    if linha_orc.startswith(palavra):
        return True
    if len(linha_orc) > len(palavra):
        return palavra_contida(linha_orc[1:], palavra)
    
    return False
#Ele sabe ler, ja eu to quase analfabeto :((
def ler_frases(linha_orc, frases, numero_frases=1):

    if not frases:
        print("Pensou que me enganaria? A magia da recursão me disse que a senha não pode ser nenhuma dessas")
        return
    
    frases_atual = frases.pop(0)
    palavras = frases_atual.split()
    palavras_normalizada = [palavra.lower() for palavra in palavras]
#tem muita palavra contida nesse hobgoblin
    todas_palavras_contidas = True
    for palavra in palavras_normalizada:
        if not palavra_contida(linha_orc, palavra):
            todas_palavras_contidas = False

    if todas_palavras_contidas:
        print(f"Já sei, a senha é a frase número {numero_frases}")
        return
#Chamando a função
    ler_frases(linha_orc, frases, numero_frases + 1)
#vamos ver se tem fim ne 
def leitura(linha_orc=None, frases=None, numero_frases=1):
    if linha_orc is None:
        linha_orc = input().lower()
    if frases is None:
        frases = [] 

    linha = input()
    if linha == "Decifra-me ou te devoro!":
        ler_frases(linha_orc, frases)
    else:
        frases.append(linha)
        leitura(linha_orc, frases, numero_frases + 1)
#função IN to função
def principal():
    leitura()

principal()
