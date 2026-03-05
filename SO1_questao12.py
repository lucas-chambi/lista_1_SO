#Declaração de valores
ano_nasc: int = 0
ano_atual: int = 0
idade: int = 0
idade17anos: int = 0

#Início
ano_nasc = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))
idade = ano_atual - ano_nasc
idade17anos = idade + 17
print ("Idade atual:", idade)
print ("Idade após 17 anos:", idade17anos)
#Fim