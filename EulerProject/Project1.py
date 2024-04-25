# Find the sum of the multiples of 3 and 5 that are less than 1000, without repetition
S3 = ((3 + 999) * 333)/2
S5 = ((5 + 995) * 199)/2
S15 = ((15 + 990) * 66)/2
Resultado = S3 + S5 - S15

print(f"A resposta da questão 1 é: {Resultado}")
