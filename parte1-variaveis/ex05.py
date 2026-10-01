# 5. Peça o preço de um produto e a quantidade comprada. Exiba o valor total, com duas casas decimais.
preco = float(input("Digite o Preço do produto: "))  #casting
quantidade = int(input("Digite a quantidade comprada: "))

total = preco * quantidade 

print(f"Valor total: R${total:.2f}")