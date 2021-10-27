"""Faça um programa para loja de tintas
o programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros que custam R$ 80,00.

Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total"""

#regra de 3: 1 litro ---- 3 m2
        #18 litro --- xx m2

area = int(input("Informe a área a ser pintada: "))

litros = area//3
if area % 3 > 0:
    litros = litros + 1

quantidade = litros//18
if litros % 18 > 0:
    quantidade = quantidade + 1

preco_unit = 80

preco_total = quantidade*preco_unit

print("Você precisa de", litros, "litros de tintas", area)
print("A quantidade de latas de tintas que deverá ser comprada é de: ",quantidade)
print("O preço total da compra será de: R$ ", preco_total,",00")