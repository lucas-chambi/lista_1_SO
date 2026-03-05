#Declaração de variáveis
alimkg: int = 0
alimgrama: int = 0
dias: int = 0

#início
alimkg = float(input("Quantidade de alimentos em kilos: "))
alimgrama = alimkg * 1000
dias = alimgrama / 50
print ("Quantidade de dias:", dias)
#Fim