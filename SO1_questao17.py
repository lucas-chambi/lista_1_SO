#Declaração de variáveis
tempo_perc: float = 0.0
vel_media: float = 0.0
litros_gastos: float = 0.0

#Início
tempo_perc = int(input("Tempo do percurso em horas: "))
vel_media = int(input("Velocidade média em km/h: "))
litros_gastos = (tempo_perc * vel_media) / 12
print ("Quant. de litros gastos:", litros_gastos)
#Fim