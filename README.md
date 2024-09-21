# QuickSort Algorithm

Este repositório contém uma implementação do algoritmo de ordenação **QuickSort**.

## Descrição

QuickSort é um algoritmo de ordenação eficiente, baseado na técnica de divisão e conquista. Ele seleciona um elemento como pivô e particiona o array em duas partes: os elementos menores que o pivô à esquerda e os elementos maiores que o pivô à direita. Em seguida, ele ordena recursivamente as duas subpartes.

A complexidade esperada no tempo de execução é **O(n log n)**, mas no pior caso, o tempo pode ser **O(n²)**, o que ocorre quando o pivô escolhido é o menor ou o maior valor em todas as divisões.

## Características

- Complexidade média: **O(n log n)**
- Complexidade no pior caso: **O(n²)**
- Algoritmo recursivo
- Algoritmo "in-place" (usa memória auxiliar mínima)
- Não estável (a ordem relativa dos elementos iguais pode mudar)

## Implementação

A implementação aqui disponível está escrita em Python & C++.

### Estrutura do projeto

- `c++/quicksort.cpp`: Implementação do algoritmo QuickSort em c++.
- `python/quicksort.py`: Implementação do algoritmo QuickSort em python (Gera uma visualização em forma de grafico).
- `gerar_arq_dados.py`: Gera o arquivo de dados randomizado.
- `test_quicksort.py`: Testes unitários para garantir o funcionamento correto do algoritmo.

