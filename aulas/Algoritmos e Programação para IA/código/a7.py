import re
import datetime
import random
# from datetime import datetime
import random
import string
from typing import Literal

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
    data = datetime.now()
    dataEdit = data.strftime('%d%m-%Y')
    numero = random.randint(000000, 999999)
    letra = string.ascii_uppercase[random.randint(0,26)]
    result = f"{letra}{numero}{dataEdit}"
    return result
      
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
    print(f"Olá {self.__nome},\nseu {self.__cpf} e seu email é {self.__email}, nascido em {self.__data_nascimento}\nResidente do endereço: {self.__endereco} \nTelefone: {self.__telefone}")
  
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

class StatusUsuario(enumerate):
  ATIVO = "ATIVO"
  SUSPENSO = "SUSPENSO"
  BLOQUEADO = "BLOQUEADO"
  
    
class LivroHistorico:
  def __init__(self, livro):
    self.__nome = livro.nome
    self.__isbn = livro.isbn
    self.__dataEmprestimo = datetime.now()
    self.__dataDevolução = None
    
  @property
  def data_devolucao(self):
    return self.__dataDevolução

  @data_devolucao.setter
  def data_devolucao(self):
    self.__dataDevolução = datetime.now()
  
class Usuario(Pessoa):
  def __init__(self, nome: str, cpf: str, email: str, data_nascimento: str, endereco: str, telefone: str, livros_emprestados: [Livro] , historico_emprestimos:[dict], multa:float, status:str):

    
    super().__init__(nome, cpf, email, data_nascimento, endereco, telefone)
    
    self.__matricula = self.[[aula banco - 29-10-2026]]Matricula()
    self.__livros_emprestados = livros_emprestados #lista de objetos Livro
    self.__historico_emprestimos = historico_emprestimos #lista de dicionarios {data_emprestimo, data_devolucao, livro}
    self.__multa = multa
    self.__status = getattr(StatusUsuario, f"{status}", "ATIVO")
  
  
  @property
  def status(self):
    return self.__status
  
  @status.setter
  def status(self, value):
    self.__status = getattr(StatusUsuario, f"{status}", "ATIVO")
  
  
  @property
  def livros_emprestados(self):
    return self.__titular
  
  @livros_emprestados.setter
  def livros_emprestados(self, value):
    self.__livros_emprestados.append(value)
    return self.__livros_emprestados

  def pegar_livro_emprestado(livro:Livro, funcionario):
    if len(self.__livros_emprestados) > 3:
      raise Exception("Você não poder estar com mais de 3 livros emprestados")
    else:
      #//TODO implementar função emprestar
      livro.emprestar(self, funcionario)
      # 
      # adiciona ao histórico
      self.__livros_emprestados = livro
  
  def devolver_livro(self, livro):
    for i in self.__livros_emprestados:
      if i.isbn == livro.isbn:
        if not livro.disponivel:
          self.remover_historico(livro)
          livro.devolver()
        else:
          raise Exception("Este livro não deve ser devolvido")
    
    
  def remover_historico(self, livro):
    for l in self.__livros_emprestados:
      if l.isbn == livro.isbn:
        for livro_registrado in self.__historico_emprestimos:
          if livro_registrado == livro.isbn:
            self.__historico_emprestimos.remove(livro_registrado)
            
  # devolver o livro: remove da lista de livros emprestados, marca o livro como não emprestado, 
  def devolver_livro(self, livro):
    for l in self.__livros_emprestados:
      if l.isbn == livro.isbn:
        self.remover_historico(livro)
        livro.disponivel = true
  
  
  # Sempre retorna a diferença de valores pagos
  def pagar_multa(self, valor:float):
    if valor > self.__multa:
      troco = valor - self.__multa
      self.__multa = 0
      print(f"O pagamento da multa foi feito, receba R${troco} de troco.")
      return troco
    elif valor < self.__multa:
      saldo_devedor = self.__multa - valor
      self.__multa = saldo_devedor      
      print(f"O pagamento parcial da multa foi feito, lhe restando uma divida de R${saldo_devedor}")
      return saldo_devedor
    else:
      print(f"Tamo quite, ta tudo certo.")
      self.__multa = 0
      return self.__multa
    
  
  def consultar_historico(self):
    for i in self.__historico_emprestimos:
      print(f"Livro emprestado {i}\n")
      
  def verificar_status(self):
    if self.status != "ATIVO":
      print(f"Você não esta com o status ATIVO")
      return False
      if self.__multa > 50:
        print(f"Você esta devendo acima do permitido")
        return False
      else:
        return True
  
  def calcular_gasto_total():
    pass




b = Usuario("Arthur", "42351460847", "arthur@gmail.com", "21/05/1992", "Rua La Sei eu, 32", "11976548765", [], [], 3.90, 3)
b.printStatus()