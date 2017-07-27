import random

quantidade = int(input("Digite a quantidade: "))
maximo = 0
soma = 0
for i in range(quantidade):
    numero = random.randint(1, 6)
    print(numero)
    if maximo < numero:
        maximo = numero
    soma += numero

print("O número máximo foi:", maximo)
print("A soma foi:", soma)
