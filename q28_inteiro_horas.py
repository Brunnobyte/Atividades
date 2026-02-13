#Entrada
Horas_inteiro = int(input("digite um número inteiro de horas:"))

#processamento
semanas = Horas_inteiro // 168
dias = (Horas_inteiro % 168) // 24
horas = Horas_inteiro % 24
print(f"{Horas_inteiro}horas correspondem a {semanas} semanas e {dias} dias e {horas} horas restantes:")