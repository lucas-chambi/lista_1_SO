#Declaração de variáveis
horas: int = 0
valor_hora: int = 0
perc_desconto: int = 0
num_desce: int = 0
salario_brt: int = 0
salario_liq: int = 0
salario_final: int = 0

#Início
horas = int(input("Horas trabalhadas: "))
valor_hora = int(input("Valor por hora: "))
perc_desconto = int(input("Percentual do desconto: "))
num_desce = int (input("Número de descendentes: "))
salario_brt = horas * valor_hora
salario_liq = salario_brt * (1 - perc_desconto / 100)
salario_final = salario_liq + 100 * num_desce
print ("Salário que será recebido: R$", salario_final)
#Fim