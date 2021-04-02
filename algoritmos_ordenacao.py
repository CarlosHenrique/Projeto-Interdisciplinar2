
def selection_sort(lista):
    for index in range(0, len(lista)):
        min_index = index

        for direita in range(index + 1, len(lista)):  # percorre a direita, começa do proximo elemento
            if lista[direita] < lista[min_index]:                       # se o elemento da direita for menor q o meu atual
                min_index = direita                                         # o menor recebe o indíce do elemento da direita

        lista[index], lista[min_index] = lista[min_index], lista[index]         # e faz a troca


def bubble_sort(lista):
    for final in range(len(lista), 0, -1):  # da ultima posição até a posição zero
        trocando = False
        for atual in range(0, final - 1):
            if lista[atual] > lista[atual + 1]:
                lista[atual + 1], lista[atual] = lista[atual], lista[atual + 1]
                trocando = True
        if not trocando:
            break




def insertion_sort(lista):
    for posicao in range(0, len(lista)):# da posicao zero até o final
        elemento_atual = lista[posicao]

        while posicao > 0 and lista[posicao - 1] > elemento_atual:
            lista[posicao] = lista[posicao - 1]
            posicao -= 1

        lista[posicao] = elemento_atual



