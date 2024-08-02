#Informações
construtor1 = input ()
posicao1 = int(input())
salario1 = int (input())
#informações 2 o retorno:
construtor2 = input ()
posicao2 = int(input())
salario2 = int(input())
#dados resultados
resultado = 0 
resultado2 = 0 
#organizações:
if construtor1 == "Red Bull": 
   resultado = (resultado + 3)
elif construtor1 == "McLaren":
    resultado = (resultado + 2) 
elif construtor1 == "Aston Martin" or construtor1 == "Mercedes":
    resultado = (resultado + 1)

#posição das organizações:
if posicao1 == 1:
   resultado = (resultado + 3)
elif posicao1 == 2:
    resultado = (resultado + 2)
if posicao1 != 3:
    resultado += (salario1 // 4)
elif posicao1 == 3 and construtor1 != "Red Bull":
    resultado = 0

# organizações parte2:
if construtor2 == "Red Bull":
    resultado2 = (resultado2 + 3)
elif construtor2 == "McLaren":
    resultado2 = (resultado2 + 2)
elif construtor2 == "Aston Martin" or construtor2 == "Mercedes":
    resultado2 = (resultado2 + 1)

#posições da organizaçoes 2
if posicao2 == 1:
    resultado2 = (resultado2 + 3)
elif posicao2 == 2:
    resultado2 = (resultado2 + 2)
if posicao2 != 3:
    resultado2 += (salario2 // 4)
elif posicao2 == 3 and construtor2 != "Red Bull":
    resultado2 = 0

#Ferrari exclusiva
if construtor1 == "Ferrari":
    resultado = 0
if construtor2 == "Ferrari":
    resultado2 = 0




#finalmente os resultados
if resultado > resultado2:
    print (f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor1}, que pontuou {resultado}.")
elif resultado2 > resultado:
    print (f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor2}, que pontuou {resultado2}.")
elif resultado == resultado2 and resultado > 0 and resultado2 >0:
    print ("As duas são ótimas opções! Vamos, Sainz!!") 
else:
    print ("Depois de tantas temporadas, o Sainz vai descançar em 2025.")
