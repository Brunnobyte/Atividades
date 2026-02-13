#entrada
Numero_inteiro= int(input("digite um numero de 3 digitos:"))

#processamento
inverso = int(str(Numero_inteiro)[::-1])
soma = Numero_inteiro + inverso
#saida
print("digite a soma do numero com seu inverso:", soma)