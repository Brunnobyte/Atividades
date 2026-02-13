#entrada
Segundos_inteiro = int(input("digite um tempo em segundos:"))

#processamento
horas = Segundos_inteiro // 3600
minutos = (Segundos_inteiro % 3600) // 60
segundos = Segundos_inteiro % 60

#saida
print(f"{Segundos_inteiro}segundos correspondem a {horas} horas e {minutos} minutos sobrando {segundos} segundos restantes: ")