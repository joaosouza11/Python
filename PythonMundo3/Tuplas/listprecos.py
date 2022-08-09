lista = ("Lápis", 1.75, "Borracha", 2.00, "Caneta", 3.00, "Caderno", 15.90, "Pincel", 9.90, "Estojo", 15.00)

print("-=" * 15)
print(f'{"LISTA DA LOJA":^30}')
print("-=" * 15)

for pos in range(0, len(lista)):
  if pos % 2 == 0:
    print(f"{lista[pos]:.<22}", end=" ")
  else:
    print(f"{lista[pos]:>4.2f}")