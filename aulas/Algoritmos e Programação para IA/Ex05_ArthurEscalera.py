# 1) Crie um função chamada conta_ate_dez 
# Essa função não tem parâmetros e deve imprimir no terminal 
# os números de 1 até 10 usando um loop. 

def conta_ate_dez():
  counter = 1
  while counter <= 10:
    print(counter)
    counter += 1
  else:
    print("Fim exercicio 1")

conta_ate_dez()
    
# 2) Crie um função chamada lista_ate_dez 
# Essa função não tem parâmetros e deve retornar uma lista com 
# os números de 1 até 10 usando um loop. 
def lista_ate_dez():
  counter = 1
  lista = []
  while counter <= 10:
    lista.append(counter)
    counter += 1
  else:
    print(f"Fim exercicio 2: {lista}")

lista_ate_dez()
    
  
# 3) Crie um função chamada conjunto_ate_dez 
# Essa função não tem parâmetros e deve retornar uma set 
# (conjunto) com os números de 1 até 10 usando um loop.
def conjunto_ate_dez():
  counter = 1
  lista = set()
  while counter <= 10:
    lista.add(counter)
    counter += 1
  else:
    print(f"Fim exercicio 3: {lista}")
    
conjunto_ate_dez()
 
# 4) Crie um função chamada tupla_ate_dez 
# Essa função não tem parâmetros e deve retornar uma tupla 
# com os números de 1 até 10 usando um loop.
def tupla_ate_dez():
  counter = 1
  lista = []
  while counter <= 10:
    lista.append(counter)
    counter += 1
  else:
    tupla = tuple(lista)
    print(f"Fim exercicio 4: {tupla}")
    
tupla_ate_dez()
 
# 5) Crie um função chamada inv_ate_dez 
# Essa função não tem parâmetros e deve imprimir no terminal  
# programa que imprima os números de 10 até 1.


# 6) Crie um função chamada conta_ate_cem 
# Essa função não tem parâmetros e deve imprimir no terminal 
# os números pares de 1 até 100 usando um loop. Use a função 
# (ver capítulos/exercícios anteriores). 
# 1 
# 7) Crie 2 funções soma_serie1 e soma_serie2: 
# Essas funções tem dois parâmetros a e b, é necessário 
# que a < b. Se for o caso as funções devem retornar “-1” 
# O objetivo dessas funções é imprimir no terminal a soma 
# de todos os números entre a e b. 
# Exemplos: 
# Se (a,b) = (1,5) => 1 + 2 + 3 + 4 +5 =15 
# Se (a,b) = (1,100) => 5.050 
# a) soma_serie1: Crie uma função usando um loop para 
# somar os valores; 
# b) soma_serie2: Use o método da soma de Gauss para 
# chegar a resposta. 
# Lembrete: A soma de Gauss chegamos a soma de 
# uma série somando o primeiro e o último elemento, 
# multiplicando o resultado pelo número de elementos 
# e depois dividindo o resultado por 2, conforme 
# equação abaixo:  
# c) Faça uma comparação entre os resultados dos dois 
# métodos (eles devem ser iguais), escreva um 
# comentário se é possível perceber diferença entre 
# performance nas duas soluções para o mesmo 
# problema. 
# 8) Crie uma função chamada fatorial(n) que calcule o fatorial 
# de um número usando loop. 
# 2 
# Atenção: Fatorial é um número natural inteiro positivo, o qual 
# é representado por n! 
# O fatorial de um número é calculado pela multiplicação desse 
# número por todos os seus antecessores até chegar ao número 1 
# 0! = 1  
# 1! = 1 
# 2! = 2 . 1 = 2 
# 5! = 5 . 4 . 3 . 2 . 1 = 120 
 
# 9) Crie uma função chamada fib(n) que calcule o número N 
# da sequência de Fibonacci, use um loop. 
# Atenção:  Sequência de Fibonacci é uma sequência de 
# números inteiros, começando normalmente por 0 e 1, na qual 
# cada termo subsequente corresponde à soma dos dois 
# anteriores. https://oeis.org/A000045  

def fib(n):
  counter = n
  fValue1 = 1
  
  
 
# 10) Crie uma função chamada list_fib_n(n) está função deve 
# retornar uma lista de tamanho N com os N primeiros números 
# de Fibonacci. Use um loop e a função fib (ver mais cedo nesse 
# 1) Crie um função chamada conta_ate_dez
# Essa função não tem parâmetros e deve imprimir no terminal
# os números de 1 até 10 usando um loop.

def conta_ate_dez():
  contador = 0
  while contador < 10:
    print(contador + 1)
    contador += 1
  else:
    print("Final exercicio 1")
    
