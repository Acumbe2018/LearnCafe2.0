#Função if e else#
#if = Se
#else = Se não , caso contrário
#elif = Então Se.
idade = int(input("Digite sua idade: "))
resp = idade >= 18

if idade >= 18:
    print("Você pode beber")
    if idade >= 21:
        print("Você é VIP")

else:
    print("Você não pode beber")

print(resp)