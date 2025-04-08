
import clipboard
#from testes2 import __arquivinho__

#### Alguns exemplos de Funções Python ####

def saudacao(nome: str) -> str:
    return f"Olá {nome}"

def somar (a: int, b: int) -> int:
    return a+b

def somar_todos(*args):
    return sum(args)

def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


print(saudacao("Junio"))
print("...")
print(somar(7, 3))
print("...")
print(somar_todos(7, 3, 3, 9))
print("...")
print( exibir_dados(nome="Ana", idade=25) )
print("...")



#### Funções Lambda ####
somar_lambda = lambda x, y: x + y
print(somar_lambda(7,7))


#### list() e map() ####
print(list())
print("...")
print(list("testando"))
print("...")
print("...")
print("...")

#print(__file__)
#print(__arquivinho__)



clipboard.copy("ok ok ok ")
print(clipboard.paste())



# um exemplo de algo que seria usado como uma INTERFACE:
# https://www.youtube.com/watch?v=xd-_oEKu_b4
class DatabaseTeste:
    def connect(self, k: str) -> str:
        ...




