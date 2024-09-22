import random

QNT_VAL = 500
SORT = False

with open("dados.txt", "w") as dados:
    if SORT:
        for i in range(QNT_VAL-1):
            dados.write(str(i) + '\n')
        dados.write(str(700))
    else:
        for i in range(QNT_VAL-1):
            dados.write(str(random.randint(0, 100)) + '\n')
        dados.write(str(random.randint(0, 100)))

print("***Arquivo de dados gerado***")
