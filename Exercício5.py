texto = input("Digite algo: ")

def inverter(string):
    resultado = ""
    for letra in string:
        resultado = letra + resultado  # Adiciona a letra antes do texto acumulado
    return resultado

print(inverter(texto))
