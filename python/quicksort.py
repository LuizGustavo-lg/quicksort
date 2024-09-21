from animationgrafic import AnimationGrafic
import random


def quick_sort(values, left, right, animation):
    
    if left < right:

        index_pivo = partition(values, left, right)
        animation.append(values, index_pivo)
        quick_sort(values, left, index_pivo-1, animation)
        quick_sort(values, index_pivo+1, right, animation)


def partition(values, left, right):
    pivo = values[left]
    j = left

    for i in range(left+1, right+1):
        if values[i] <= pivo:
            j += 1
            values[j], values[i] = values[i], values[j];

    values[left], values[j] = values[j], values[left];
    return j



print("***Gerando Lista Aleatoria**")

values = []
for i in range(100):
    values.append(random.randint(0, 100))


animation = AnimationGrafic()


print("**Ordenando**")
quick_sort(values, 0, len(values)-1, animation)

print("**Exibindo Grafico**")
animation.render(interval=300)
# animation.save()
animation.show()