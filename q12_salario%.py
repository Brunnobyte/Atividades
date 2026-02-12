# Entrada
salario = int(input("Digite um número inteiro:"))
novo_salario = float(input("Digite o percentual de aumento:(1% a 100%) "))


#processo
aumento = salario * (1 + novo_salario/100)

#saida 
print("o resultado da soma do salario + o percentual e:", aumento )