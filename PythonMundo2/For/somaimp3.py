#Realizar a soma de todos os números ímpares múltiplos de 3 entre 1 e 500

n = 0
cont = 0
#Para saber se são ímpares
for i in range (1, 501, 2):
  #Para saber se é múltiplo de 3
  if i % 3 == 0:
    cont += 1
    n += i
print("A soma de todos os {} valores solicitados é {}".format(cont, n))