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

def soliciteIdade(pIdade):
  idade = pIdade
  if idade < 12:
    print("Criança")
  if idade <= 12 and idade >= 17:
    print("Adolescente")
  if idade <= 18 and idade >= 59:
    print("Adulto")
  if idade >= 60:
    print("Idoso")
  
  
  
soliciteIdade(78)
soliciteIdade(13)
soliciteIdade(34)


# 2) Função chamada retorna_maior
# Essa função deverá receber 2 números inteiros e voltar o valor
# do maior valor.
# Exemplo:
# print(retorna_maior(3, 4)) # 4
# print(retorna_maior(8, 5)) # 8

def retorna_maior(a, b):
  return a if a > b else b  

retorna_maior(1, 2)
retorna_maior(6, 2)

# 3) Crie a função calc_desconto
# 1
# Receba o valor de uma compra (número de ponto flutuante):
# - Até R$100 → 5% de desconto
# - Até R$500 → 10% de desconto
# - Acima de R$500 → 15% de desconto
# Mostre o valor final com desconto.