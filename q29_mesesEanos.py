#Entrada
Meses_inteiro = int(input("digite uma quantidade de meses:"))

#processamento
#primeiro preciso calcular quantos anos e depois quantos meses restam 
anos = Meses_inteiro // 12
meses = Meses_inteiro % 12
 
#saida
print(f"{Meses_inteiro} meses que correspondem a {anos} anos restando {meses} meses")