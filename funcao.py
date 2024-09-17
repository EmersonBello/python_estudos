def trabalho (nome):
    print(f"quem ira trabalhar é {nome}")

def horario (horas):
    print(f"quanatas horas {horas} ")

def setor (tipo):
    print(f"o setor é {tipo}")

def carreira (nome,horas,tipo):
    trabalho(nome)
    horario(horas)
    setor(tipo)

carreira("joao","13 a 15", "engenharia")    

def soma_num(num1,num2):
    return num1 + num2
resultado = soma_num(20,20)
print(f"o resultado da soma é {resultado}")


# funções dinâmicas
def maior_num(lista_num):
    return max(lista_num)

lista_total = maior_num([2, 3, 54, 344, -56, 344])
print(lista_total)

def verifica_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num_primo = verifica_primo(44)
print(num_primo) 

def verifica_par_impar(lista):
    for num in lista:
        if num % 2 == 0:
            print(f"{num} é par")
        else:
            print(f"{num} é impar")

lista_numeros = verifica_par_impar([2, 3, 4, 5, 6, 7, 8, 9, 10])
print(lista_numeros)
