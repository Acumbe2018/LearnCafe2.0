"""2.faça um programa que pergunte  quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário do mês"""

ganho_hora = int(input("Quanto você ganha por hora/trabalhada? R$ "))
hora_trabalhada = int(input("Quantas horas você trabalha por mês ?  "))

sal = ganho_hora*hora_trabalhada

print("Seu salário por mês é de R$: ", sal)