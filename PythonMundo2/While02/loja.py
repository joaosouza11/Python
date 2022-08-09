cont = total = totmil = menor = 0
barato = ""

print("-="*15)
print("{: ^30}".format("LOJA ATACADISTA"))
print("-="*15)

while True:
  nome = str(input("Nome do Produto: "))
  preco = float(input("Preço: R$"))
  total += preco
  cont += 1
  if preco > 1000:
    totmil += 1

  if cont == 1 or preco < menor:
    menor = preco
    barato = nome

  continuar = str(input("Você quer continuar? [S/N]")).strip().upper()[0]
  if continuar == "N":
    break
  print("-="*15)

print("{:-^30}".format(" RECIBO "))
print(f"Você comprou {cont} produtos e o total da compra foi R${total:.2f}")
print(f"{totmil} produtos custaram mais de R$1000")
print(f"O produto mais barato foi {barato} que custou R${menor:.2f}")