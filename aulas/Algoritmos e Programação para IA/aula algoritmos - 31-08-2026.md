# Aula de aula algoritmos

## Principal

### IF

> *Toda frase de fã do Neymar começa com IF*

### Condicional:
  - Se (if) a condição for Positiva (True) entra no bloco de código
  - Se (if) for negativa, ele não passa pelo bloco de código e escapa/sai, o que acontece com o código depende do que se tem depois do bloco de código
  - Se (if) for um `else` ele realiza independemente o código dentro do bloco de texto do `else`
  - Se (if) for o `elif` ele receberá novos parametros e por sua vez se forem atendidas as suas condições entra no bloco de código
### Conjuntos ou Sets
  - É uma lista com elementos unicos
  - Ele é a base de conjuntos
  - `a.intersection(b)` `intersection()` e `&` são o metodo e o operador, respectivamente, de intersecção
  - `a.union(b)` `union()` e `|` são o metodo e o operador, respectivamente, de união
  - `list()` transformar um Set/Conjunto em uma Lista
  - `set()` transforma uma Lista em Sets/Conjunto 
### Switch/Case
  - o switch case usa a palavra chave `match *valor*:`
  - se usa o `case valor/condição esperada`
  - `_` é uma variavel que quando usada em um `case` ela sempre passa no erro/não passando nos cases anteriores
``` py
a = 0
b = 2

match a:
  case 0:
    print("É um número 0")
  case 1:
    print("É um número 1")
  case 2:
    print("É um número 2")
  case 0 if b == 2:
    print("É um número 0 e o b é um número 2")
  case _:
    print("Default")

```

### Loops
  - Serve para percorrer elementos de lista
  - Estruturas de repetição
  - 
  #### While
    - Estrutura de repetição aonde ele faz o código obedecer uma condição para entrar em um bloco de código e assim realizar as alterações

- `while` iteração por condição para uma lista
``` py
i = 0
while i < 0:
  i = i + 1
  print(i)
```
- Iteração pelo while em array/lista
``` py
i = 0
lista = [1,2,3,4,5,6]
while i < len(lista):
  print(lista[i])
  i += 1
  print(i)
```
- `for...in...` serve como desempacotador, ele entende de maneira simples que está realizando uma tarefa semelhante ao `while` em um array
``` py
i = 0
for i in lista:
  print(i)
```

- existe o `range()` que serve para criar um espaço
``` py

for i in lista:
  i = i + 1
  print(i)
``` 
## O que entendi:

- ...

## O que não entendi:

- ...

## TODOs (tarefas):

- [ ] ...

## Glossário:

- ...

## Notas e Rascunhos:

...
