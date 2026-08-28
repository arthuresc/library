
lista_compras = ["ovo", "pão", "leite", "presunto"]
print(lista_compras)
print(type(lista_compras))
#
print(lista_compras[0])
print(type(lista_compras[0]))
#
print(lista_compras[-2])
print(len(lista_compras)) #4
# slice
print(lista_compras[1:3])
print(lista_compras[1:])
print(lista_compras[:3])

lista = ["a", 1, 3.14, True, False]
print(type(lista[3]))
lista[3] = False
print(lista)

#
lista_compras.append("mantega")
print(lista_compras)
lista_compras.remove("presunto")
print(lista_compras)

a = [5,8,7,1]
a.sort()
a.reverse()
print(a)

print(a.pop())
print(a)

minha_tupla = (1,1,5,6)
print(minha_tupla)
print(type(minha_tupla))
print(minha_tupla[2])
#minha_tupla[0] = 123
t = (5,)
print(len(t))
#
estrutura = [[("ola", "mundo"), "python"], 1, 2, (3,4)]
print(len(estrutura))
print(len(estrutura[0]))
print(estrutura[0][1])
print(estrutura[0][0][1])
print(estrutura[3][1])

ident_2 = [[1,0],[0,1]] # matrix
print(ident_2[0][1])
#
a = "ola"
b = " mundo"
a = a + b
print(a)
# 
a = [1,2,3]
b = a
a.append(4)
print(b)
#
a = "ola"
b = " mundo"
c = a
a = a + b
print(c)
#
aluno = {"Nome": "Bob da Silva", "idade": 21, "altura": 1.83}
print(type(aluno))
print(aluno["Nome"])
print(aluno["idade"])
print(aluno.keys())
print(aluno.values())

def abra_cadabra():
    print("!!!!!!!!!!!!!!!!")
    print("apareceu um coelho")
    print("!!!!!!!!!!!!!!!!")

print("fim!")
abra_cadabra()
print("tanana...")
abra_cadabra()

def soma(a,b):
    return a + b

x = soma(2, 5)
print(x)
#
x = abra_cadabra()
print(x)

def fun_inv(a,b):
    return b, a

x, y = fun_inv(5, 6)
print(x)

x = fun_inv(1, 2)
print(type(x))

def fun_x():
    return 1,2,4

x = fun_x()
print(x)

a = 1
b = 2
def yyy(a):
    return a * b

print(yyy(5))
#####
a = 123
def yyy():
    a = "ola mundo"

yyy()
print(a)

# 
batata = 1
def pc(Batata):
    print(batata)

pc("ola mundo")

def yyy(a=5,b=0):
    print(a)
    print(b)

yyy(b=2)


