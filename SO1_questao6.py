#Declaração de variáveis
ValorX: int = 0
ValorY: int = 0
Dummy: int = 0
#Início
print ("Invertedor de valor")
ValorX = int(input("Valor X: "))
ValorY = int(input("Valor Y: "))
Dummy = ValorX
ValorX = ValorY
ValorY = Dummy
print ("Novo valor X:", ValorX)
print ("Novo valor Y:", ValorY)
#Fim