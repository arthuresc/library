# Exercício 03
# Crie o programa Python. Siga as instruções à risca.
# Entrega deve ser um arquivo “.py”
# 1-Faça (em Python 3) a função chamada escreve_ola. Sem parâmetros e sem retorno. Deverá escrever “ola exercício 03” e terminar: (atenção se estou pedindo apenas a função deverá entregar a função, no caso de ser um exercício no computador faça a chamada do código para verificar se existe algum erro,# mas entregue só o que foi pedido).

def escreve_ola():
  print("ola exercício 03");


# 2- Crie funções que resolvam as Expressões lógicas Crie para cada letra uma função que receba os valores booleanos (True ou False) e retorne o valor do resultado das expressões (deverá ser um booleano também).
# a) A and B
def logExp1(a, b):
  return a and b;
# b) A or B
def logExp2(a, b):
  return a or b;
# c) not A
def logExp3(a, b):
  return not a, b;
# d) B and C
def logExp4(a, b, c):
  return a ,b and c;
# e) A or B and C
def logExp5(a, b, c):
  return a or b and c;

# 3- Calculadora de operações
# Crie as funções:
# soma(a, b)
# subtracao(a, b)
# multiplicacao(a, b)
# divisao(a, b)
# O programa deve solicitar dois números e utilizar as funções
# para apresentar os quatro resultados. Crie pelo menos duas
# chamadas de teste de cada função que está criando.
def soma(a, b):
  print("soma ", a + b)
def subtracao(a, b):
  print("subtracao ", a - b)
def multiplicacao(a, b):
  print("multiplicacao ", a * b)
def divisao(a, b):
  print("divisao ", a / b)

soma(3, 4)
soma(7, 9)
subtracao(3, 4)
subtracao(7, 9)
multiplicacao(3, 4)
multiplicacao(7, 9)
divisao(3, 4)
divisao(7, 9)

# 4- Validação de dados
# Crie uma função:
# validar_usuario(nome, idade)
# A função deve retornar uma expressão booleana indicando se:
# ● o nome possui pelo menos 3 caracteres; e
# ● a idade está entre 18 e 100 anos.
# Essa função deverá usar somente expressões lógicas
# (operadores lógicos para devolver a resposta).
# Crie pelo menos duas chamadas de teste para a função que
# está criando.
def validar_usuario(nome, idade):
  return len(nome) >= 3 and idade >= 18 and idade <= 100
  # print(result);
  # return result;

validar_usuario("Arthur", 13);
validar_usuario("Iã", 18);


# 5 — Estatísticas de uma lista
# Crie uma lista contendo 10 números inteiros.
# Utilize funções e operações sobre listas para apresentar:
# A) Apresente a quantidade de elementos da lista.

lista = [100,2,3,4,5,6,7,8,9,10];
# elLista = lista[1]
# lista[1]
print(len(lista))
nicolasCarvalho = "Nicolas Carvalho"
# B)Apresente o maior valor.
print(lista[9])
# C)Apresente o menor valor.
print(lista[0])
# D) Apresente a soma dos valores.
print(lista[0]+lista[1]+lista[2]+lista[3]+lista[4]+lista[5]+lista[6]+lista[7]+lista[8]+lista[9])
# E) Apresente a média dos valores.
print((lista[0]+lista[1]+lista[2]+lista[3]+lista[4]+lista[5]+lista[6]+lista[7]+lista[8]+lista[9])/len(lista))
# F)Apresente o primeiro elemento utilizando o operador de
# acesso por índice.
print(lista[0])
# G) Apresente o último elemento utilizando o operador de acesso por índice.
print(lista[9])
# H) Utilize slicing (:) para apresentar:
# ● os três primeiros elementos;
# ● os três últimos elementos;
# ● os elementos que estão nas posições pares.
print(lista[0:3]);
print(lista[7:10]);
# AQUI VOU A TERCEIRA RESPOSTA

# I) Atualize o valor de pelo menos dois elementos da lista
# utilizando o operador de acesso por índice.

lista[2] = 3;
lista[6] = 31;

print(lista)
# J) Utilize append() para adicionar dois novos números à
# lista.

lista.append(11)
lista.append(12)
print(lista)
# K)Utilize pop() para remover um elemento da lista.
lista.pop(2)
print(lista)

# L)Ao final, apresente a lista resultante após todas as
# operações.
# Para fazer esses exercícios use somente as funções básicas já
# incluídas nas listas.

print(lista)


