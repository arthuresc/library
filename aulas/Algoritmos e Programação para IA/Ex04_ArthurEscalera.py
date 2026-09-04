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
  if idade >= 12 and idade <= 17:
    print("Adolescente")
  if idade >= 18 and idade <= 59:
    print("Adulto")
  if idade >= 60:
    print("Idoso")
    

soliciteIdade(78)

# 2) Função chamada retorna_maior
# Essa função deverá receber 2 números inteiros e voltar o valor
# do maior valor.
# Exemplo:
# print(retorna_maior(3, 4)) # 4
# print(retorna_maior(8, 5)) # 8