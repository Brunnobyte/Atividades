#Entrada
Numero_inteiro = int(input("digite um numero inteiro de 4 digitos:"))

#processamento / calcular e escrever a soma dos elementos do numero
milhar = Numero_inteiro // 1000
resto_milhar = Numero_inteiro % 1000
centena = resto_milhar // 100
resto_centena = resto_milhar % 100
dezena = resto_centena // 10
resto_dezena = resto_centena % 10
unidade = resto_dezena

#saida
print(f"A soma dos elementos do número {Numero_inteiro} é: {milhar + centena + dezena + unidade}")