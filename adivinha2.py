import random

quantidade = int(input("Digite a quantidade: "))
numeros = []
for i in range(quantidade):
    numero = random.randint(1, 6)
    numeros.append(numero)

for n in numeros:
    print(n)

print("O número máximo foi:", max(numeros))
print("A soma foi:", sum(numeros))
