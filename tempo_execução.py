import random
import time
from algoritmos_ordenacao import(
    bubble_sort,
    selection_sort,
    insertion_sort)

def lista_semi_ordenada(tamanho):
    lista = [i for i in range(0, tamanho+1)]
    for i in range(10, tamanho, 10):
        lista[i], lista[i-1] = lista[i-1], lista[i]
    return lista

algoritmos = {
        "bubble_sort": bubble_sort,
        "selection_sort": selection_sort,
        "insertion_sort": insertion_sort
            }

numero_itens = 2000
lista_normal = [random.randint(0, numero_itens)
                for i in range(numero_itens)]

random.shuffle(lista_normal)
semi_ordenada = lista_semi_ordenada(numero_itens)
reversa = sorted(lista_normal, reverse=True)


print("Lista randômica")
print("=-" * 50)
for nome, algoritmo in algoritmos.items():
    lista = list(lista_normal)
    inicio = time.time()
    algoritmo(lista)
    fim = time.time()
    tempo = fim - inicio

    if lista == sorted(lista):
        print(f"O {nome} levou {tempo:.4f}s")
    else:
        pass

print("\n\nLista semi-ordenada")
print("-=" * 50)
for nome, algoritmo in algoritmos.items():
    lista = list(semi_ordenada)
    inicio = time.time()
    algoritmo(lista)
    fim = time.time()
    tempo = fim - inicio

    if lista == sorted(lista):
        print(f"O {nome} levou {tempo:.4f}s")
    else:
        pass

print("\n\nLista ordenada reversamente")
print("-=" * 50)
for nome, algoritmo in algoritmos.items():
    lista = list(reversa)
    inicio = time.time()
    algoritmo(lista)
    fim = time.time()
    tempo = fim - inicio
    if lista == sorted(lista):
        print(f"O {nome} levou {tempo:.4f}s")
    else:
        pass