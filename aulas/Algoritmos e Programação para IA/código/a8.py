print("Exercicio 1")
a1 = lambda num: num*2

print(a1(5))

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
a2 = lambda lista:map(lambda x: x ** 2,lista)

pizza = a2(numeros)
for i in pizza:
  print(i)
  
  
print("Exercicio 2")
numeros2 = [10, 20, 30, 40, 50]
a3 = lambda lista:map(lambda x: x + 5, lista)

pizza2 = a3(numeros2)
for i in pizza2:
  print(i)
  
  
print("Exercicio 3")
numeros3 = [10, 20, 30, 40, 50]
a3 = lambda lista:map(lambda x: x + 5, lista)

pizza2 = a3(numeros3)
for i in pizza2:
  print(i)
  
  
print("Exercicio 4")
numeros4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a4 = lambda lista:filter(lambda x: not x % 2, lista)

pizza3 = a4(numeros4)
for i in pizza3:
  print(i)


print("Exercicio 5")
numeros5 = [3, 12, 7, 20, 15, 2, 30, 9]
a5 = lambda lista:filter(lambda x: x > 10, lista)

pizza5 = a5(numeros5)
for i in pizza5:
  print(i)


print("Exercicio 6")
numeros6 = ["Ana", "Carlos", "João", "Beatriz", "Luiz", "Maria"]
a6 = lambda lista:filter(lambda x: len(x) >= 4, lista)

pizza6 = a6(numeros6)
for i in pizza6:
  print(i)


print("Exercicio 7")
numeros7 = ["ana", "carlos", "joao", "beatriz"]
a7 = lambda lista:map(lambda x: x.upper(), lista)

pizza7 = a7(numeros7)
for i in pizza7:
  print(i)


print("Exercicio 8")
numeros8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = lambda lista:filter(lambda x: not x % 2, lista)
a8 = lambda lista:map(lambda x: x ** 2, pares(lista))

pizza8 = a8(numeros8)
for i in pizza8:
  print(i)


print("Exercicio 9")
numeros9 = [5, 12, 8, 20, 3, 15, 25, 7]

cond1 = lambda lista:filter(lambda x: x > 10, lista)
a9 = lambda lista:map(lambda x: x * 3, cond1(lista))

pizza9 = a9(numeros9)
for i in pizza9:
  print(i)


print("Exercicio 10")
numeros10 = [10, 15, 20, 25, 30, 35, 40]

cond2 = lambda lista:filter(lambda x: x >= 25, lista)
a10 = lambda lista:map(lambda x: x * 9/5 + 32, cond2(lista))

pizza10 = a10(numeros10)
for i in pizza10:
  print(i)
  


print("Exercicio 11")
numeros11 =  [50, 120, 80, 200, 35, 150, 90]

cond3 = lambda lista:filter(lambda x: x > 100, lista)
a11 = lambda lista:map(lambda x: x - x * 0.1, cond3(lista))

pizza11 = a11(numeros11)
for i in pizza11:
  print(i)
  
  


print("Exercicio 12")
alunos = [
{"nome": "Ana", "nota": 8},
{"nome": "Carlos", "nota": 5},
{"nome": "João", "nota": 9},
{"nome": "Maria", "nota": 6},
{"nome": "Pedro", "nota": 4}
]


a12 = lambda lista:filter(lambda x: x["nota"] >= 6, lista)

pizza12 = a12(alunos)
for i in pizza12:
  print(i)
  
  


print("Exercicio 13")
numeros13 = [10, 15, 20, 25, 30, 35, 40, 45, 50]

cond4 = lambda lista:filter(lambda x: not x % 2 and x > 20, lista)
a13 = lambda lista:map(lambda x: x * 2, cond4(lista))

pizza13 = a13(numeros13)
for i in pizza13:
  print(i)
  
