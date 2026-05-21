# --- SEM parâmetro, SEM retorno ---
def soma_fixa():
    resultado = 4 + 2
    print(resultado)

soma_fixa()  # Output: 6


# --- COM parâmetro, SEM retorno ---
def soma(x, y):
    print(x + y)

soma(4, 2)   # Output: 6
soma(10, 5)  # Output: 15


# --- COM parâmetro, COM retorno ---
def soma_retorno(x, y):
    return x + y

print(soma_retorno(4, 2))  # Output: 6

# o retorno pode ser guardado numa variável
resultado = soma_retorno(10, 5)
print(resultado)  # Output: 15