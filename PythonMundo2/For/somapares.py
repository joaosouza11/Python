soma = 0
cont = 0

for i in range(1, 7):
  n = int(input("Digite o {}° valor: ".format(i)))
  if n % 2 == 0:
    soma += n
    cont += 1

#Se o usuário digitar apenas 1 número par
if cont == 1:
  print("Você digitou apenas 1 número par, então o resultado deu {}".format(soma))
#Se o usuário digitar vários números pares
else:
  print("A soma dos {} números pares deu {}".format(cont, soma))