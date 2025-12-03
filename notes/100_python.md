# Python

## Características

- Tem tipagem dinâmica, quando você declara um valor ou variável não é necessário que seja declarado também o tipo do valor que sera inserido

## Comportamentos

#### 


## [Operadores](https://docs.python.org/3/reference/expressions.html#operator-precedence)

- [`lambda`](https://docs.python.org/3/reference/expressions.html#operator-precedence)

- [`and` `not` `or`](https://docs.python.org/3/reference/expressions.html#boolean-operations)

## Funções

- [`enumerate()`](https://docs.python.org/pt-br/3/library/functions.html#enumerate): Devolve um objeto enumerado, algo que possa ser iterado ex:

  ```python
    seasons = ['Spring', 'Summer', 'Fall', 'Winter'] 
    list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    list(enumerate(seasons, start=1))
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
  ```

- [`type(variavel)`](https://docs.python.org/pt-br/3/library/functions.html#type): Devolve o tipo daquele valor que é seu parametro
- [`sorted(iteravel)`]()
- [`len()`]()
- [`tuple()`]() - Parse de listas para tuplas.
- [`count()`]() - Parse de listas para tuplas.

## Instruções

- [`del()`]()

- `with`
  - https://www.geeksforgeeks.org/python/with-statement-in-python/
    - (Resumir)

## Tipos

### Strings

#### Definição e características

- São consideradas como listas, é possível iterar e etc
- Posso usar `f'Texto da String'` para usar código dentro da String sem precisar concatenar

#### Edição de Strings
- Rever o [exercicio](C:\Users\arthu\OneDrive\Documentos\Projetos\Python\P3-Mundo03\exercicio076.py)

## Tipos de variáveis (e listas)

  Entre os tipos de 'listas' no python temos:
    - Conjuntos
    - Tuplas
    - Listas
    - Dicionários

### Tuplas

#### Definição

- Tem indices
- Não podem ser alteradas (imutáveis)
- Se eu somar 2 tuplas terei na realidade 2 tuplas concatenadas
- Podem receber mais de 1 tipo de dados dentro das tuplas

#### Métodos

- `tupla.count(valor)`: é um objeto interno da tupla que vai conseguir procurar quantas vezes aparece o valor dado na tupla que está usando esse objeto/método
- `tupla.index(valor)`: é um objeto interno da tupla que vai conseguir retornar o indice referente ao valor dado ao objeto
