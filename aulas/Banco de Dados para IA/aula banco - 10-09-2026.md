# Aula de aula banco

## Principal

- Entidades
  - 
- 
## O que entendi:

- PK - Primary key (Chave primaria)
- Tabela assossiativa: é a impressão entre Carta e Ilustrador
- Chave candidata: são todas as outras
  - ~~Super chave, minima ou conjunto minimo~~
  - 
- Superchave: é um conjunto de informações formado por chaves candidatas, ou seja, é o conjunto de todas outras chaves da entidade 

- (menos especifico) Superchave *(conjunto)* -> Chave candidata *(cada chave)* -> Chave primaria (mais especifico)

- Chave alternante: 1 unica que poderia ter sido escolhida ao inves da Primária

- Foreign Key (Chave estrangeira): é a chave que faz referencia a outro registro 

- **NAS RELAÇÕES**
  - Muitos para Muitos serão sempre 3 tabelas (no minimo)
    - Uma tabela de relação, o nome da tabela é: Tabela Relacional
  - 1 para Muitos serão 2 tabelas só

## O que não entendi:

- OracleID: qual a diferença de um ID comum?
  - Ele tambem usa UUID
  - Ele é especifico do Magic, se trata de uma estratégia de como definir que um ID para uma carta (ex: Nome de carta), mas a sua diferença para o ID é que o ID é unico e mesmo se tratando da mesma carta mas outra *"impressão"*

## TODOs (tarefas):

- [ ] ...

## Glossário:

- ...

## Notas e Rascunhos:

- https://www.freecodecamp.org/portuguese/learn/introduction-to-sql-and-postgresql/lecture-working-with-relational-databases/what-are-the-different-types-of-relationships-in-a-relational-database
- https://medium.com/@francethais/modelagem-de-banco-de-dados-entidades-relacionamentos-e-atributos-cada1a6e63d0
