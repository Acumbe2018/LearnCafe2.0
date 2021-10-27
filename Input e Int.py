"""Função input e Int"""

x = input("Entre com sua mensagem ou número:")

x = int(x)
#função input sempre retornará como string (coisa).#
#função int converte a string(coisa) em número#
print(type(x))

num1 = int(input("Digite seu primeiro número:"))
num2 = int(input("Digite seu segundo número:"))

print(num1, "+",num2, "=", num1+num2)
print(num1, "-",num2, "=", num1-num2)
print(num1, "*",num2, "=", num1*num2)
print(num1, "//",num2, "=", num1//num2)

A = [1,2,3,4]
len(A)