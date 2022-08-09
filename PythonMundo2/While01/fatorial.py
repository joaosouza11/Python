n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
f = 1 #Elemento neutro de uma fatorial

print("Calculando {}! = ".format(n), end="")
while c > 0:
  print("{}".format(c), end = "")
  print(" x " if c > 1 else " = ", end="") #Formatação da output
  f *= c
  c -= 1
print("{}".format(f))


'''Forma simplificada utilizando biblioteca

from math import factorial

n = int(input("Digite um número para calcular seu Fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}".format(n, f))'''