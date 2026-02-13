#entrada
dia_inteiro= int(input("digite um dia inteiro:"))

#processamento
semanas = dia_inteiro // 7
dias = dia_inteiro % 7

#saida
print(f"{dia_inteiro} dias correspondem a {semanas} semanas e {dias} dias restantes:")