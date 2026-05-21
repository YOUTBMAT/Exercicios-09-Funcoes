texto = input("Digite algo: ")

def inverter(string):
    resultado = ""
    for letra in string:
        resultado = letra + resultado
    return resultado

print(inverter(texto))
