#Declaração de valores
cateto1: int = 0
cateto2: int = 0
hipotenusa: int = 0

#Início
cateto1 = int(input("Valor do primeiro cateto: "))
cateto2 = int(input("Valor do segundo cateto: "))
hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
print ("Hipotenusa do triângulo retângulo:", hipotenusa)
#Fim