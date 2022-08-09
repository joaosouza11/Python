print("10 termos de uma progressão aritmética")

n1 = int(input("Primeiro termo: "))
n2 = int(input("Razão: "))

#Fórmula para descobrir qual é o 10° termo
dec = n1 + 10 * n2

for i in range(n1, dec, n2):
  print(i, end=" ➙  ")
print("Acabou")