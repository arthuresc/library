import math


# 1) Crie um programa em Python que:
# - Solicite ao usuário sua idade.
# - Verifique:
  # Se a idade for menor que 0 → imprima "Idade inválida"
  # Se for menor que 12 → imprima "Criança"
  # Se for entre 12 e 17 → imprima "Adolescente"
  # Se for entre 18 e 59 → imprima "Adulto"
  # Se for 60 ou mais → imprima "Idoso"
# def soliciteIdade(pIdade = None):
#   idade = pIdade or input("Digite sua idade: ");
#   print("Teste final", idade)

def solicite_idade(propsIdade):
  idade = propsIdade
  if idade < 12:
    print("Criança")
  if idade >= 12 and idade <= 17:
    print("Adolescente")
  if idade >= 18 and idade <= 59:
    print("Adulto")
  if idade >= 60:
    print("Idoso")
    

solicite_idade(78)

# 2) Função chamada retorna_maior
# Essa função deverá receber 2 números inteiros e voltar o valor
# do maior valor.
# Exemplo:
# print(retorna_maior(3, 4)) # 4
# print(retorna_maior(8, 5)) # 8

def retorna_maior(a:int,b:int):
  return a if a > b else b;

print(retorna_maior(1,3))
print(retorna_maior(5,3))

# 3) Crie a função calc_desconto
# Receba o valor de uma compra (número de ponto flutuante):
# - Até R$100 → 5% de desconto
# - Até R$500 → 10% de desconto
# - Acima de R$500 → 15% de desconto
# Mostre o valor final com desconto.
# Exemplo: Se o valor original é R$ 100, a redução será: (R$ 100 - (R$ 100 × 0,25)) / R$ 100 = R$ 75.

def calc_desconto(valorCompra: float):
  teste: int;
  if valorCompra <= 100:
    teste = 100
  elif valorCompra <= 500:
    teste = 500
  else:
    teste = 501
  desconto = {
  100: 0.05,
  500: 0.10,
  501: 0.15
  }[teste]
  result: float = valorCompra - (valorCompra * desconto)
  return result
  
  

print(calc_desconto(100))
print(calc_desconto(120))
print(calc_desconto(1000))

# 4) Crie uma função chamada
# calc_hipotenusa essa função recebe todo lados catetos do
# triângulo e retorna o valor inteiro da hipotenusa

def calc_hipotenusa(ca,cb):
  hipotenusa = math.sqrt((ca ** 2) + (cb ** 2))
  return int(hipotenusa)

print(calc_hipotenusa(3,4))


# 5) Função de Triângulo
# Criar uma função chamada eh_triangulo que recebe três
# inteiros (Tamanho de três retas) e retorna um valor booleano
# (bool) True se os valores inteiros formarem um triângulo e
# Falso se for impossível formar um triângulo.
# Lembrete Matemático - Só irá existir um triângulo se,
# somente se, os seus lados obedecerem à seguinte regra: um de
# seus lados deve ser maior que o valor absoluto (módulo) da
# diferença dos outros dois lados e menor que a soma dos outros
# dois lados.


def eh_triangulo(a, b, c):
    # Verifica a condição para todos os lados
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    return False
  
print(eh_triangulo(3,4,6))
print(eh_triangulo(3,6,34))
print(eh_triangulo(3, 4, 5)) # True
print(eh_triangulo(1, 2, 3)) # False
print(eh_triangulo(2, 2, 2)) # True
print(eh_triangulo(0, 4, 5)) # False

# 6) Implemente a função valida_z
# A função deverá fazer o que está descrito no fluxograma
# abaixo:

def valida_z():
  print("Iniciando fução")
  x = 2
  z = 1
  if x > z:
    print("Verdadeiro")
    if x > 10:
      z = 10
    else:
      z = 20;
  else:
    z = 30
  print(z)
  
# 7) Veja o Pseudo-código abaixo:
# INÍCIO
# ESCREVA "Digite um número inteiro:"
# LEIA numero
# SE (numero MOD 2 = 0) ENTÃO
# ESCREVA "O número é PAR"
# SENÃO
# ESCREVA "O número é ÍMPAR"
# FIMSE
# FIM
# Usando como referência o Pseudo-código implemente: 
# a) o Fluxograma equivalente (use o draw.io) 
# b) Uma função chamada eh_par em Python 
def eh_par():
  numero = input("Digite um número inteiro: ") 
  if numero ** 2 == 0:
    print("O número é PAR")
  else:
    print("O número é IMPAR")
    
eh_par()    
    
# 8)Veja o Pseudo-código abaixo: 
# INÍCIO 
# ESCREVA "Digite a nota do aluno:" 
# LEIA nota 
# ESCREVA "Digite a frequência do aluno (%):" 
# LEIA frequencia 
# SE (nota >= 7 E frequencia >= 75) ENTÃO 
# ESCREVA "Aluno APROVADO" 
# SENÃO 
# ESCREVA "Aluno REPROVADO" 
# FIMSE 
# FIM 
# Usando como referência o Pseudo-código implemente: 
# a) o Fluxograma equivalente (use o draw.io) 
# b) Uma função chamada esta_aprovado em Python

def esta_aprovado():
  nota = input("Digite a nota do aluno: ")
  frequencia = input("Digite a frequência do aluno (%): ")
  
  if nota >= 7 and frequencia >= 75:
    print("Aluno APROVADO")
  else:
    print("Aluno REPROVADO")
esta_aprovado()