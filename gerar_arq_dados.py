import random

QNT_VAL = 100

with open("dados.txt", "w") as dados:
    for i in range(QNT_VAL-1):
        dados.write(str(random.randint(0, 100)) + '\n')
    dados.write(str(random.randint(0, 100)))

print("***Arquivo de dados gerado***")
