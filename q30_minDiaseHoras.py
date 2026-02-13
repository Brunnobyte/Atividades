#entrada
minutos_inteiro = int(input("digite uma qunatidade em minutos:"))

#processamento
#primeiros calcularemos qunatos dias darão essa quantidade de minutos com o % calcularemos quantas horas e minutos restam
dias = minutos_inteiro // 1440
horas = minutos_inteiro // 60
minutos = minutos_inteiro % 60 

#saida
print(f"{minutos_inteiro} minutos são {dias} dias que correspondem a {horas} horas e {minutos} minutos:")