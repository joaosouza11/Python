avancar = "S"
count = total = maior = menor = 0

while avancar == "S":
  n = int(input("Digite um número: "))
  avancar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
  total += n
  count += 1

  #Apenas um valor, ele vai ser o MENOR e o MAIOR ao mesmo tempo
  if count == 1:
    maior = menor = n
  #Mais de um valor
  else:
      if n > maior:
        maior = n
      if n < menor:
        menor = n

media = total / count
print("Você digitou {} valores e a média foi {:.2f}".format(count, media))
print("O menor valor foi {} e o maior foi {}". format(menor, maior))