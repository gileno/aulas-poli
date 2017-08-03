import os

def get_contato():
    nome = input("Nome: ")
    email = input("E-mail: ")
    return nome, email

quantidade = int(input("Digite uma quantidade: "))

#arquivo = open('contatos.csv', 'w')
arquivo = open('contatos.csv', 'a')

for i in range(quantidade):
    nome, email = get_contato()
    arquivo.write(nome)
    arquivo.write(',')
    arquivo.write(email)
    arquivo.write(os.linesep)
    #arquivo.write("\n")
print("Fim do programa")