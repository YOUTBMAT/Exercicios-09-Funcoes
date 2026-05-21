def contar_caracteres():
    texto = input("Digite uma palavra/frase: ")
    caractere = input("Digite qual caractere deseja contar: ")
    quantidade = texto.count(caractere)
    print(quantidade)

contar_caracteres()