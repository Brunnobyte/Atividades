#Entrada
nota1 = float(input("digite a primeira nota:,"))
peso1 = float(input("digite o peso da nota 1"))

nota2 = float(input("digite a segunda nota"))
peso2 = float(input("digite o peso da nota 2"))

nota3 = float(input("digite a terceira nota"))
peso3 = float(input("digite o peso da nota 3"))

#processamento
media = (nota1 * peso2) + (nota2 * peso2) + (nota3 * peso3) 
mendia_ponderada = media / (peso1 + peso2 + peso3 )
#saida
print(f"> a media ponderada e {mendia_ponderada}.")