"""Escrever um programa que:
 1) Imprima dois números inteiros
 2) imprima a soma destes números
 3) Imprima a subtração destes números
 4) Imprima a multiplicação destes números
 5) imprima a divisáo normal
 6) Imprima a divisão inteira
 7) Imprima o resto da divisão do maior pelo menor"""

x = 15
y = 10
soma = x+y
subtraçao = x-y
mult = x*y
div_normal = x/y
div_inteira = x//y
resto_divisao= x % y

print(1,"os números inteiros são",x,y)
print(2,"A soma será",soma)
print(3,"A subtração será",subtraçao)
print(4,"A multiplicação será", mult)
print(5,"A Divisão normal será",div_normal)
print(6,"A divisão dos números inteiros será", div_inteira)
print(7,x,"resto",y,"=",resto_divisao)
