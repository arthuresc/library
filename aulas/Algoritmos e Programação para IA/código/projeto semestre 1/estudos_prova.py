def quicksort(lista, counter = 1):
  counter = counter + 1
  if len(lista) <= 1:
    return lista
  pivo = lista[len(lista) // 2]
  menores = [x for x in lista if x < pivo]
  iguais = [x for x in lista if x == pivo]
  maiores = [x for x in lista if x > pivo]
  
  pMeno = quicksort(menores)
  pMaio = quicksort(maiores)
  ingual = iguais
  print(f"\n{" " * counter * 2}Os menores: {pMeno}\n{" " * counter * 2}Os maiores: {pMaio}\n{" " * counter * 2}E os iguais: {ingual}\n{" " * counter * 2}E a lista de entrada: {lista}\n -------{counter}-------")
  return quicksort(menores, counter) + iguais + quicksort(maiores, counter)


# listin = ["arroz", "feijão", "batata"]
listin = ["1", "4","2", "8", "10", "6", "3"]
# print(listin)
quicksort(listin)
listin2 = quicksort(listin)

print("-" * 12, listin2)
