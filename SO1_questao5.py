#Declaração de variáveis
ValorA: float = 0
ValorB: float = 0
ValorC: float = 0
delta: float = 0
raiz1: float = 0
raiz2: float = 0

#Início
ValorA = float(input("Valor A: "))
ValorB = float(input("Valor B: "))
ValorC = float(input("Valor C: "))
delta = ValorB ** 2 - (4 * ValorA * ValorC)
raiz1 = (-ValorB + (delta ** 0.5)) / (2 * ValorA)
raiz2 = (-ValorB - (delta ** 0.5)) / (2 * ValorA)
print ("Raíz 1:", raiz1)
print ("Raíz 2:", raiz2)

#Fim