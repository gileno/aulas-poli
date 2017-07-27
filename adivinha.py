import random

numero = random.randint(1, 20)

for i in range(5):
    chute = input("Digite um número: ")
    chute = int(chute)

    diferenca = numero - chute

    if diferenca == 0:
        print("Você acertou!!!")
        break
    elif diferenca > 0:
        print("Você errou, o número é maior!!!")
    else:
        print("Você errou, o número é menor!!!")

print("Fim do programa, o número era:", numero)