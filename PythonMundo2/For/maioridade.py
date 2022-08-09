from datetime import datetime

atual = datetime.today().year
demaior = 0
demenor = 0

for i in range(1,8):
  nasc = int(input("({}° Pessoa) Ano de nascimento: ".format(i)))
  idade = atual - nasc
  if idade >= 18:
    demaior += 1
  else:
    demenor += 1

#Mesmo já sabendo a quantidade de maior, realizei a contagem "demenor" para ter certeza do resultado

print("Existem {} pessoas maiores de idade e {} menores de idade".format(demaior, demenor))