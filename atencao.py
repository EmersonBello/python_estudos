from decimal import Decimal, getcontext

getcontext().prec = 2


n = int(input())
k = int(input())

if (1 <= n <= 100) and (1 <= k <= 1000):
    valor = n - 1
    valor2 = k - valor
    
    divicao = Decimal(valor2) / Decimal(n)
    resultado = f"{divicao:.1f}"
    
    print(resultado)
else:
    print("Error")