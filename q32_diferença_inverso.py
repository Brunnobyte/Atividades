#entrada
Numero_inteiro = int(input("digite 3 numeros inteiro:"))

#processamento / calcular e escrever a diferença entre a o numero e o seu inverso
inversao = int(str(Numero_inteiro)[::-1])
diferença = Numero_inteiro - inversao

#saida
print("o resultado da diferença do numero com seu inverso e:", diferença)