# 6 — Cadastro de produto
# Crie uma tupla representando um produto:
# produto = ("Notebook", 3500.00, 10, "Informática")
# Mostre:
# ● nome;
# ● preço;
# ● quantidade;
# ● categoria.
# Depois crie uma função que receba a tupla e calcule o valor
# total do estoque (preço × quantidade)
tupla = ("notebook", 3500.00, 10, "informática")
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])
def totalEstoque(param):
  valor = param[1]
  qtd = param[2]
  print(valor * qtd)
  
totalEstoque(tupla)
  


# 7 — Coordenadas
# Crie uma tupla:
# ponto = (10, 20, 30)
# Desempacote os valores em três variáveis:
# x, y, z = ponto
# Crie uma função que receba x, y e z e retorne a soma das
# coordenadas.

ponto = (10, 20, 30)

x, y, z = ponto

def funcaoQueRecebaXYZ(xis, ypsilon, ze):
  return xis + ypsilon + ze;

print(funcaoQueRecebaXYZ(x,y,z));

# 8 — Cadastro de aluno
# Crie um dicionário:
# aluno = {
#  "nome": "João",
#  "idade": 20,
#  "curso": "ADS",
#  "nota1": 8.0,
#  "nota2": 7.5
# }

pedrin = {
 "nome": "Pedrin",
 "idade": 20,
 "curso": "ADS",
 "nota1": 8.0,
 "nota2": 7.5
}


# A) O programa deve apresentar:

# ● nome;
print(pedrin["nome"])
# ● idade;
print(pedrin["idade"])
# ● curso;
print(pedrin["curso"])
# ● notas;
print("Nota 1: ", pedrin["nota1"])
print("Nota 2: ", pedrin["nota2"])
# ● média.
print(pedrin["nota1"] + pedrin["nota2"]/2)# B)Crie uma função:
# calcular_media(aluno)
# que obtenha as notas diretamente do dicionário e retorne a
# média (nota1 + nota2) / 2
def calcular_media(estudante):
  media = pedrin["nota1"] + pedrin["nota2"] / 2;
  print(media);
  return media

calcular_media(pedrin)

# 9- Conversão de temperatura
# Crie duas funções:
# celsius_para_fahrenheit(celsius)
# fahrenheit_para_celsius(fahrenheit)
# As funções devem realizar as conversões utilizando as
# fórmulas:
# ● Fahrenheit = (Celsius × 9/5) + 32
# ● Celsius = (Fahrenheit - 32) × 5/9
# O programa deve solicitar uma temperatura em Celsius e
# outra em Fahrenheit e apresentar os respectivos resultados.

def celsius_para_fahrenheit(celsius):
  result = (celsius * 1.8) + 38;
  print(result);
  return result;


def fahrenheit_para_celsius(fahrenheit):
  result = (fahrenheit - 32) * 1.8;
  print(result);
  return result;

celsius_para_fahrenheit(0);

fahrenheit_para_celsius(48);

# 10- Registro de uma viagem
# Uma empresa de turismo deseja armazenar informações sobre
# uma viagem em uma tupla.
# Crie uma tupla contendo:
# ● cidade de destino;
# ● quantidade de dias;
# ● meio de transporte;
# ● valor da aviagem.
# Exemplo:
# viagem = ("Rio de Janeiro", 5, "Ônibus", 850.00)

viagem = ("Maranhão", 7, "Trem", 35.00);
# O programa deve:
# A) apresentar a tupla completa;
print(viagem);
# B)apresentar a quantidade de elementos;
print(len(viagem));
# C)verificar se "Ônibus" está presente na tupla
# utilizando o operador in;
print("Ônibus" in viagem)
# D) criar uma nova tupla acrescentando uma
# informação sobre o tipo de hospedagem;
viagem2 = ("Sapopemba", 28, "Mobilete", 3267.00, "Hotel 3 Estrelas");
# E) apresentar a nova tupla.
print(viagem2)



# 11- Cadastro de produto
# Crie um programa que solicite ao usuário os dados de um
# produto:
# ● Nome do produto;
# ● Categoria;
# ● Preço;
# ● Quantidade em estoque;
# ● Código do produto.
# Após receber os dados, crie um dicionário contendo todas
# essas informações.
# O programa deve:
# 1. Imprimir o dicionário completo;
# 2. Imprimir cada informação individualmente utilizando
# suas respectivas chaves;
# 3. Calcular e apresentar o valor total em estoque,
# considerando: preço × quantidade


# 12- Sabendo que:
# crie uma função area_circulo que recebe o diâmetro em cm e
# deve retornar a área do círculo em cm2.
# Crie a função raio_circulo que recebe o diâmetro e retorna o
# raio. use ela na função anterior.
# Crie pelo menos duas chamadas de teste para a função que
# está criando.
