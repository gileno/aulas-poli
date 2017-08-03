import os

arquivo = open('contatos.csv', 'r')

conteudo = arquivo.read()

linhas = conteudo.split(os.linesep)
#linhas = conteudo.split('\n')
print('Quantidade de linhas:', len(linhas))

emails = []

for linha in linhas:
    email = linha.split(",")[1]
    emails.append(email)

emails_unicos = set(emails)

for email in emails_unicos:
    count = emails.count(email)
    if count > 1:
        print('E-mail:', email, '[', count, ']')
