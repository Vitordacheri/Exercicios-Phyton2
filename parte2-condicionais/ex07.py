# 7. Peça dois números e exiba qual é o maior. Se forem iguais, informe isso.

num1 = float(input("Digite o primero numero: "))
num2 = float(input("Digite o segundo numero: "))

if num1 > num2:
    print("O primero numero é maior. ") 
elif num2 > num1:
    print("O segundo número é maior")
else:
    print("Os dois números são iguais")

