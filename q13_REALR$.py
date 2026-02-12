#Entrada
Real = int(input("digite um valor em R$:"))
percentual = int(input("digite uma porcentagem de ex:(1% a 100%)"))

#processo
Aumento = Real * (1 + percentual/100)

#saida
print("o resultado do aumento e:", Aumento )