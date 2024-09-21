import random

with open("dados.txt", "w") as dados:
    for i in range(1000):
        dados.write(str(random.randint(0, 100)) + '\n')
