#ENtrada
idade_anos = int(input("digite a idade em anos:"))
idade_meses = int(input("digite a idade em meses:"))
idade_dias = int(input("digite a idade em dias:")) 

#processamento
total_dias = (idade_anos * 365) + (idade_meses * 30) + idade_dias

#saida
print(f"A idade total em dias é: {total_dias}")