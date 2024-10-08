#include <iostream>
#include <fstream>
#include <ctime>
using namespace std;
int count_inter = 0;

void swap(int values[], int i, int j){
    /*
    Troca dois valores de posiçao em um array
    param: int values[] - vetor de elementos
    param: int i - primeiro elemento
    param: int j - segundo elemento
    */
    int aux = values[j];
    values[j] = values[i];
    values[i] = aux;
}

int pickPivoIndexByMedian(int values[], int left, int right){
    /*
    Seleciona a mediana de 3 valores de uma lista
    param: int values[] - vetor de elementos
    param: int left - indice do elemento mais a direita
    param: int right - indice do elemento mais a esquerda
    return: indice
    */
    int mid = (left+right)/2;
    if((values[left] > values[mid]) != (values[left] > values[right])){
        return left;
    }
    else if((values[mid] > values[left]) != (values[mid] > values[right])){
        return mid;
    }
    else {
        return right;
    }
}

int pickPivoIndexByRandom(int values[], int left, int right){
    /*
    Seleciona um indice randomico da lista
    param: int values[] - vetor de elementos
    param: int left - indice do elemento mais a direita
    param: int right - indice do elemento mais a esquerda
    return: indice
    */
    return (rand()%(right-left))+left;
}

int pickPivoIndexByLeft(int values[], int left, int right){
    /*
    Seleciona o primeiro indice
    param: int values[] - vetor de elementos
    param: int left - indice do elemento mais a direita
    param: int right - indice do elemento mais a esquerda
    return: indice
    */
    return left;
}


int partition(int values[], int left, int right){
    /*
    Seleciona um pivo
    Ordena os elementos menores que o pivo a esquerda e os maiores a direita
    param: int values[] - vetor de elementos
    param: int left - indice do elemento mais a direita
    param: int right - indice do elemento mais a esquerda
    return: indice pivo
    */

    // int index_pivo = pickPivoIndexByLeft(values, left, right);
    // int index_pivo = pickPivoIndexByRandom(values, left, right);
    int index_pivo = pickPivoIndexByMedian(values, left, right);
    
    int pivo = values[index_pivo];
    swap(values, left, index_pivo);
    index_pivo = left;

    for (int i = left+1; i<=right; i++){
        if (values[i] <= pivo){
            ++index_pivo;
            swap(values, i, index_pivo);       
        }
    }
    swap(values, left, index_pivo);
    return index_pivo;
}

void quick_sort(int values[], int left, int right){
    /*
    Ordena um vetor com elementos inteiros
    param: int values[] - vetor de elementos para ordenação
    param: int left - indice do elemento mais a direita
    param: int right - indice do elemento mais a esquerda
    */
    ++count_inter;
    if (left < right){
        int index_pivo = partition(values, left, right);
        quick_sort(values, left, index_pivo-1);
        quick_sort(values, index_pivo+1, right);
    }
}
 

int main(){
    int values[500];
    srand(time(0));
    
    ifstream dados;

    dados.open("./dados.txt");
    for (int i = 0; !dados.eof(); i++){
        dados >> values[i];
    }
    dados.close();

    int tm_v = sizeof(values)/sizeof(values[0])-1;
    
    quick_sort(values, 0, tm_v);

    for(int i = 0; i<=tm_v; i++){
        cout << values[i] << ", ";
    }
    cout << '\n';
    cout << "Interações: " << count_inter << '\n';
}
