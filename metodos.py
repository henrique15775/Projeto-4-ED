def BubbleSort (lista):
  
  tam = len(lista)

  for i in range(tam - 1):
    for j in range(0, tam - i - 1):
      if lista[j] > lista[j + 1] :
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
  
  """
  exchanges = True
  passnum = len(lista)-1
  while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if lista[i]>lista[i+1]:
               exchanges = True
               temp = lista[i]
               lista[i] = lista[i+1]
               lista[i+1] = temp
       passnum = passnum-1
  """
  print(lista)
  print()

def InsertionSort (lista):

  tam = len(lista)

  for i in range (1, tam):
    key = lista[i]
    j = i - 1
    while j >= 0 and key < lista[j] :
      lista[j + 1] = lista[j]
      j -= 1
    
    lista[j + 1] = key

  print(lista)
  print()

def ShellSort (lista):

  tam = len(lista)
  gap = tam // 2

  while gap > 0:
    for i in range(gap, tam):
      temp = lista[i]
      j = i

      while  j >= gap and lista[j - gap] > temp:
        lista[j] = lista[j - gap]
        j -= gap

      lista[j] = temp

    gap //= 2
  
  print(lista)
  print()

def MergeSort (lista):
  if len(lista) > 1:
    mid = len(lista) // 2

    L = lista[:mid]

    R = lista[mid:]

    MergeSort(L)

    MergeSort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        lista[k] = L[i]
        i += 1
      else:
        lista[k] = R[j]
        j += 1
      k += 1

    while i < len(L):
      lista[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      lista[k] = R[j]
      j += 1
      k += 1


def partition(lista, low, high):
  i = (low - 1)         
  pivot = lista[high]     

  for j in range(low, high):
    if lista[j] <= pivot:
      i = i + 1
      lista[i], lista[j] = lista[j], lista[i]

  lista[i + 1], lista[high] = lista[high], lista[i + 1]
  return (i + 1)

def QuickSort (lista, low, high):
  if (len(lista) == 1):
    return lista
  if (low < high):
    pi = partition(lista, low, high)
    QuickSort(lista, low, pi - 1)
    QuickSort(lista, pi + 1, high)