"""Faça um programa para loja de tintas
o programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros que custam R$ 80,00 ou em galões de 4 litros que custam R$ 25,00.

Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total, nas 3 situações:
comprar apenas latas de 18 litros
comprar apenas galóes de 4 litros
misturar latas e galóes de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, numeros inteiros."""

#cobertura = 1litro == 6 metros2
#lata = 18litros
#galões = 4 litros
#custo = 80,00 a lata
#custo2 = 25 galões

area = int(input("Informe o tamanho da area que será pintada: "))
#acrescentado 10% de folga na area
area = area*1.1

excesso = area-int(area) ##aqui estamos pegando as casas decimais da area
area = int(area) ##Aqui retiramos a parte inteira da area

if excesso > 0:
    area = area + 1 #arredondando para cima

litros1, litros2 = area//6, area//6
lata = litros1//18
galao = litros2//4
custo_lata = 80
custo_galao = 25

if area % 6 > 0:
   litros1 = (litros1+1)
if litros1 % 18 > 0:
    lata = lata+1
if area % 6 > 0:
    litros2 = (litros2+1)
if litros2 % 4 > 0:
    galao = galao+1

preco_por_lata = custo_lata*lata
preco_por_galao = custo_galao*galao

print("Para a area de ", area, "m2")
print("Você precisará de", lata, "lata de 18 litros sendo", "ao preço total de: R$",preco_por_lata,",00")
print("Você precisará de", galao, "galão de 4 litros sendo","ao preço total de: R$",preco_por_galao,",00")