conta_ate_dez()

# 2) Crie um função chamada lista_ate_dez
# Essa função não tem parâmetros e deve retornar uma lista com
# os números de 1 até 10 usando um loop.

def lista_ate_dez():
    contador = 0
    lista = []
    while contador < 10:
      lista.append(contador + 1)
      contador += 1
    else:
      print(f"Final exercicio 2: {lista}")
    
lista_ate_dez()

# 3) Crie um função chamada conjunto_ate_dez
# Essa função não tem parâmetros e deve retornar uma set
# (conjunto) com os números de 1 até 10 usando um loop.


def conjunto_ate_dez():
    contador = 0
    lista = set()
    while contador < 10:
      lista.add(contador + 1)
      contador += 1
    else:
      print(f"Final exercicio 3: {lista}")
    
conjunto_ate_dez()

# 4) Crie um função chamada tupla_ate_dez
# Essa função não tem parâmetros e deve retornar uma tupla
# com os números de 1 até 10 usando um loop.


def tupla_ate_dez():
  contador = 0
  lista = []
  while contador < 10:
    lista.append(contador + 1)
    contador += 1
  else:
    tupla = tuple(lista)
    print(f"Final exercicio 4: {tupla}  do tipo {type(tupla)}")
    
tupla_ate_dez()

# 5) Crie um função chamada inv_ate_dez
# Essa função não tem parâmetros e deve imprimir no terminal
# programa que imprima os números de 10 até 1.

def inv_ate_dez():
  contador = 10
  lista = []
  while contador > 0:
    lista.append(contador)
    contador = contador - 1
  else:
    print(f"Final exercicio 5: {lista}")
    
inv_ate_dez()

# 6) Crie um função chamada conta_ate_cem
# Essa função não tem parâmetros e deve imprimir no terminal
# os números pares de 1 até 100 usando um loop. Use a função
# (ver capítulos/exercícios anteriores).

def conta_ate_cem():
  lista = []
  for i in range(0, 101, 2):
    lista.append(i)
    # print(f"{i}")
  else:
    print(f"Final exercicio 6: {lista}")
        
conta_ate_cem()

# 7) Crie 2 funções soma_serie1 e soma_serie2:
# Essas funções tem dois parâmetros a e b, é necessário
# que a < b. Se for o caso as funções devem retornar “-1”
# O objetivo dessas funções é imprimir no terminal a soma
# de todos os números entre a e b.
# Exemplos:
# Se (a,b) = (1,5) => 1 + 2 + 3 + 4 +5 =15
# Se (a,b) = (1,100) => 5.050
# a) soma_serie1: Crie uma função usando um loop para
# somar os valores;
# b) soma_serie2: Use o método da soma de Gauss para
# chegar a resposta.
# Lembrete: A soma de Gauss chegamos a soma de
# uma série somando o primeiro e o último elemento,
# multiplicando o resultado pelo número de elementos
# e depois dividindo o resultado por 2, conforme
# equação abaixo:
# c) Faça uma comparação entre os resultados dos dois
# métodos (eles devem ser iguais), escreva um
# comentário se é possível perceber diferença entre
# performance nas duas soluções para o mesmo
# problema.

def soma_serie1(a,b):
  texto = f"(a,b) = ({a},{b}) => "
  textoUnidade = 0
  result = 0
  for i in range(a,(b+1)):
    result = result + i
    textoUnidade = textoUnidade + a
    texto += f"{textoUnidade} "
  else:
    print(f"Final exercicio 7-a: {texto}= {result}")

soma_serie1(1,25)

def soma_serie2(a,b):
  result = 0



# 8) Crie uma função chamada fatorial(n) que calcule o fatorial
# de um número usando loop.
# Atenção: Fatorial é um número natural inteiro positivo, o qual
# é representado por n!
# O fatorial de um número é calculado pela multiplicação desse
# número por todos os seus antecessores até chegar ao número 1
# 0! = 1
# 1! = 1
# 2! = 2 . 1 = 2
# 5! = 5 . 4 . 3 . 2 . 1 = 120

# 9) Crie uma função chamada fib(n) que calcule o número N
# da sequência de Fibonacci, use um loop.
# Atenção: Sequência de Fibonacci é uma sequência de
# números inteiros, começando normalmente por 0 e 1, na qual
# cada termo subsequente corresponde à soma dos dois
# anteriores. https://oeis.org/A000045

# 10) Crie uma função chamada list_fib_n(n) está função deve
# retornar uma lista de tamanho N com os N primeiros números
# de Fibonacci. Use um loop e a função fib (ver mais cedo nesse
# mesmo episódio).