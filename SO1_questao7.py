#Declaração de variáveis
comp: int = 0
alt: int = 0
larg: int = 0
vol: int = 0

#Início
print ("Calculador de volume de paralelepípedos")
comp = int(input("Comprimento: "))
alt = int(input("Altura: "))
larg = int(input("Largura: "))
vol = comp * alt * larg
print ("Volume do paralelepípedo:", vol)
#Fim