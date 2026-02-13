#entrada
metros_inteiro = int(input("digite um numero inteiro de metro:"))

#processamento
quilometros = (metros_inteiro // 1000)
metros_restantes = (metros_inteiro % 1000)

#saida 

print(f"{metros_inteiro} metros correspondem a {quilometros} quilômetros e {metros_restantes} metros restantes:")