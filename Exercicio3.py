"""1. faça um programa que peça as 4 notas bimestrais e mostre a média do aluno"""

#programa 1#

Nota1 = int(input("Informe sua nota do primeiro bimestre:"))
Nota2 = int(input("Informe sua nota do segundo bimestre:"))
Nota3 = int(input("Informe sua nota do terceiro bimestre:"))
Nota4 = int(input("Informe sua nota do quarto bimestre:"))

media_geral = [Nota1,Nota2,Nota3,Nota4]

average = (Nota1+Nota2+Nota3+Nota4) / (len(media_geral))
#Função len conta o número de itens de uma lista e retorna um número#

print("Sua Média do Ano é:", average)


