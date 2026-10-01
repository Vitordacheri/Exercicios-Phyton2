lista = [3, 4, 6, 8, 10]

maior_numero = lista[0]

for numero in lista:
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número na lista é: {maior_numero}")