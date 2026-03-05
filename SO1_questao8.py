#Declaração de variáveis
valor: float = 0.0
valornovo: float = 0.0

#Início
valor = float(input("Valor depositado na poupança: "))
valornovo = valor * 1.015
print ("Valor após 1 mês:", round(valornovo))
#Fim