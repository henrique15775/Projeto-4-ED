import random 
import time
import os
from metodos import *

lista = []

for i in range(20000):
  lista.append(random.randint(1, 5000))


while True:
  os.system("clear")
  print('#1-BubbleSort\n#2-InsertionSort\n#3-ShellSort\n#4-MergeSort\n#5-QuickSort\n#6-Quit\n\n')
  interacao = int(input("Digite a opção"))

  if (interacao == 1):
    lista_alt = lista.copy()
    print(f"\n{lista}\n\n")
    inicio = time.time()
    BubbleSort(lista_alt)
    fim = time.time()
    total = (fim - inicio)
    print(f"Tempo levado com o BubbleSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      pass
    else:
      quit()
  
  elif (interacao == 2):
    lista_alt = lista.copy()
    print(f"\n{lista}\n")
    inicio = time.time()
    InsertionSort(lista_alt)
    fim = time.time()
    total = (fim - inicio)
    print(f" Tempo levado com o InsertionSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      pass
    else:
      quit()
  
  elif (interacao == 3):
    lista_alt = lista.copy()
    print(f"\n{lista}\n")
    inicio = time.time()
    ShellSort(lista_alt)
    fim = time.time()
    total = (fim - inicio)
    print(f"Tempo levado com o ShellSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      pass
    else:
      quit()
  
  elif (interacao == 4):
    lista_alt = lista.copy()
    print(f"\n{lista}\n")
    inicio = time.time()
    MergeSort(lista_alt)
    fim = time.time()
    print()
    print(f"{lista_alt}")
    print()
    total = (fim - inicio)
    print(f"Tempo levado com o MergeSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      pass
    else:
      quit()
  
  elif (interacao == 5):
    lista_alt = lista.copy()
    print(f"\n{lista}\n")
    inicio = time.time()
    QuickSort(lista_alt, 0, len(lista_alt) - 1)
    fim = time.time()
    print()
    print(f"{lista_alt}")
    print()
    total = (fim - inicio)
    print(f"Tempo levado com o QuickSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      pass
    else:
      quit()
  
  else:
    break