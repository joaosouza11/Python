maior = 0
menor = 0

for p in range (1,6):
  peso = float(input("Digite o peso da {}° pessoa:  ".format(p)))
  #Caso a primeira pessoa tenha o valor maior ou menor
  if p == 1:
    maior = peso
    menor = peso
  #Para as demais pessoas
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso

print("O maior peso é {}Kg".format(maior))
print("O menor peso é {}Kg".format(menor))