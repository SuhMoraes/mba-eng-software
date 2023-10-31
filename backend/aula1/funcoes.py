# Criando uma função com Python com def
def soma():
    print(40+2)

soma()

def soma_com_argumentos(a, b):
    print(a +b)
    
soma_com_argumentos(5,45)
soma_com_argumentos(35, 45)


def soma_com_argumentos_e_retorno(a,b):
    return a + b

resposta = soma_com_argumentos_e_retorno(80, 20)
print(resposta)