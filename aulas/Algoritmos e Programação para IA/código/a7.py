import re
import datetime
import random
from datetime import datetime
import random
import string

class BibliotecaStorage:
  def __init__(self):
    pass
    

# Ex 01
class ContaBancaria(object):
  def __init__(self, titular:string, saldo:float):
    self.__titular = titular;
    self.__saldo = saldo;
    
  # @property
  # def saldo(self):
  #   return self.__saldo
  
  # @saldo.setter
  # def saldo(self, value):
  #   self.__saldo = value
  #   return self.__saldo
    
  @property
  def titular(self):
    return self.__titular
  
  @titular.setter
  def titular(self, value):
    self.__titular = value
    return self.__titular
  
  def depositar(self, valorDeEntrada):
    saldoAntigo = self.__saldo
    self.__saldo = self.__saldo + valorDeEntrada
    print(f"Seu saldo era de R${saldoAntigo} e agora é de R${self.__saldo}")
    
  def sacar(self, valorDeSaida):
    saldoAntigo = self.__saldo
    self.__saldo = self.__saldo - valorDeSaida
    print(f"Seu saldo era de R${saldoAntigo} e agora é de R${self.__saldo}")
        
  def extrato(self):
    print(f"Olá {self.__titular}, seu saldo é de: R${self.__saldo}.")


a = ContaBancaria("Arthur", 3.5)

a.extrato()

# Ex 02
class AuxMixin:
  
  def __init__(self):
    self._padrao = {
      "email":r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
      "data":r"^\d{2}/\d{2}/\d{4}$",
      "telefone":r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$",
      "cpf":r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
    }
    
  def validar(self, pattern, value):
    try:
      match = re.match(pattern, value)
      if (not match):
        raise ValueError("O valor não corresponde a formatação esperada")
      else:
        return value
    except ValueError as erro:
      print(f"Falha na validação do campo: {erro}")
      raise ValueError
    
  def gerarMatricula(self):
    data = datetime.strftime('%d/%m/%Y')
    dataEdit = datetime.strftime('%d%m-%Y')
    numero = random.randint(000000, 999999)
    letra = string.ascii_letters[random.randint(0,9)]
    return f"{letra}{numero}{dataEdit}"
      
      
      #lançar a exception correta e alterada para dizer que está errado o padrão
        
      
class Pessoa(AuxMixin):
  
  def __init__(self, nome:string, cpf:string, email:string, data_nascimento:string, endereco:string, telefone:string):
    
    super().__init__()
    
    self.__nome = nome
    self.__cpf = self.validar(self._padrao["cpf"], cpf)
    self.__email = self.validar(self._padrao["email"], email)      
    self.__data_nascimento = self.validar(self._padrao["data"], data_nascimento)
    self.__endereco = endereco
    self.__telefone = self.validar(self._padrao["telefone"], telefone)
    
  def exibir_dados(self):
    print(f"Olá {self.__nome},\nseu [[aula banco - 22-10-2026]] é {self.__email}, nascido em {self.__data_nascimento}\nResidente do endereço: {self.__endereco} \nTelefone: {self.__telefone}")
  
  def fazer_aniversario():
    print(f"Feliz aniversário, se hoje for o dia {self.__data_nascimento}")

  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(self, value):
    self.__email = value

  @property
  def telefone(self):
    return self.__telefone
  
  @telefone.setter
  def telefone(self, value):
    self.__telefone = value
    


arthur = Pessoa("Arthur", "42351460847", "arthur@gmail.com", "21/05/1992", "Rua La Sei eu, 32", "11976548765")

arthur.exibir_dados()
  

class Usuario(Pessoa):
  def __init__(self, nome: str, cpf: str, email: str, data_nascimento: str, endereco: str, telefone: str):

    
    super().__init__(nome, cpf, email, data_nascimento, endereco, telefone)
    
    self.matricula = self.gerarMatricula()


b = Usuario("Arthur", "42351460847", "arthur@gmail.com", "21/05/1992", "Rua La Sei eu, 32", "11976548765")

print(b.matricula)