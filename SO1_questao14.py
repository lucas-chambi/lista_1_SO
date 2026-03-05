#Declaração de variáveis
angulo_a: int = 0
angulo_b: int = 0
angulo_c: int = 0

#Início
angulo_a = int(input("Ângulo A: "))
angulo_b = int(input("Ângulo B: "))
angulo_c = 180 - (angulo_a + angulo_b)
print ("Valor do terceiro ângulo:", angulo_c)
#Fim