def e_palindromo():
    palavra = input("Digite uma palavra: ")
    resultado = ""
    for letra in palavra:
        resultado = letra + resultado
    if resultado == palavra:
        True
        print("A palavra é um palíndromo")
    else:
        False
        print("A palavra não é um palíndromo")

e_palindromo()