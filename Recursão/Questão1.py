#que saudades do meu cursão, digo dados da questão:
def definir_login(acesso):
    numeros = acesso.split(":")
    def calcular_soma(num):
        if num == 0:
            return 0
        else:
            if num % 2 == 0:
                return 2 * num + calcular_soma(num - 1)
            else:
                return 3 * num + calcular_soma(num - 1)
    login = ""
    for num_str in numeros:
        num = int(num_str)
        soma = calcular_soma(num)
        login += str(soma)
    return login

#ISQUECI MINHA SENHA KAKA QUAL FOI
def definir_senha(acesso):
    numeros = acesso.split(":")
    def calcular_fatorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * calcular_fatorial(num - 1)    
    senha = ""
    for num_str in numeros:
        num = int(num_str)
        fatorial = calcular_fatorial(num)
        senha += str(fatorial)
    return senha

acesso = input()
#qual é o meu nome mesmo? ah é lembrei
login_decifrado = definir_login(acesso)
#UUUUUUUU ENERGIA RECUPERADAAAAAAA, digo senha recuperadaaaaaaaa
senha_decifrada = definir_senha(acesso)

print("As credenciais de acesso da área secreta da fortaleza foram decodificadas com sucesso!")
print(f"Login: {login_decifrado}")
print(f"Senha: {senha_decifrada}")






    
