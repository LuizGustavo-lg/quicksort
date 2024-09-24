from animationgrafic import AnimationGrafic


def quick_sort(values, left, right, animation, order = 0):
    '''
    -> Ordena um vetor com elementos inteiros
    :param values: vetor de elementos para ordenação
    :param left: indice do elemento mais a direita
    :param right: indice do elemento mais a esquerda
    :param animation: objeto de animação
    :param order: ordem de ordenação do array (crescente/decrescente) - default=True crescente
    '''
    
    if left < right:

        index_pivo = partition(values, left, right, order)
        animation.append(values, index_pivo)
        quick_sort(values, left, index_pivo-1, animation)
        quick_sort(values, index_pivo+1, right, animation)


def partition(values, left, right, order):
    '''
    -> Seleciona um pivo
    -> Ordena os elementos menores que o pivo a esquerda e os maiores a direita
    :param values: vetor de elementos
    :param left: indice do elemento mais a direita
    :param right: indice do elemento mais a esquerda
    :param order: ordem de ordenação do array, menores a direita ou a esquerda
    :return: indice pivo
    '''
    pivo = values[left]
    j = left

    for i in range(left+1, right+1):
        if (values[i] <= pivo) == order:
            j += 1
            values[j], values[i] = values[i], values[j];

    values[left], values[j] = values[j], values[left];
    return j


values = []

with open("dados.txt", "r") as dados:
    for linha in dados:
        values.append(int(linha.strip()))


animation = AnimationGrafic()


quick_sort(values, 0, len(values)-1, animation)

print(values)
# animation.render(interval=300)
# animation.show()
# animation.save()