n = int(input("Digite um número inteiro: "))
count = 0

#Saber se é divisível e mostrar os respectivos números
for i in range(1, n+1):

  #Divisível
  if n % i == 0:
    print("\033[32m", end="")
    count += 1

  #Não divisível
  else:
    print("\033[31m", end="")
  print("{} ".format(i), end="")

#Contar quantas vezes é divisível
print("\n\33[m0 número {} foi divisível {} vezes".format(n, count))
if count == 2:
  print("Então, é um número PRIMO!")
else:
  print("Então, NÃO é um número PRIMO!")