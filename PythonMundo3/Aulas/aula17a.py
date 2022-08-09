valores = []
valores.append(3)
valores.append(9)
valores.append(7)

valores.sort()

for c, v in enumerate(valores):
  print(f"Na posição {c} encontrei o valor {v}")
print("Cheguei ao final!")

print("-=" * 15)


numeros = []

for cont in range(0, 5):
  numeros.append(int(input("Digite um valor: ")))

print(f"Você digitou os números ", end="")
for n in numeros:
  print(n, end=" ")