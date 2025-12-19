codigo1, qtd1, valor1  = input().split()
codigo2, qtd2, valor2  = input().split()

codigo1 = int(codigo1)
qtd1 = int(qtd1)
valor1 = float(valor1)

codigo2 = int(codigo2)
qtd2 = int(qtd2)
valor2 = float(valor2)


resultado = (qtd1 * valor1 + qtd2 * valor2)

print(f"VALOR A PAGAR: R$ {resultado:.2f}")