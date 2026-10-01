positivo = 0

while True:
    numero = float(input("Digite um número (ou 0 para sair): "))

    if numero == 0:
        break
    if numero > 0:
        positivo += 1

print(f"Quantidade de números positivos digitados: {positivo}")
